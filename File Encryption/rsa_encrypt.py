
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Example usage
file_name = input("Enter the file name: ")
file = open(file_name,"r+")
message = file.read()
e = int(input("Enter key to encrypt: "))
n = int(input("Enter modulo to encrypt: "))
public_key = (e, n)  # Replace with the actual public key
encrypted_message = encrypt(message, public_key)
file.close()
msg = ""
for i in encrypted_message:
    msg = msg+str(i)+","
msg = msg[:-1]
file_out = open(file_name, "w+")
file_out.write(msg)
file_out.close()
