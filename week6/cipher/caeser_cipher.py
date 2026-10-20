def encrypt(data, shift=-1) -> str:
    encrypted_data = ''

    for i in data:
        encrypted_data += chr(ord(i) + shift)

    return encrypted_data

def decrypt(data, shift=-1) -> str:
    decrypted_data = ''
    
    for i in data:
        decrypted_data += chr(ord(i) - shift)

    return decrypted_data
