import qrcode as qr

code = qr.make("hello world")
code.save("code.png")
code.show()