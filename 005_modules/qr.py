import qrcode

data = "Hello Foram 👋"

qr = qrcode.QRCode(
    version=1,  # controls size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box
    border=4  # thickness of border
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("custom_qr.png")

print("Custom QR Code created!")