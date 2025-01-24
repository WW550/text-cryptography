import tkinter as tk
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet

# Functions for encryption and decryption
def generate_key():
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "Key generated and saved to secret.key.")

def load_key():
    """Loads the encryption key from a file."""
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found. Generate a key first.")
        return None

def encrypt_text():
    key = load_key()
    if key:
        text = text_input.get("1.0", tk.END).strip()
        if text:
            fernet = Fernet(key)
            encrypted_text = fernet.encrypt(text.encode()).decode()
            output_text.delete("1.0", tk.END)
            output_text.insert("1.0", encrypted_text)
            messagebox.showinfo("Success", "Text encrypted successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter text to encrypt.")

def decrypt_text():
    key = load_key()
    if key:
        encrypted_text = text_input.get("1.0", tk.END).strip()
        if encrypted_text:
            try:
                fernet = Fernet(key)
                decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
                output_text.delete("1.0", tk.END)
                output_text.insert("1.0", decrypted_text)
                messagebox.showinfo("Success", "Text decrypted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter text to decrypt.")

# Create the main window
root = tk.Tk()
root.title("Encrypt/Decrypt GUI")
root.geometry("500x400")

# Add widgets
key_button = tk.Button(root, text="Generate Key", command=generate_key)
key_button.pack(pady=10)

tk.Label(root, text="Input Text:").pack()
text_input = tk.Text(root, height=5, width=50)
text_input.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt Text", command=encrypt_text)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt Text", command=decrypt_text)
decrypt_button.pack(pady=5)

output_label = tk.Label(root, text="Output:")
output_label.pack()
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

# Run the main loop
root.mainloop()
