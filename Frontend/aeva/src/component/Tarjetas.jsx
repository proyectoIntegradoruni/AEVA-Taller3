import React from "react";
import Card from "./tarjeta";

import image1 from "./image1.jpg";
import image2 from "./image1.jpg";
import image3 from "./image1.jpg";
import { Grid } from '@mui/material';

const cards = [
  {
    id: 1,
    title: "FELIZ",
    image: image1,
    url: "https://faztweb.com",
  },
  {
    id: 2,
    title: "Fazt Blog",
    image: image2,
    url: "https://blog.faztweb.com",
  },
  {
    id: 3,
    title: "Fazt Youtube",
    image: image3,
    url: "https://youtube.com/fazttech",
  },
  {
    id: 3,
    title: "Fazt Youtube",
    image: image3,
    url: "https://youtube.com/fazttech",
  },
];

function Cards() {
  return (
    <div className="d-flex justify-content-center align-items-center h-100">
      <Grid container spacing={1}>
        {cards.map(({ title, image, url, id }) => (
          <Grid item xs={12} sm={6} md={3} key={id}>
            <Card imageSource={image} title={title} url={url} />
          </Grid>
        ))}
      </Grid>
    </div>
  );
}

export default Cards;