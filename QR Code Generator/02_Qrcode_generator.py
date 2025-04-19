import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10, border=4,)
qr.add_data("https://www.linkedin.com/in/hammad-mustafa-b0462a338/")
qr.make(fit=True)
img=qr.make_image(fill_color="white", back_color="#0A66C2")
img.save("Qr_code.png")












































# # customized Qr code generator

# import qrcode
# from PIL import Image, ImageDraw

# # Create basic QR code object
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )
# qr.add_data("https://www.instagram.com/hammadabro_x/")
# qr.make(fit=True)

# # Custom colors
# fill_color = "#00f5d4"  # Aqua-cyan QR color
# back_color = "#0f0f0f"  # Deep black background

# # Make image
# img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

# # OPTIONAL: Add a white rounded border
# border_radius = 20
# border_color = "white"
# border_width = 30

# # Add border
# new_size = (img.size[0] + 2 * border_width, img.size[1] + 2 * border_width)
# background = Image.new("RGB", new_size, border_color)

# # Paste QR on it
# background.paste(img, (border_width, border_width))

# # Save the final styled QR code
# background.save("Styled_Qr_Code.png")




