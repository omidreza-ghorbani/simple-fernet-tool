from cryptography.fernet import Fernet

def generate_key():
    # Generate a new random encryption key
    key = Fernet.generate_key()
    return key.decode('utf-8')

def encrypt_message(key_str, message_str):
    # Encrypt a text message using the key
    fernet = Fernet(key_str.encode('utf-8'))
    encrypted = fernet.encrypt(message_str.encode('utf-8'))
    return encrypted.decode('utf-8')

def decrypt_message(key_str, encrypted_str):
    # Decrypt an encrypted message using the key
    fernet = Fernet(key_str.encode('utf-8'))
    decrypted = fernet.decrypt(encrypted_str)
    return decrypted.decode('utf-8')
