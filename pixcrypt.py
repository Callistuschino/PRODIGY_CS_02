import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np
def get_numeric_key():
    while True:
        try:
            key = int(input("Enter a numeric key (0–255): "))
            if 0 <= key <= 255:
                return key
            else:
                print("⚠️ Invalid input! Please enter a number between 0 and 255.")
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

# Fancy Banner
def banner():
    print(r"""
██████╗ ██╗██╗  ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
██╔══██╗██║╚██╗██╔╝██╔════╝██╔══██╗██║   ██║██╔══██╗╚══██╔══╝
██████╔╝██║ ╚███╔╝ ██║     ██████╔╝██║   ██║██████╔╝   ██║   
██╔═══╝ ██║ ██╔██╗ ██║     ██╔═══╝ ██║   ██║██╔═══╝    ██║   
██║     ██║██╔╝ ██╗╚██████╗██║     ╚██████╔╝██║        ██║   
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝      ╚═════╝ ╚═╝        ╚═╝   
  🔐 Welcome to PIXCRYPT - Simple Image Encryption Tool 🔐
    """)


# Encryption with different operations
def encrypt_image(image_path, method="xor", key=50):
    img = Image.open(image_path)
    arr = np.array(img)

    if method == "xor":
        encrypted_arr = arr ^ key
    elif method == "add":
        encrypted_arr = ((arr.astype(np.int16) + key) % 256).astype(np.uint8)
    elif method == "subtract":
        encrypted_arr = ((arr.astype(np.int16) - key) % 256).astype(np.uint8)
    elif method == "swap":
        encrypted_arr = np.flipud(arr)   # swap rows (can also do np.fliplr for columns)
    else:
        print("[-] Unknown method. Defaulting to XOR.")
        encrypted_arr = arr ^ key

    encrypted_img = Image.fromarray(np.uint8(encrypted_arr))
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if save_path:
        encrypted_img.save(save_path)
        print(f"[+] Image encrypted using '{method}' and saved as {save_path}")


# Decryption with corresponding operations
def decrypt_image(image_path, method="xor", key=50):
    img = Image.open(image_path)
    arr = np.array(img)

    if method == "xor":
        decrypted_arr = arr ^ key
    elif method == "add":
        decrypted_arr = ((arr.astype(np.int16) - key) % 256).astype(np.uint8)
    elif method == "subtract":
        decrypted_arr = ((arr.astype(np.int16) + key) % 256).astype(np.uint8)
    elif method == "swap":
        decrypted_arr = np.flipud(arr)   # flipping again restores original
    else:
        print("[-] Unknown method. Defaulting to XOR.")
        decrypted_arr = arr ^ key

    decrypted_img = Image.fromarray(np.uint8(decrypted_arr))
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )
    if save_path:
        decrypted_img.save(save_path)
        print(f"[+] Image decrypted using '{method}' and saved as {save_path}")


# Main menu
def main():
    while True:
        print("\nSelect an option:")
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            file_path = filedialog.askopenfilename(
                title="Select an image to encrypt",
                filetypes=[
                    ("All Supported Images", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp;*.PNG;*.JPG;*.JPEG;*.BMP;*.GIF;*.TIFF;*.WEBP"),
                    ("All Files", "*.*")
                ]
            )
            if not file_path:
                print("⚠️ No file selected. Returning to menu.")
                continue

            while True:
                print("\nChoose encryption/decryption method:")
                print("1. XOR with Key")
                print("2. Add Key")
                print("3. Subtract Key")
                print("4. Swap Pixels")

                method_choice = input("Enter method (1/2/3/4): ").strip()
                methods = {"1": "xor", "2": "add", "3": "subtract", "4": "swap"}

                if method_choice not in methods:
                    print("⚠️ Invalid choice. Try again.")
                    continue

                method = methods[method_choice]

                try:
                    if method in ["xor", "add", "subtract"]:
                        key = get_numeric_key()
                        encrypt_image(file_path, method, key)
                    else:
                        encrypt_image(file_path, method)
                except Exception as e:
                    print(f"⚠️ Error: {e}. Try again.")
                    continue

                break  # go back to main menu after success

        elif choice == "2":
            file_path = filedialog.askopenfilename(
                title="Select an image to decrypt",
                filetypes=[
                    ("All Supported Images", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff;*.webp;*.PNG;*.JPG;*.JPEG;*.BMP;*.GIF;*.TIFF;*.WEBP"),
                    ("All Files", "*.*")
                ]
            )
            if not file_path:
                print("⚠️ No file selected. Returning to menu.")
                continue

            while True:
                print("\nChoose encryption/decryption method:")
                print("1. XOR with Key")
                print("2. Add Key")
                print("3. Subtract Key")
                print("4. Swap Pixels")

                method_choice = input("Enter method (1/2/3/4): ").strip()
                methods = {"1": "xor", "2": "add", "3": "subtract", "4": "swap"}

                if method_choice not in methods:
                    print("⚠️ Invalid choice. Try again.")
                    continue

                method = methods[method_choice]

                try:
                    if method in ["xor", "add", "subtract"]:
                        key = get_numeric_key()
                        decrypt_image(file_path, method, key)
                    else:
                        decrypt_image(file_path, method)
                except Exception as e:
                    print(f"⚠️ Error: {e}. Try again.")
                    continue

                break  # go back to main menu after success

        elif choice == "3":
            print("👋 Exiting PIXCRYPT. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")
            continue

if __name__ == "__main__":
    banner()
    main()
    
