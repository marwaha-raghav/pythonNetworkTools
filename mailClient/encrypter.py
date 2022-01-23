# Steps:
# Import Fernet
# Then generate an encryption key, that can be used for encryption and decryption.
# Convert the string to byte string, so that it can be encrypted.
# Instance the Fernet class with the encryption key.
# Then encrypt the string with Fernet instance.
# Then it can be decrypted with Fernet class instance and it should be instanced with the same key used for encryption.

from cryptography import fernet
from pathlib import Path

from fernet import Fernet


class CryptoEngine:
    key = Fernet.generate_key()

    def __init__(self, password):
        self.secret = password
        # Using fernet to generate symmetrical encryption key

    def encrypt_message(self):
        """
        This function is part of the CryptoEngine and is responsible for encrypting the secrets from the file
        :return:
        """
        print("Print context", __name__)
        # instance of fernet class with key
        encryption_engine = Fernet(self.key)
        # password is encoded to a byte string and encrypted
        encrypted_message = encryption_engine.encrypt(self.secret.encode())
        # Write secret to a file
        with open(Path("password.txt"), 'wb') as f:
            f.write(encrypted_message)

    @staticmethod
    def decrypt_message():
        """
               This function is part of the CryptoEngine and is responsible for decrypting the secrets from the file
               :return:
        """
        with open('password.txt', 'rb') as f:
            read_secret = f.read()
            decryption_engine = Fernet(CryptoEngine.key)
            decrypted_message = decryption_engine.decrypt(read_secret)
            return decrypted_message.decode()



