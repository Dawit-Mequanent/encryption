from flask import Flask, jsonify, request
from Crypto.Cipher import AES
from encryption import *
from appdb import *
from ess import *
from flask_cors import CORS
from decryption import *
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import getpass

app = Flask(__name__)

CORS(app, resources={r"/encryption": {"origins": "http://localhost:5173"}})

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