import React from "react";
import PropTypes from "prop-types";

import "./card.css";
//<p>AEVA</p>
function Card({ imageSource, title, text, url }) {
  return (
    <div className="card text-center bg-dark animate__animated animate__fadeInUp">
      <div className="overflow2">
        <img src={imageSource} alt="a wallpaper" className="card-img-top" />
        <div className="card-body text-light">
        <h4 className="card-title">{title}</h4>
        <p className="card-text text-secondary">
          {text
            ? text
            : "FELIZ"}
        </p>
        
      </div>
      </div>
      
    </div>
  );
}

Card.propTypes = {
  title: PropTypes.string.isRequired,
  text: PropTypes.string,
  url: PropTypes.string,
  imageSource: PropTypes.string
};

export default Card;