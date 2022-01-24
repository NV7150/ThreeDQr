import glob
import os
import open3d as o3d

from QrCodeDefiner import *
from VisTools import print_vox

pcd = o3d.io.read_point_cloud("resources/Data2.ply")
frame_json_pathes = glob.glob(os.path.join("resources", "2022_01_12_16_15_51", "frame_*.json"))

def_pos = define_qr_pos(frame_json_pathes, pcd)

res_pcd = o3d.geometry.PointCloud()

(p, c) = print_vox(def_pos['142422061877'], [255, 255, 0])
(p2, c2) = print_vox(def_pos['135322064678'], [255, 0, 255])
p.extend(p2)
c.extend(c2)

res_pcd.points = p
res_pcd.colors = c

o3d.visualization.draw_geometries([pcd, res_pcd])