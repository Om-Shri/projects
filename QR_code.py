import qrcode
from PIL import Image

data = input("Enter url here :")
file_name = input("enter file name:")

qr = qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(file_name)