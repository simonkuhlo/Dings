from models.frame_collection_meta import FrameCollectionMeta
from sensors.sensor_base_class import SensorBaseClass, SensorData, TFrameModel
from models.sensor_frames import UnknownSensor1FrameBase
from sensors.sensor_meta import SensorMeta


class Sensor2(SensorBaseClass[UnknownSensor1FrameBase]):
    @property
    def meta(self) -> SensorMeta:
        return SensorMeta(
            name = "Unknown Sensor 2",
            property_prefix = "us2"
        )

    def parse(self, data: str) -> SensorData[UnknownSensor1FrameBase]:
        lines = [line.rstrip("\n") for line in data.splitlines() if line.strip()]
        if len(lines) < 3:
            return SensorData(meta=FrameCollectionMeta(fps=1), frames=[])

        data_start = 3

        frames: list[UnknownSensor1FrameBase] = []

        for line in lines[data_start:]:
            parts = line.split("\t")

            if len(parts) < 9:
                continue

            try:
                frame = UnknownSensor1FrameBase(
                    force_l_heel=float(parts[1]),
                    force_l_medial=float(parts[2]),
                    force_l_lateral=float(parts[3]),
                    force_l_total=float(parts[4]),
                    force_r_heel=float(parts[6]),
                    force_r_medial=float(parts[7]),
                    force_r_lateral=float(parts[8]),
                    force_r_total=float(parts[9]),
                )
            except (ValueError, IndexError):
                continue

            frames.append(frame)

        return SensorData(meta=FrameCollectionMeta(fps=1), frames=frames)

