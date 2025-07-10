import base64
from cryptography.fernet import Fernet

# Caesar Cipher
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Base64
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()

# Reverse
def reverse_cipher(text):
    return text[::-1]

# AES Encryption with Fernet
def generate_key():
    return Fernet.generate_key()

def aes_encrypt(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode()).decode()

def aes_decrypt(encrypted_text, key):
    f = Fernet(key)
    return f.decrypt(encrypted_text.encode()).decode()

# Encrypt Menu
def encrypt_message():
    print("\nChoose encryption method:")
    print("1. Caesar Cipher")
    print("2. Base64 Encoding")
    print("3. Reverse Cipher")
    print("4. AES Encryption (with key)")

    choice = input("Enter choice (1-4): ")
    message = input("Enter your message: ")

    if choice == '1':
        shift = int(input("Enter Caesar shift (e.g., 3): "))
        print("🔐 Encrypted:", caesar_cipher_encrypt(message, shift))

    elif choice == '2':
        print("🔐 Encrypted:", base64_encode(message))

    elif choice == '3':
        print("🔐 Encrypted:", reverse_cipher(message))

    elif choice == '4':
        key = generate_key()
        encrypted = aes_encrypt(message, key)
        print("🔐 Encrypted:", encrypted)
        print("🔑 Save this key to decrypt: ", key.decode())

    else:
        print("❌ Invalid choice.")

# Decrypt Menu
def decrypt_message():
    print("\nChoose decryption method:")
    print("1. Caesar Cipher")
    print("2. Base64 Decoding")
    print("3. Reverse Cipher")
    print("4. AES Decryption (with key)")

    choice = input("Enter choice (1-4): ")
    message = input("Enter encrypted message: ")

    if choice == '1':
        shift = int(input("Enter Caesar shift (e.g., 3): "))
        print("🔓 Decrypted:", caesar_cipher_decrypt(message, shift))

    elif choice == '2':
        print("🔓 Decrypted:", base64_decode(message))

    elif choice == '3':
        print("🔓 Decrypted:", reverse_cipher(message))

    elif choice == '4':
        key = input("Enter secret key: ").encode()
        try:
            print("🔓 Decrypted:", aes_decrypt(message, key))
        except:
            print("❌ Invalid key or message.")

    else:
        print("❌ Invalid choice.")
