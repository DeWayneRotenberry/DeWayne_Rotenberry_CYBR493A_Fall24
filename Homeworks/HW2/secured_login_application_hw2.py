"""
DeWayne Rotenberry
10/14/2024
Homework #2
This implements a secure login system using a GUI. It encrypts usernames and passwords stored in a database to ensure secure authentication.
"""



# Required Libraries
import hashlib
import tkinter as tk
from tkinter import messagebox
from Homeworks.HW1.HW1 import DBConnector
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Database Connection

#Looked up on google simple encryption and decryption methods for python then looked up some hashlib python examples https://thepythoncode.com/article/hashing-functions-in-python-using-hashlib
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()




# Method to create users table in the database
def create_users_table(db):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS rotenberry_dewayne_hw2 (
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """
    db.query(create_table_query, '')


def insert_user(db, username, password):
    #hashes username and password
    hashed_username = hash_data(username)
    hashed_password = hash_data(password)


    insert_user_query = "INSERT INTO rotenberry_dewayne_hw2 (username, password) VALUES (%s, %s);"
    db.query(insert_user_query, (hashed_username, hashed_password))


# Method to authenticate user by checking decrypted username and password
def authenticate_user(db, username, password):
    # Query to fetch the encrypted username and password from the database
    fetch_user_query = "SELECT username, password FROM rotenberry_dewayne_hw2;"
    result = db.query(fetch_user_query, ())

    for row in result:
        stored_username = row[0]
        stored_password = row[1]

        if hash_data(username) == stored_username:

            return hash_data(password) == stored_password

    return False


# GUI for Login Screen
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


# Main Function
def main():
    # List of required packages
    required_packages = ['hashlib', 'Crypto', 'package3']

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            install(package)

    # Connect to the database
    db = DBConnector.MyDB()

    # Create the users table
    create_users_table(db)

    # Insert sample users (comment this out after running once to avoid duplicate users)
    #user_name = input("Give me a username to store in the database:")
    #password = input("Give me a password to store in the database:")
    #insert_user(db, user_name, password)

    # Launch the login screen
    create_login_screen(db)


if __name__ == "__main__":
    main()
