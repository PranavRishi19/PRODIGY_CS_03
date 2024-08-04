from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    pixels = np.array(image)
    
    # Apply basic mathematical operation and swap pixels
    encrypted_pixels = (pixels + key) % 256
    
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(image_path)
    encrypted_pixels = np.array(encrypted_image)
    
    # Reverse the basic mathematical operation and swap pixels
    decrypted_pixels = (encrypted_pixels - key) % 256
    
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? Enter E or D (or Q to quit): ").upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            image_path = input("Enter the path to the image: ")
            output_path = input("Enter the path for the output image: ")
            try:
                key = int(input("Enter the encryption key (integer): "))
                if choice == 'E':
                    encrypt_image(image_path, output_path, key)
                elif choice == 'D':
                    decrypt_image(image_path, output_path, key)
            except ValueError:
                print("Invalid input. Please enter an integer for the encryption key.")
        else:
            print("Invalid choice. Please enter E, D, or Q.")

if __name__ == "__main__":
    main()
