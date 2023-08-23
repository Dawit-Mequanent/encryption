from flask import Flask, request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import hashlib

app = Flask(__name__)

# Preset password (for demonstration purposes)
# In a real application, the hashed password would be stored securely and not in plain text
hashed_password = hashlib.sha256("password".encode()).hexdigest()

def check_password(input_password):
    hashed_input = hashlib.sha256(input_password.encode()).hexdigest()
    return hashed_password == hashed_input

@app.route('/decryption', methods=['POST'])
def decryption():
    encrypted_data = request.form['data']
    password = request.form['password']

    if check_password(password):
        key = password.encode('UTF-8')
        key = pad(key, AES.block_size)

        try:
            data = b64decode(encrypted_data)
            length = len(data)
            iv = data[:16]
            ciphertext = data[16:length]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = cipher.decrypt(ciphertext)
            decrypted = unpad(decrypted, AES.block_size)
            with open('decrypted_data.txt', 'wb') as file:
                file.write(decrypted)
            return "Decryption successful."
        except ValueError:
            return "Decryption failed. Wrong password."
    else:
        return "Decryption failed. Incorrect password."

@app.route('/encryption', methods=['POST'])
def encryption():
    data = request.form['data']
    password = request.form['password']

    if check_password(password):
        key = password.encode('UTF-8')
        key = pad(key, AES.block_size)

        cipher = AES.new(key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(data.encode('UTF-8'), AES.block_size))
        encrypted_data = b64encode(cipher.iv + ciphertext).decode('UTF-8')

        return encrypted_data
    else:
        return "Encryption failed. Incorrect password."

if __name__ == '__main__':
    app.run()