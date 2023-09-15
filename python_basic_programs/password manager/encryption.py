from cryptography.fernet import Fernet
import base64
import hashlib
import os

def generate_encryption_key(master_password):
    salt = os.urandom(16)
    key = base64.urlsafe_b64encode(hashlib.pbkdf2_hmac('sha256', master_password.encode('utf-8'), salt, 100000))
    return key, salt

def encrypt(data, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode())
    return cipher_text

def decrypt(encrypted_data, key):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(encrypted_data).decode()
    return plain_text
