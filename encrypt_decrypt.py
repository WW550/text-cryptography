from cryptography.fernet import Fernet

def generate_key():
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key.")

def load_key():
    """Loads the encryption key from a file."""
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Error: Key file not found. Generate a key first using the script.")
        return None

def encrypt_text(text, key):
    """Encrypts the given text using the provided key."""
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    """Decrypts the given encrypted text using the provided key."""
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

def main():
    print("Options:\n1. Generate Key\n2. Encrypt Text\n3. Decrypt Text\n4. Exit")
    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            generate_key()
        elif choice == "2":
            key = load_key()
            if key:
                text = input("Enter text to encrypt: ")
                encrypted_text = encrypt_text(text, key)
                print(f"Encrypted Text: {encrypted_text.decode()}")
        elif choice == "3":
            key = load_key()
            if key:
                encrypted_text = input("Enter text to decrypt: ").encode()
                try:
                    decrypted_text = decrypt_text(encrypted_text, key)
                    print(f"Decrypted Text: {decrypted_text}")
                except Exception as e:
                    print(f"Decryption failed: {e}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
