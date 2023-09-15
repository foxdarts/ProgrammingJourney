from ui import UIManager
from password_manager import PasswordManager

def main():
    ui_manager = UIManager()
    master_password = ui_manager.get_master_password()

    if not master_password:
        messagebox.showinfo("Error", "Master password is required.")
        return

    password_manager = PasswordManager(master_password)
    ui_manager = UIManager(password_manager)
    ui_manager.show_menu()

if __name__ == "__main__":
    main()

