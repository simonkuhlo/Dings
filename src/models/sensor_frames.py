from pydantic import BaseModel

class Vector3(BaseModel):
    x: float
    y: float
    z: float

class Transform3D(BaseModel):
    position: Vector3
    rotation: Vector3

# Unknown device TODO: Rename
class UnknownSensor1FrameBase(BaseModel):
    force_l_heel: float
    force_l_medial: float
    force_l_lateral: float
    force_l_total: float

    force_r_heel: float
    force_r_medial: float
    force_r_lateral: float
    force_r_total: float

# Unknown device by Movella Technologies TODO: Rename
class UnknownSensor2FrameBase(BaseModel):
    euler: Vector3
    acc: Vector3
    gyro: Vector3

# Unknown motion capture device TODO: Rename
class UnknownSensor3FrameBase(BaseModel):
    center_of_gravity: Vector3 #in mm
    l_wrist: Transform3D #in mm and deg
    l_elbow: Transform3D
    l_shoulder: Transform3D
    r_wrist: Transform3D
    r_elbow: Transform3D
    r_shoulder: Transform3D
    l_toe: Transform3D
    l_ankle: Transform3D
    # [...]
    #TODO finish defining
