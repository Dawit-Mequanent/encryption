from flask import Flask, request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode

app = Flask(__name__)

@app.route('/encryption', methods=['POST'])
def handle_encryption():
    # Get the uploaded file and key from the form data
    uploaded_file = request.files['file']
    key = request.form['key']

    # Read the file data
    file_data = uploaded_file.read()
    # Encrypt the file data
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB)
    ciphertext = cipher.encrypt(pad(file_data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ciphertext = b64encode(ciphertext).decode('utf-8')
    encrypted_data = iv + ciphertext

    # Save the encrypted data to a new file
    encrypted_file_path = uploaded_file.filename + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file: 
        encrypted_file.write(encrypted_data.encode('utf-8'))

    return 'File encrypted and saved as ' + encrypted_file_path

if __name__ == '__main__':
    app.run()