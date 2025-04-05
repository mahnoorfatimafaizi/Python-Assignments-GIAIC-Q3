import qrcode
from PIL import Image
from pyzbar.pyzbar import decode


def create_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

def decode_qr_code(filename):
    img = Image.open(filename)
    decoded_objects = decode(img)
    if decoded_objects:
        for obj in decoded_objects:
            print("Decoded data:", obj.data.decode("utf-8"))
    else:
        print("No QR code found in the image.")


if __name__ == "__main__":

    data_to_encode = "Hello, this is a test QR code!🥴😊 "
    output_file = "my_qr_code.png"
    create_qr_code(data_to_encode, output_file)

    # Example: Decode the QR code
    decode_qr_code(output_file)