import json
import os
import glob
import trimesh
from imageio import imread, imwrite
import numpy as np


def to_arr(m):
    m = np.array(m)
    shape = int(np.sqrt(m.shape[0]))
    return m.reshape((shape, shape))


class Frame:
    pose = None
    pos = None
    rotate = None
    projection_matrix = None
    intrinsics = None
    image_path = None
    has_image = None

    @staticmethod
    def from_json(json_path: str):
        d = json.load(open(json_path, 'r'))
        f = Frame()
        f.image_path = json_path.replace(".json", ".jpg")
        f.has_image = os.path.exists(f.image_path)

        # extended rotation matrix
        f.pose = to_arr(d["cameraPoseARFrame"])
        f.pos = f.pose[:3, 3:].flatten()
        f.rotate = f.pose[:3, :3]
        f.rotate = np.concatenate([f.rotate, np.zeros((3, 1))], axis=1)
        f.rotate = np.concatenate([f.rotate, np.array([[0, 0, 0, 1]])], axis=0)

        f.projection_matrix = to_arr(d["projectionMatrix"])
        f.intrinsics = to_arr(d["intrinsics"])
        return f


