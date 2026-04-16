from pydantic import BaseModel
from .frame_collection_meta import FrameCollectionMeta
from .sensor_frames import UnknownSensor1FrameBase, UnknownSensor2FrameBase, UnknownSensor3FrameBase

class CombinedFrameBase(BaseModel):
    unknown_sensor_1: UnknownSensor1FrameBase
    unknown_sensor_2: UnknownSensor2FrameBase
    unknown_sensor_3: UnknownSensor3FrameBase

class CombinedFrameCollection(BaseModel):
    meta: FrameCollectionMeta
    frames: list[CombinedFrameBase]