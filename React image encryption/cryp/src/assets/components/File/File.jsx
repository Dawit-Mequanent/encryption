import React from "react";
import css from "../File/file.module.css";

const File = () => {
  
  return (
    <div className={css.image}>
      
      <div className={css.enc}>Encrypted File</div>
      <input type="password" className="encpass"></input>
      <input type="submit" value="Encrypted" className={css.but1}></input>
      
      <div className={css.dec}>Decrypted Image</div>
      <input type="password" className="decpass"></input>
      <input type="submit" value="Decrypted" className={css.but}></input>
    </div>
  );
};
export default File;
