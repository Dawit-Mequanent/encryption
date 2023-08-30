from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from base64 import b64decode
from Crypto.Util.Padding import pad

def decrypt(file_name, key):
    with open(file_name, 'r') as entry:
        encrypted_data = entry.read()

    iv = b64decode(encrypted_data[:24])
    ciphertext = b64decode(encrypted_data[24:])
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    try:
        decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

        original_file_name = file_name[:-4]  # Remove the '.enc' extension from the file name
        with open(original_file_name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print('Decryption successful!')
    except ValueError:
        print('Incorrect password. Decryption failed.')

password = input('Please insert your password to Decrypt: ')
key = password.encode('UTF-8')
key = pad(key, AES.block_size)

file_name = input('Please enter the encrypted file name: ')
decrypt(file_name, key)



