import cv2
from pyzbar.pyzbar import decode, ZBarSymbol


class QRCode:
    def __init__(self, value, pos, size):
        self.value = value
        self.pos = pos
        self.size = size


def decode_image(path: str):
    img = cv2.imread(path)
    value = decode(img, symbols=[ZBarSymbol.QRCODE])

    objs = []
    if value:
        for qrcode in value:
            x, y, w, h = qrcode.rect
            dec_inf = qrcode.data.decode('utf-8')
            objs.append(QRCode(dec_inf, [x, y], [w, h]))

    return objs

