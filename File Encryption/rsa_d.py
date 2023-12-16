def decrypt(msg2, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in msg2]
    return "".join(decrypted_message)

# Example usage
encrypted_file = input("Enter the file name to decrypt: ") # Replace with the actual encrypted message
file = open(encrypted_file, "r+")
encrypted_message = file.read()
d = int(input("Enter key to decrypt: "))
n = int(input("Enter modulo to decrypt: "))
msg = encrypted_message.split(",")
file.close()
msg2 = []
for i in msg:
    msg2.append(int(i))
private_key = (d, n)  # Replace with the actual private key
decrypted_message = decrypt(msg2, private_key)
file_out = open(encrypted_file, "w+")
file_out.write(decrypted_message)
print("Decrypted Message:", decrypted_message)
file_out.close()
