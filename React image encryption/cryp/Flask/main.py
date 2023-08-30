from flask import Flask, jsonify
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


@app.route('/encryption', methods=['POST'])
def encryption_route():
    password = getpass.getpass('Please insert your password: ')
    key = password.encode('UTF-8')
    key = pad(key, AES.block_size)

    file = request.files['file']
    file_name = file.filename

    encrypted_image_data = encrypt(file_name, key)

    return jsonify({'encryptedImage': encrypted_image_data})

@app.route('/decryption', methods=['POST'])
def decryption_route():
    password = getpass.getpass('Please insert your password: ')
    key = password.encode('UTF-8')
    key = pad(key, AES.block_size)

    file = request.files['file']
    file_name = file.filename

    decrypt(file_name, key)

    return 'Decryption successful!'




if __name__ == '__main__':
    app.run()

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




