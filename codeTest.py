import numpy as np

import cv2


font = cv2.FONT_HERSHEY_SIMPLEX


def read_qr(img):
    qrd = cv2.QRCodeDetector()
    retval, decoded_info, points, straight_qrcode = qrd.detectAndDecodeMulti(img)

    if retval:
        points = points.astype(np.int)

        for dec_inf, point in zip(decoded_info, points):
            if dec_inf == '':
                continue

            # QRコード座標取得
            x = point[0][0]
            y = point[0][1]

            # QRコードデータ
            print('dec:', dec_inf)
            img_bgr = cv2.putText(img, dec_inf, (x, y - 6), font, .3, (0, 0, 255), 1, cv2.LINE_AA)

            # バウンディングボックス
            img_bgr = cv2.polylines(img_bgr, [point], True, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('image', img)
    cv2.waitKey(0)


img_load = cv2.imread('resources/sample/IMG_2829.png', cv2.IMREAD_COLOR)
read_qr(img_load)

