from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass

password = getpass.getpass('Enter password: ')
print('You entered:', password)
key = password.encode('UTF')
key = pad(key,AES.block_size)

with open ('image.jpg.enc','+r') as entry:
    try:
        data = entry.read()
        length = len(data)
        iv = data[:24]
        iv = b64decode(iv)
        ciphertext = data[24:length]
        ciphertext = b64decode(ciphertext)
        cipher = AES.new(key,AES.MODE_CFB,iv)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted,AES.block_size)
        with open('wow.jpg','wb') as data:
            data.write(decrypted)
        data.close()
    except(ValueError,KeyError):
        print('wrong password')



