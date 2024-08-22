import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from PIL import Image, ImageDraw

def create_qr_with_centered_logo(url, logo_path, output_path, qr_color="black", bg_color="white", box_size=10, border=4):
    # Create QR code
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=box_size, border=border)
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR code image with rounded corners
    qr_image = qr.make_image(fill_color=qr_color, back_color=bg_color, 
                             image_factory=StyledPilImage, 
                             module_drawer=RoundedModuleDrawer())

    # Convert to PIL image
    qr_image = qr_image.convert("RGBA")

    # Calculate the size of the center area (approximately 1/4 of the QR code size)
    center_size = qr_image.size[0] // 4

    # Create a white rectangle mask
    mask = Image.new('RGBA', qr_image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(mask)
    center_pos = ((qr_image.size[0] - center_size) // 2,
                  (qr_image.size[1] - center_size) // 2)
    draw.rectangle([center_pos, (center_pos[0] + center_size, center_pos[1] + center_size)], 
                   fill=(255, 255, 255, 255))

    # Apply the mask to the QR code
    qr_image = Image.alpha_composite(qr_image, mask)

    # Open the logo image
    logo = Image.open(logo_path)

    # Resize the logo to fit the center area
    logo = logo.resize((center_size, center_size))

    # Paste the logo to the QR code center
    qr_image.paste(logo, center_pos, logo)

    # Save the result
    qr_image.save(output_path)
    print(f"QR code generated and saved as '{output_path}'")


url = "https://master--kingflexcode.netlify.app/"
logo_path = "/Users/yuntungshih/Desktop/KingFlex Work/KING_FLEX_Horizontal.png"  # 請替換為實際的logo路徑
output_path = "qr_code_with_centered_logo.png"

create_qr_with_centered_logo(url, logo_path, output_path)