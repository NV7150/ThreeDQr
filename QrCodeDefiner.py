from FrameLoader import Frame
from QrCodeDecoder import QRCode, decode_image
from QrPointer import ray_cast_qr, get_qr_from_frame


def define_qr_pos(frame_pathes, pcd):
    found_qrs = {}
    found_counts = {}
    for path in frame_pathes:
        frame = Frame.from_json(path)
        if not frame.has_image:
            continue

        qrcodes = decode_image(frame.image_path)

        if len(qrcodes) < 1:
            continue

        for qrcode in qrcodes:
            qr_pos = get_qr_from_frame(qrcode, frame)

            (rc_pos, rc_dist, true_point) = ray_cast_qr(frame, qr_pos, pcd)

            if qrcode.value not in found_qrs.keys():
                found_qrs.setdefault(qrcode.value, true_point)
                found_counts.setdefault(qrcode.value, 1)
            else:
                found_counts[qrcode.value] += 1
                count = found_counts[qrcode.value]
                avr = found_qrs[qrcode.value]
                new_avr = (avr * (count - 1) + true_point) / count
                found_qrs[qrcode.value] = new_avr

    return found_qrs
