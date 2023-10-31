import React from 'react';
import './Muk.css';

function Muk() {
  const [profileImg, setProfileImg] = React.useState('https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png');
  const [selectedFile, setSelectedFile] = React.useState(null);

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
      <div></div>
    </div>
  );
};

export default Muk;