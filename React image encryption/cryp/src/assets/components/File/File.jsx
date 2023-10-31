import React, { useState } from 'react';
import css from '../File/file.module.css';
import axios from 'axios';

const File = () => {
  const [profileImg, setProfileImg] = React.useState('https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png');
  const [selectedFile, setSelectedFile] = React.useState(null);
  const [encryptedImage, setEncryptedImage] = useState(null);
  const [decryptedImage, setDecryptedImage] = useState(null);
  const [encryptionPassword, setEncryptionPassword] = useState('');
  const [decryptionPassword, setDecryptionPassword] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const [selectedDecryptedImage, setSelectedDecryptedImage] = useState(null);

  const handleEncryptedSubmit = () => {
    const password = encryptionPassword;
    const file = selectedImage;
    encryptImage(file, password);
  };

  

  const handleEncryptionPasswordChange = (e) => {
    setEncryptionPassword(e.target.value);
  };

  const handleDecryptionPasswordChange = (e) => {
    setDecryptionPassword(e.target.value);
  };

  const handleDecryptedSubmit = () => {
    const password = decryptionPassword;
    const file = selectedDecryptedImage;
    decrypt(file, password);
  };
  const handleImageChange = (e, isDecryption) => {
    const selectedFile = e.target.files[0];
    if (isDecryption) {
      setSelectedDecryptedImage(selectedFile);
    } else {
      setSelectedImage(selectedFile);
    }
  };

  const encryptImage = (file, password) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('password', password);
    formData.append('key', '0123456789abcdef0123456789abcdef');

    axios.post('http://localhost:5000/encryption', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
      .then((response) => {
        console.log('Image uploaded:', response.data);
        setEncryptedImage(response.data.image);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const decrypt = (file, password) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('password', password);
    formData.append('key', '0123456789abcdef0123456789abcdef');
  
    axios.post('http://localhost:5000/decryption', formData, {
      responseType: 'blob' // Specify response type as 'blob' to handle binary data
    })
      .then((response) => {
        console.log('Decryption successful!');
        const decryptedImageUrl = URL.createObjectURL(response.data);
        setDecryptedImage(decryptedImageUrl);
      })
      .catch((error) => {
        console.error('Decryption failed:', error);
      });
  };




  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedFile(file);

    const reader = new FileReader();
    reader.onload = () => {
      if (reader.readyState === 2) {
        setProfileImg(reader.result);
      }
    };
    reader.readAsDataURL(file);
  };



  return (
    <div className="page">
      <div className="encryption">Image Encryption</div>
      <div className="container">
        <h1 className="heading">Add your File</h1>
        <div className="img-holder">
          <img src={profileImg} alt="" id="img" className="img" />
        </div>
        <input type="file" name="file-upload" id="input" onChange={handleFileChange} />
        <div className="label">
          <label className="file-upload" htmlFor="input">
            <i className="material-icons"></i>
            Choose your File Here
          </label>
        </div>
      </div>

      <div className={css.image}>
        <div className={css.enc}>
          <div className={css.tex}>Encrypted File</div>
          <div className={css.holde}>
            {encryptedImage && <img src={encryptedImage} alt="" className={css.encryptedImage} />}
          </div>
        </div>
        <input
          type="password"
          className="encpass"
          value={encryptionPassword}
          onChange={handleEncryptionPasswordChange}
        />
        <input
          type="file"
          className={css.fileInput}
          onChange={handleImageChange}
        />
        <button className={css.but1} onClick={handleEncryptedSubmit}>
          Encrypt
        </button>
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
        <input
          type="file"
          className={css.fileInput}
          onChange={(e) => handleImageChange(e, true)}
        />
        <button className={css.but} onClick={handleDecryptedSubmit}>
          Decrypt
        </button>
        <div className={css.lertsign}></div>
      </div>
    </div>
  );
};
  
  export default File;