from cryptography.fernet import Fernet
from decouple import config

class EncryptionManager:

    def __init__(self) -> None:
        secret_key = config("CRYPTO_KEY")
        secret_key = secret_key + "="
        self.fernet = Fernet(secret_key.encode())

    def encrypt_data(self, data):
        encrypted_data = self.fernet.encrypt(data.encode('utf-8'))
        return encrypted_data

    def decrypt_data(self, data):
        decrypted_data = self.fernet.decrypt(data).decode('utf-8')
        return decrypted_data