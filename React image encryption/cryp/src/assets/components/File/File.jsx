import React, { useState } from 'react';
import css from '../File/file.module.css';

const File = () => {
  const [encryptedImage, setEncryptedImage] = useState(null);
  const [decryptedImage, setDecryptedImage] = useState(null);
  const [encryptionPassword, setEncryptionPassword] = useState('');
  const [decryptionPassword, setDecryptionPassword] = useState('');

  const handleEncryptedSubmit = () => {
    const password = encryptionPassword;
    const file = 'image.jpg'; 
    encrypt(file, password);
  };

  const handleDecryptedSubmit = () => {
    const password = decryptionPassword;
    const file = 'image.jpg.enc'; 
    decrypt(file, password);
  };

  const handleEncryptionPasswordChange = (e) => {
    setEncryptionPassword(e.target.value);
  };

  const handleDecryptionPasswordChange = (e) => {
    setDecryptionPassword(e.target.value);
  };

  const encrypt = (file, password) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('password', password);

    fetch('/encryption', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        const encryptedImageData = data.encryptedImage;
        setEncryptedImage(encryptedImageData);
      })
      .catch((error) => {
        console.error('Encryption failed:', error);
      });
  };

  const decrypt = (file, password) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('password', password);

    fetch('/decryption', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        const decryptedImageData = data.decryptedImage;
        setDecryptedImage(decryptedImageData);
      })
      .catch((error) => {
        console.error('Decryption failed:', error);
      });
  };

  return (
    <div className={css.image}>
      <div className={css.enc}>
        <div className={css.tex}>Encrypted File</div>
        <div className={css.holde}>
          {encryptedImage && <img src={encryptedImage}
           alt="" className={css.encryptedImage} />}
        </div>
      </div>
      <input
        type="password"
        className="encpass"
        value={encryptionPassword}
        onChange={handleEncryptionPasswordChange}
      />
      <input type="submit" value="Encrypt" className={css.but1} onClick={handleEncryptedSubmit} />

      <div className={css.dec}>
        <div className={css.tex}>Decrypted Image</div>
        <div className={css.hold}>
          {decryptedImage && <img src={decryptedImage} alt="" className={css.decryptedImage} />}
        </div>
      </div>

      <input
        type="password"
        className="decpass"
        value={decryptionPassword}
        onChange={handleDecryptionPasswordChange}
      />
      <input type="submit" value="Decrypt" className={css.but} onClick={handleDecryptedSubmit} />
    </div>
  );
};

export default File;