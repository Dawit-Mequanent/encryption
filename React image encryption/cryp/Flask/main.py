from flask import Flask
from Crypto.Cipher import AES
from encryption import *
from appdb import *
from ess import *
from decryption import *
from Crypto.Util.Padding import pad
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import getpass



app = Flask(__name__)


@app.route('/encryption')
def encryption():
    key = input ('please insert your password:')
    key = key.encode('UTF-8')
    key = pad(key,AES.block_size)

def encrypt (file_name,key):
        with open (file_name,'rb') as entry:
            data = entry.read()
            cipher = AES.new(key, AES.MODE_ECB)
            ciphertext = cipher.encrypt(pad(data,AES.block_size))
            iv = b64encode(cipher.iv).decode('UTF-8')
            ciphertext = b64encode(ciphertext).decode('UTF-8')
            to_write = iv + ciphertext

        entry.close()
        with open(file_name+'.enc','w') as data:    
           data.write(to_write)
        data.close()

        encrypt('image.jpg', key)   


@app.route('/decryption')
def decryption():

    password = getpass.getpass('Enter password to Decrypt: ')
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
            cipher = AES.new(key,AES.MODE_ECB,iv)
            decrypted = cipher.decrypt(ciphertext)
            decrypted = unpad(decrypted,AES.block_size)
            with open('wow.jpg','wb') as data:
               data.write(decrypted)
            data.close()
        except(ValueError,KeyError):
            print('wrong password')

    def pad(entry):
            padded = entry+(16-len(entry)%16)*'['
            return(padded)

    plain_text ='Made in Ethiopia'
    plain_text = pad(plain_text)
    plain_text=plain_text.encode('UTF-8')

    key = '12345'
    key = pad(key)
    key = key.encode('UTF-8')

    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plain_text)
    print(ciphertext)

    cipher = AES.new(key, AES.MODE_ECB)
    data = cipher.decrypt(ciphertext)

    data= data.decode('UTF-8')
    unpad = data.find('[')
    data = data[:unpad]
    print('decode text = ', data)





if __name__ == '__main__':
    app.run()