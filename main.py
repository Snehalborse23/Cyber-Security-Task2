from PIL import Image

# Encrypt image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")  # ensure RGB format
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Add key value (use modulo 256 to keep values in range)
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    encrypted_path = "encrypted_image.png"
    img.save(encrypted_path)
    print(f"✅ Image encrypted successfully! Saved as {encrypted_path}")

# Decrypt image
def decrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Subtract key value (use modulo 256 to keep values in range)
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    decrypted_path = "decrypted_image.png"
    img.save(decrypted_path)
    print(f"✅ Image decrypted successfully! Saved as {decrypted_path}")

# Main menu
def main():
    print("=== Simple Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter choice (1 or 2): ")

    image_path = input("Enter image file path: ")
    key = int(input("Enter encryption key (integer): "))

    if choice == '1':
        encrypt_image(image_path, key)
    elif choice == '2':
        decrypt_image(image_path, key)
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
