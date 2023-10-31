from flask import Flask, request
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/decryption', methods=['POST'])
def handle_decryption():
    # Get the uploaded file and key from the form data
    uploaded_file = request.files['file']
    key = request.form['key']

    print(f"File: {uploaded_file.filename}")
    print(f"Key: {key}")
    # Read the encrypted file data
    encrypted_file_data = open(uploaded_file.filename, 'rb').read()
    # Extract the IV and ciphertext from the encrypted data
    iv = encrypted_file_data[:16]
    ciphertext = encrypted_file_data[16:]

    # Decrypt the ciphertext
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)

    # Save the decrypted data to a new file
    decrypted_file_path = uploaded_file.filename + '.dec'
    with open(decrypted_file_path, 'wb') as decrypted_file: 
        decrypted_file.write(plaintext)

    return 'File decrypted and saved as ' + decrypted_file_path

if __name__ == '__main__':
    app.run()