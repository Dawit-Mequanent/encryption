import React, { Component } from 'react';
import './Muk.css';
import axios from 'axios';

export class Muk extends Component {
  state = {
    profileImg: 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png',
    selectedImage: null
  };

  imageHandler = (e) => {
    const reader = new FileReader();
    reader.onload = () => {
      if (reader.readyState === 2) {
        this.setState({ profileImg: reader.result, selectedImage: e.target.files[0] });
      }
    };
    reader.readAsDataURL(e.target.files[0]);
  };

  uploadImage = () => {
    const { selectedImage } = this.state;
    if (!selectedImage) {
      console.log('No image selected');
      return;
    }

    const formData = new FormData();
    formData.append('image', selectedImage);

    axios.post('http://localhost:5000/encryption', formData)
      .then((response) => {
        console.log('Image uploaded:', response.data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  render() {
    const { profileImg } = this.state;
    return (
      <div className="page">
        <div className="encryption">Image Encryption</div>
        <div className="container">
          <h1 className="heading">Add your Image</h1>
          <div className="img-holder">
            <img src={profileImg} alt="" id="img" className="img" />
          </div>
          <input type="file" accept="image/*" name="image-upload" id="input" onChange={this.imageHandler} />
          <div className="label">
            <label className="image-upload" htmlFor="input">
              <i className="material-icons"></i>
              Choose your Photo Here
            </label>
            <button onClick={this.uploadImage} className='up'>Upload Image</button>
          </div>
        </div>
        <div></div>
      </div>
    );
  }
}

export default Muk;