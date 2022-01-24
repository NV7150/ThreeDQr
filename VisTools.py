import numpy as np
import open3d as o3d


def print_vox(v_p, c_arr, size=2):
    points = []
    colors = []
    for x in [n / 100 for n in range(-size, size, 1)]:
        for y in [n / 100 for n in range(-size, size, 1)]:
            for z in [n / 100 for n in range(-size, size, 1)]:
                points.append(v_p + np.array([x, y, z]))

                colors.append(c_arr)

    return o3d.utility.Vector3dVector(np.array(points)), o3d.utility.Vector3dVector(np.array(colors))
