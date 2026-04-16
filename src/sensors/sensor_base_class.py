from pathlib import Path
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .sensor_meta import SensorMeta
from models.frame_collection_meta import FrameCollectionMeta


TFrameModel = TypeVar("TFrameModel")

class SensorData(Generic[TFrameModel]):
    def __init__(self, meta: FrameCollectionMeta, frames: list[TFrameModel]):
        self.meta: FrameCollectionMeta = meta
        self.frames: list[TFrameModel] = frames

class SensorBaseClass(ABC, Generic[TFrameModel]):
    @property
    @abstractmethod
    def meta(self) -> SensorMeta:
        raise NotImplementedError()

    def parse_file(self, path: Path) -> SensorData[TFrameModel]:
        content: str = ""
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return self.parse(content)

    @abstractmethod
    def parse(self, data: str) -> SensorData[TFrameModel]:
        raise NotImplementedError()