import qrcode
from PIL import Image

def generate_qr_code(data, output_file, logo_path=None, color="black", background="white", box_size=10, border=4):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color=color, back_color=background)

    # If a logo path is provided, add the logo to the QR code
    if logo_path:
        logo = Image.open(logo_path)

        # Calculate logo size
        img_w, img_h = img.size
        logo_size = min(img_w, img_h) // 5
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Calculate position to paste the logo
        pos = ((img_w - logo_size) // 2, (img_h - logo_size) // 2)

        # Paste the logo on the QR code
        img = img.convert("RGBA")
        logo = logo.convert("RGBA")
        img.paste(logo, pos, logo)

    # Save the generated QR code to a file
    img.save(output_file)

def main():
    # Welcome
    print("Welcome to the QR Code Generator!")
    print("This program generates a QR code for the data you provide.")
    # Get user input
    data = input("Enter the data to encode in the QR code: ")
    output_file = input("Enter the output file name (e.g., 'qrcode.png'): ").strip()
    
    # Ensure output_file is not empty
    while not output_file:
        print("Output file name cannot be empty. Please provide a valid file name.")
        output_file = input("Enter the output file name (e.g., 'qrcode.png'): ").strip()

    logo_path = input("Enter the path to the logo image file (or leave empty if no logo): ").strip()
    color = input("Enter the color of the QR code (default 'black'): ").strip() or "black"
    background = input("Enter the background color of the QR code (default 'white'): ").strip() or "white"
    box_size = int(input("Enter the box size of the QR code (default 10): ").strip() or 10)
    border = int(input("Enter the border size of the QR code (default 4): ").strip() or 4)

    # Generate the QR code with the provided inputs
    generate_qr_code(data, output_file, logo_path if logo_path else None, color, background, box_size, border)
    print(f"QR code generated and saved to {output_file}")

if __name__ == "__main__":
    main()