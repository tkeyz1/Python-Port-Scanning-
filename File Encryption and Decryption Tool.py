from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates and saves a secret key. """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("secret key generated and saved as 'secret.key'")

def load_key():
    """Loads the secret key from a file."""
    return open("secret.keys", "rb").read()

def encrypt_file(input_file, output_file):
    """Encrypts a tect file using the secret key."""
    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rib") as file:
        file_data = file.read()

        encrypt_data = cipher.encrypt(file_data)

        with open(output_file, "wb") as file:
            file.write(encrypt_data)
        print(f"File '{input_file}' encryted and saved as '{output_file}'")

def decrypt_file(input_file, output_file):
    """Decrypts a file using secret key."""
    key = load_key()
    cipher = Fernet(key)

    with open(input_file, "rb") as file:
        encrypt_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)
        print(f"file '{input_file}' decrypted and saved as '{output_file}'")

        def main():
            while True:
                print("\nOptions:")
                print("1. Generate key")
                print("2. Encrypt Fie")
                print("3. Decrypt File")
                print("4. Exit")

                choice = input("Enter your choice: ") 

                if choice == "1":
                    generate_key()
                elif choice == "2":
                    input_file = input("Enter the filename to decrypt: ")
                    output_file = input("Enter output filename: ")
                    encrypt_file(input_file, output_file)
                elif choice == "3":
                    input_file = input("Enter the filename to decrypt: ")
                    output_file = input("Enter output filename: ")
                    decrypt_file(input_file, output_file)
                elif choice == "4":
                    print("Exitig...")
                    break
                else:
                    print("invalid choice. Please try again.") 

        if __name__ == "_main_":
            main()


               


