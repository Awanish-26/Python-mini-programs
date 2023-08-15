import qrcode

def generate_qrcode(text):

    qr =qrcode.QRCode(
        version = 1 ,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10 ,
        border = 2 ,
    )

    qr.add_data(text)
    qr.make_image(fit=True)
    img = qr.make_image(fill_color = "black" , back_color = "white")
    img.save("qrimg01.png")

__name__
url =input("Enter disired url :")
generate_qrcode(url)
print("Successfully Created")