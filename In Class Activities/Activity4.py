# Required Libraries
import psycopg2
# from Demos.win32ts_logoff_disconnected import username
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import os
import DBConnector

# Database Connection

# Function to generate and store the Fernet key
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

# Function to load the Fernet key from a file
def load_key():
    return open("secret.key", "rb").read()

# encrypt username
def encrypt_username(username):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(username.encode())

def decrypt_username(encrypted_username):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_username).decode()

# Function to encrypt data
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

# Function to decrypt data
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()


# Method to create users table in the database
def create_users_table(db):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rotenberry_dewayne_activity4 (
        
        username VARCHAR NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """
    db.query(create_table_query,'')

def insert_user(db, username, password):
    encrypted_username = encrypt_username(username)
    encrypted_password = encrypt_password(password)

    # Ensure the encrypted password is stored as a string
    encrypted_username_str = encrypted_username.decode('utf-8')
    encrypted_password_str = encrypted_password.decode('utf-8')

    insert_user_query = "INSERT INTO rotenberry_dewayne_activity4 (username, password) VALUES (%s, %s);"
    db.query(insert_user_query, (encrypted_username_str, encrypted_password_str))

# Method to authenticate user by checking decrypted password
def authenticate_user(db, username, password):
    fetch_user_query = "SELECT password FROM rotenberry_dewayne_activity4 WHERE username = %s;"
    result = db.query(fetch_user_query, (username,))
    if result:
        #stored_encrypted_username = result[0][0]
        stored_encrypted_password = result[0][0]

        #decrypted_username = decrypt_username(stored_encrypted_username)
        decrypted_password = decrypt_password(stored_encrypted_password)
        return decrypted_password == password
    return False

# GUI for Login Screen DO NOT CHANGE FOR HW2
def create_login_screen(db):
    def attempt_login():
        username = entry_username.get()
        password = entry_password.get()
        if authenticate_user(db, username, password):
            messagebox.showinfo("Login Success", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    root = tk.Tk()
    root.title("Secure Login Screen")

    label_username = tk.Label(root, text="Username")
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)

    label_password = tk.Label(root, text="Password")
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    login_button = tk.Button(root, text="Login", command=attempt_login)
    login_button.grid(row=2, columnspan=2)

    root.mainloop()

# Main Function DO NOT CHANGE FOR HW2
def main():
    # Generate key if it does not exist
    generate_key()

    # Connect to the database
    db = DBConnector.MyDB()

    # Create the users table
    create_users_table(db)

    # Insert sample users (comment this out after running once to avoid duplicate users)
   # user_name = input("Give me a username to store in the database:")
   # password = input("Give me a password to store in the database:")
  #  insert_user(db, user_name, password)

    # Launch the login screen
    create_login_screen(db)

if __name__ == "__main__":
    main()
