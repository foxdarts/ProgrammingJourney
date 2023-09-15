import tkinter as tk
from tkinter import simpledialog, messagebox
from password_manager import PasswordManager

class UIManager:
    def __init__(self, password_manager):
        self.password_manager = password_manager

    def show_menu(self):
        self.root = tk.Tk()
        self.root.title("Password Manager")
        self.root.geometry("800x400")

        menu_frame = tk.Frame(self.root, padx=20, pady=20)
        menu_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        tk.Label(menu_frame, text="Password Manager", font=("Arial", 16)).pack(pady=10)

        existing_options = ["Add New Entry", "Get Entry", "Update Entry", "Delete Entry", "Generate New Database", "Copy to Clipboard"]
        for option in existing_options:
            tk.Button(menu_frame, text=option, command=lambda opt=option: self.handle_option(opt)).pack(pady=5)

        database_frame = tk.Frame(self.root, padx=20, pady=20)
        database_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

        tk.Label(database_frame, text="Database Entries").pack()
        self.listbox = tk.Listbox(database_frame, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.populate_listbox()
        self.root.mainloop()

    def handle_option(self, option):
        if option == "Add New Entry":
            self.add_new_entry()
        elif option == "Get Entry":
            self.get_entry()
        elif option == "Update Entry":
            self.update_entry()
        elif option == "Delete Entry":
            self.delete_entry()
        elif option == "Generate New Database":
            self.generate_new_database()
        elif option == "Copy to Clipboard":
            self.copy_to_clipboard()

    def generate_new_database(self):
        db_info = self.password_manager.load_db_info()
        if db_info:
            messagebox.showinfo("Database Info", "Database already linked to this master password.")
        else:
            self.password_manager.create_new_database()
            messagebox.showinfo("Success", "New database created and linked to this master password.")
            self.populate_listbox()

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        entries = self.password_manager.get_all_entries()
        for entry_type, entry_dict in entries.items():
            for name in entry_dict:
                self.listbox.insert(tk.END, f"{entry_type}: {name}")

    def add_new_entry(self):
        entry_types = ["Website", "App", "Email", "Notes"]
        entry_type = simpledialog.askstring("Entry Type", "Choose entry type:", 
                                            initialvalue=entry_types[0], 
                                            show=entry_types)
        if entry_type:
            name = simpledialog.askstring("Name", f"Enter the {entry_type} name:")
            if name:
                username = simpledialog.askstring("Username", f"Enter the {entry_type} username:")
                if username:
                    password = simpledialog.askstring("Password", f"Enter the {entry_type} password:")
                    if password:
                        self.password_manager.add_entry(entry_type, name, username, password)
                        self.populate_listbox()
                        self.show_message("Success", "Entry added successfully.")
                    else:
                        self.show_message("Error", "Password is required.")
                else:
                    self.show_message("Error", "Username is required.")
            else:
                self.show_message("Error", f"{entry_type} name is required.")
        else:
            self.show_message("Error", "Entry type not selected.")

    def update_entry(self):
        selected_item = self.listbox.get(tk.ACTIVE)
        if selected_item:
            entry_type, name = selected_item.split(": ")
            entry_info = self.password_manager.get_entries_by_type(entry_type).get(name)
            if entry_info:
                username = simpledialog.askstring("Username", "Enter the new username:", initialvalue=entry_info["username"])
                if username:
                    password = simpledialog.askstring("Password", "Enter the new password:", initialvalue=entry_info["password"])
                    if password:
                        self.password_manager.update_entry(entry_type, name, username, password)
                        self.populate_listbox()
                        self.show_message("Success", "Entry updated successfully.")
                    else:
                        self.show_message("Error", "Password is required.")
                else:
                    self.show_message("Error", "Username is required.")
            else:
                self.show_message("Error", "Invalid entry.")
        else:
            self.show_message("Error", "No entry selected.")

    def delete_entry(self):
        selected_item = self.listbox.get(tk.ACTIVE)
        if selected_item:
            entry_type, name = selected_item.split(": ")
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this entry?")
            if confirmation:
                if self.password_manager.delete_entry(entry_type, name):
                    self.populate_listbox()
                    self.show_message("Success", "Entry deleted successfully.")
                else:
                    self.show_message("Error", "Failed to delete entry.")
        else:
            self.show_message("Error", "No entry selected.")

    def copy_to_clipboard(self):
        selected_item = self.listbox.get(tk.ACTIVE)
        if selected_item:
            entry_type, name = selected_item.split(": ")
            entry_info = self.password_manager.get_entries_by_type(entry_type).get(name)
            if entry_info:
                password = entry_info["password"]
                if password:
                    self.password_manager.copy_to_clipboard(password)
                    self.show_message("Success", "Password copied to clipboard.")
                else:
                    self.show_message("Error", "No password available for this entry.")
            else:
                self.show_message("Error", "Invalid entry.")
        else:
            self.show_message("Error", "No entry selected.")

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

# Entry point for the application
if __name__ == "__main__":
    master_password = input("Enter your master password: ")
    if not master_password:
        print("Master password is required.")
    else:
        password_manager = PasswordManager(master_password)
        ui_manager = UIManager(password_manager)
        ui_manager.show_menu()
