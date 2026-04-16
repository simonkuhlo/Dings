from nicegui import ui, events
from sensor_input_visualizer import sensor_input
from sensors.sensor1 import Sensor1
from sensors.sensor2 import Sensor2
from sensors.sensor3 import Sensor3


async def handle_upload(e: events.UploadEventArguments):
    content = await e.file.text()
    sensor = Sensor1()
    sensor_data = sensor.parse(content)
    text: str = f"Sensor: {sensor.meta.name} \n"
    text += f"FPS: {sensor_data.meta.fps} \n"
    text += f"Frames ({len(sensor_data.frames)}): \n"
    index = 0
    for frame in sensor_data.frames:
        text += f"{index} : {frame} \n"
        index += 1
    ui.label(text=text).style('white-space: pre-wrap')


if __name__ in {"__main__", "__mp_main__"}:
    ui.context.client.content.classes('h-screen')
    with ui.tabs().classes('w-full') as tabs:
        input_tab = ui.tab('Input')
        modify_tab = ui.tab('Modify')
        output_tab = ui.tab("Output")
    with ui.tab_panels(tabs, value=input_tab).classes('w-full max-w-200 self-center'):
        tab_panel = ui.tab_panel(input_tab)
        with tab_panel:
            sensor_input(tab_panel, Sensor1())
            sensor_input(tab_panel, Sensor2())
            sensor_input(tab_panel, Sensor3())
            ui.button("+ Add Sensor").classes("w-full")
        with ui.tab_panel(modify_tab):
            ui.label('Modify Tab')
        with ui.tab_panel(output_tab):
            with ui.row().classes('w-full items-center justify-between'):
                ui.label("Prefix properties")
                ui.checkbox()
            with ui.row().classes('w-full items-center justify-between'):
                ui.label("Format")
                ui.select(["csv", "json"], value="csv")
            ui.button('Generate & Download', on_click=lambda: ui.download("/")).classes("w-full")

    ui.run(host='localhost', port=8080)