from encryption_utils import *

def main():
    print("🔐 Welcome to CipherX")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            encrypt_message()
        elif choice == '2':
            decrypt_message()
        elif choice == '3':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
