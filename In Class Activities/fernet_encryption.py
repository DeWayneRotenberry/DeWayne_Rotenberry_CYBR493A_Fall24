from cryptography.fernet import Fernet

# Step 1: Generate a key (keep this secure!)
key = Fernet.generate_key()

# Step 2: Create a cipher object using the generated key
cipher_suite = Fernet(key)

# Step 3: Save the key securely to a file for later use in decryption
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Step 4: Encrypt a message
text_to_encrypt = "This is a secret message."
text_bytes = text_to_encrypt.encode()  # Convert the string to bytes
encrypted_text = cipher_suite.encrypt(text_bytes)  # Encrypt the message

# Step 5: Save the encrypted text to a file to avoid copy-paste issues
with open('encrypted_data.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_text)

print("Encryption successful. Encrypted text saved to file.")
