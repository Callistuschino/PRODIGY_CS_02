# PROGIDY_CS_02 

## 🔐PIXCRYPT - Pixel Encryption & Decryption Tool

Pixcrypt is a **pixel manipulation tool** written in Python that encrypts and decrypts images using multiple methods such as XOR, Add Key, Subtract Key, and Pixel Swapping.


## Features
- Encrypt/Decrypt images with different methods:
  - **XOR with key**
  - **Add key to pixel values**
  - **Subtract key from pixel values**
  - **Swap pixel values**
- Supports PNG, JPEG, and JPG formats.
- Prevents data overflow with safe NumPy operations.
- Interactive CLI with menus and error handling.
- Saves encrypted/decrypted images automatically.


## Requirements
Make sure you have the following installed:
- Python 3.x
- Pillow (`pip install pillow`)
- NumPy (`pip install numpy`)


## Clone the repository:

*git clone git@github.com:Callistuschino/PRODIGY_CS_02.git*

*cd PROGIDY_CS_02*


## Run the program:

*python3 pixcrypt.py*


Follow the menu to:

+ Encrypt an image

+ Decrypt an image

+ Exit program


## Example for encryption (XOR with key = 123):

Select an option:
1. Encrypt an Image
2. Decrypt an Image
3. Exit
Enter your choice (1/2/3): 1

Choose encryption method:
1. XOR with Key
2. Add Key
3. Subtract Key
4. Swap Pixels
Enter method (1/2/3/4): 1<br>
Enter a numeric key (0–255): 123

The encrypted image will be saved as:

*Abujaxor.png*


## Project Structure

PRODIGY_CS_02/
│── pixcrypt.py           # Main encryption/decryption script<br>
│── Abujaxor.png          # Example XOR encrypted image<br>
│── Abujakey.png          # Example Add key encrypted image<br>
│── Abujasubstract.png    # Example Subtract key encrypted image<br>
│── Abujaswap.png         # Example Swap pixel encrypted image<br>
│── abuja.jpeg            # Original test image


## Disclaimer
This project is for educational and demonstration purposes only.<br>
It should not be used for securing sensitive or production data.


## Author
Ozichukwu Callistus Nonso<br>
Cybersecurity Analyst & Ethical Hacker<br>
*GitHub: Callistuschino*
