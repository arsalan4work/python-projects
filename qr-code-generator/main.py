import qrcode

def generate_qr_code(data, filename):
    
    #Generates a QR code from the given data and saves it as an image.
    try:
        # Ensure the filename has a .png extension
        if not filename.lower().endswith(".png"):
            filename += ".png"
        
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        
        image = qr.make_image(fill_color="black", back_color="white")
        image.save(filename)
        
        print(f"✅ QR code successfully saved as '{filename}'")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    data = input("🔗 Enter the text or URL: ").strip()
    filename = input("💾 Enter the filename (without extension for auto .png): ").strip()

    if data:
        generate_qr_code(data, filename)
    else:
        print("⚠️ No data provided. Exiting...")
