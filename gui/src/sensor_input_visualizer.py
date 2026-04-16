from nicegui import ui, events

from sensors.sensor_base_class import SensorBaseClass


async def handle_upload(e: events.UploadEventArguments):
    pass

def sensor_input(parent, sensor: SensorBaseClass):
    with parent:
        with ui.card().classes("w-full"):
            with ui.row().classes('w-full items-center justify-between'):
                ui.label(sensor.meta.name)
                with ui.dropdown_button('Settings', icon='settings'):
                    with ui.card().classes("w-80"):
                        with ui.row().classes('w-full items-center justify-between'):
                            ui.label("Property prefix")
                            ui.input(value=sensor.meta.property_prefix).classes("w-30")
            ui.separator()
            ui.upload(label="Upload data", on_upload=handle_upload, max_files=1).classes("w-full")