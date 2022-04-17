import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


#text encode
qr = pyqrcode.create("benjamin")
qr.png("qr.png", scale=8)


d = decode(Image.open("qr.png"))
print(d)
