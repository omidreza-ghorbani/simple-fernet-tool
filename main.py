from encrypt import generate_key, encrypt_message, decrypt_message

def show_menu():
    print("\n====== Fernet Encryption Tool ======")
    print("1. Generate new key")
    print("2. Encrypt a message")
    print("3. Decrypt a message")
    print("4. Exit")
    print("====================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            key = generate_key()
            print(f"\nGenerated key: {key}\n\n")

        elif choice == '2':
            key = input("Enter your key: ").strip()
            message = input("Enter your message to encrypt: ").strip()
            try:
                encrypted = encrypt_message(key, message)
                print(f"\nEncrypted message: {encrypted}\n\n")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            key = input("Enter your key: ").strip()
            encrypted = input("Enter the encrypted message: ").strip()
            try:
                decrypted = decrypt_message(key, encrypted)
                print(f"\nDecrypted message: {decrypted}\n\n")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. try again.")

if __name__ == "__main__":
    main()
