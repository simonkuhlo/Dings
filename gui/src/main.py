from nicegui import ui, events
from sensors.sensor1 import Sensor1

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
    ui.upload(label="Upload UnknownSensor1 data", on_upload=handle_upload, max_files=1)
    ui.run(host='localhost', port=8080)