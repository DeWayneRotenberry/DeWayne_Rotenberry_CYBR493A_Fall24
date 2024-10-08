from cryptography.fernet import Fernet

# Step 1: Load the previously saved key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

# Step 2: Create a cipher object using the same key
cipher_suite = Fernet(key)

# Step 3: Load the encrypted text from a file (this avoids base64 issues caused by manual input)
with open('encrypted_data.txt', 'rb') as encrypted_file:
    encrypted_text = encrypted_file.read()

# Step 4: Decrypt the encrypted text
try:
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    decrypted_message = decrypted_text.decode()  # Convert from bytes to string
    print("Decryption successful. Decrypted text:", decrypted_message)
except cryptography.fernet.InvalidToken:
    print("Decryption failed: The key or the encrypted data is invalid.")
