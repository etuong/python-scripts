# A simple encryption technique

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char == " ":
            decrypted_message += " "
        else:
            decrypted_message += chr((ord(char) - key) % 256)
    print(f"Your decrypted message is: {decrypted_message}\n")
    return decrypted_message


def encrypt(plaintext, key):
    encrypted_message = ""
    for char in plaintext:
        if char == " ":
            encrypted_message += " "
        else:
            encrypted_message += chr((ord(char) + key) % 256)

    print(f"Your encrypted message is: {encrypted_message}\n")
    return encrypted_message


plaintext = "My name is Ethan UONG!"
key = 5
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(key))
encrypted_message = encrypt(plaintext, key)
decrypted_message = decrypt(encrypted_message, key)
