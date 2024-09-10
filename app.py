import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer
from PIL import Image, ImageDraw

def create_qr_with_smaller_logo(url, logo_path, output_path, qr_color="#000000", bg_color="#FFFFFF", box_size=10, border=4):
    # Create QR code
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR code image
    qr_image = qr.make_image(fill_color=qr_color, back_color=bg_color, 
                             image_factory=StyledPilImage, 
                             module_drawer=SquareModuleDrawer())

    # Print QR code size
    print(f"QR code size: {qr_image.size[0]}x{qr_image.size[1]} pixels")

    # Convert to PIL image
    qr_image = qr_image.convert("RGBA")

    # Calculate the size of the logo (approximately 1/4 of the QR code size)
    logo_size = qr_image.size[0] // 4
    print(f"Logo size: {logo_size}x{logo_size} pixels")

    # Create a white square for the logo background
    background_size = logo_size + 20  # Add some padding around the logo
    print(f"Logo background size: {background_size}x{background_size} pixels")
    background = Image.new('RGBA', (background_size, background_size), (255, 255, 255, 255))

    # Open and resize the logo
    logo = Image.open(logo_path).convert("RGBA")
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Paste the logo onto the white background
    background_center = (background_size - logo_size) // 2
    background.paste(logo, (background_center, background_center), logo)

    # Calculate position to paste the logo (centered)
    qr_center = qr_image.size[0] // 2
    paste_position = (qr_center - background_size // 2, qr_center - background_size // 2)

    # Paste the logo with white background onto the QR code
    qr_image.paste(background, paste_position, background)

    # Save the result
    qr_image.save(output_path)
    print(f"QR code with smaller logo generated and saved as '{output_path}'")

# Usage
url = "https://master--kingflexcode.netlify.app/"
logo_path = "/Users/yuntungshih/Desktop/kingflex_logo.png"  # Replace with the actual logo path
output_path = "qr_code_with_smaller_logo.png"

create_qr_with_smaller_logo(url, logo_path, output_path)