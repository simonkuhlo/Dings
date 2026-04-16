from pydantic import BaseModel


class FrameCollectionMeta(BaseModel):
    fps: int
    #additional information like start time, etc.