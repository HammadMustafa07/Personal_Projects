# black and white themed Qr code generator

import qrcode as qr
img = qr.make("https://www.instagram.com/hammadabro_x/")
img.save("insta_qrcode.png")