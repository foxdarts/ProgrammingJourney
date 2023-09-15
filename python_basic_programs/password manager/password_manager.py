import json
from cryptography.fernet import Fernet
import base64
import os

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.fernet = Fernet(base64.urlsafe_b64encode(master_password.encode()))
        self.database = self.load_database()

    def load_database(self):
        try:
            with open("database.json", "rb") as file:
                encrypted_data = file.read()
                decrypted_data = self.decrypt_database(encrypted_data)
                return decrypted_data
        except FileNotFoundError:
            return {"entries": {}}

    def save_database(self):
        with open("database.json", "wb") as file:
            encrypted_data = self.encrypt_database(self.database)
            file.write(encrypted_data)

    def encrypt_database(self, data):
        encrypted_data = self.fernet.encrypt(json.dumps(data).encode())
        return encrypted_data

    def decrypt_database(self, encrypted_data):
        decrypted_data = self.fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    def encrypt_password(self, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        return encrypted_password.decode()

    def add_entry(self, entry_type, name, username, password):
        self.database.setdefault("entries", {}).setdefault(entry_type, {})
        entry = {
            "name": name,
            "username": username,
            "password": self.encrypt_password(password)
        }
        self.database["entries"][entry_type][name] = entry
        self.save_database()

    def get_all_entries(self):
        return self.database.get("entries", {})

    def update_entry(self, entry_type, name, username, password):
        entries = self.database.get("entries", {}).get(entry_type, {})
        if name in entries:
            entry = {
                "name": name,
                "username": username,
                "password": self.encrypt_password(password)
            }
            entries[name] = entry
            self.save_database()
            return True
        return False

    def delete_entry(self, entry_type, name):
        entries = self.database.get("entries", {}).get(entry_type, {})
        if name in entries:
            del entries[name]
            self.save_database()
            return True
        return False

    def load_db_info(self):
        try:
            with open("db_info.json", "rb") as file:
                encrypted_data = file.read()
                decrypted_data = self.decrypt_database(encrypted_data)
                return decrypted_data
        except FileNotFoundError:
            return None

    def save_db_info(self):
        db_info = {"master_password": self.master_password}
        with open("db_info.json", "wb") as file:
            encrypted_data = self.encrypt_database(db_info)
            file.write(encrypted_data)

    def create_new_database(self):
        self.save_database()
        self.save_db_info()

    def copy_to_clipboard(self, password):
        os.system("echo " + password.strip() + "| clip")

