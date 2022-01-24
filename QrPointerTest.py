import numpy
import open3d as o3d
from FrameLoader import Frame
from QrPointer import *
import QrCodeDecoder

frame = Frame.from_json("resources/2022_01_12_16_15_51/frame_00315.json")
pcd = o3d.io.read_point_cloud("resources/Data2.ply")

qrcode = QrCodeDecoder.decode_image(frame.image_path)[0]

pos = get_qr_from_frame(qrcode, frame)

(rc_pos, rc_dist, true_point) = ray_cast_qr(frame, pos, pcd)
print(rc_dist)


def print_vox(v_p, c_arr, size=2):
    points = []
    colors = []
    for x in [n / 100 for n in range(-size, size, 1)]:
        for y in [n / 100 for n in range(-size, size, 1)]:
            for z in [n / 100 for n in range(-size, size, 1)]:
                points.append(v_p + np.array([x, y, z]))

                colors.append(c_arr)

    return o3d.utility.Vector3dVector(numpy.array(points)), o3d.utility.Vector3dVector(numpy.array(colors))


result_pcd = o3d.geometry.PointCloud()
(p, c) = print_vox(rc_pos, [0, 255, 0])
(p2, c2) = print_vox(true_point, [255, 0, 0])
p.extend(p2)
c.extend(c2)
result_pcd.points = p
result_pcd.colors = c


o3d.visualization.draw_geometries([pcd, result_pcd])

