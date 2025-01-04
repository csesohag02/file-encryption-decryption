"""
Created on Sat Jan  4 13:23:02 2025
Author: @csesohag02
GitHub: https://github.com/csesohag02
"""


from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate and save a key for encryption/decryption."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'key.key'.")

def load_key():
    """Load the encryption/decryption key from a file."""
    if not os.path.exists("key.key"):
        raise FileNotFoundError("Key file not found. Please generate a key first.")
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file, output_file):
    """Encrypt the content of a text file."""
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{input_file}' encrypted and saved as '{output_file}'.")

def decrypt_file(input_file, output_file):
    """Decrypt the content of a text file."""
    key = load_key()
    fernet = Fernet(key)

    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"File '{input_file}' decrypted and saved as '{output_file}'.")

def main():
    print("File Encryption/Decryption Tool")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            input_file = input("Enter the file to encrypt: ")
            output_file = input("Enter the output file name: ")
            encrypt_file(input_file, output_file)
        elif choice == "3":
            input_file = input("Enter the file to decrypt: ")
            output_file = input("Enter the output file name: ")
            decrypt_file(input_file, output_file)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


"""
Created and maintained by @csesohag02
GitHub: https://github.com/csesohag02
"""
