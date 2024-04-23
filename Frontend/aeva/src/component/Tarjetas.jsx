import React from "react";
import Card from "./tarjeta";

import image1 from "./image1.jpg";
import image2 from "./image1.jpg";
import image3 from "./image1.jpg";
import { Grid } from '@mui/material';

const cards = [
  {
    id: 1,
    title: "Enojado",
    image: "https://www.humanidadescomunidad.unam.mx/wp-content/uploads/2022/02/controlar-el-enojo-3.jpg",
    url: "https://st3.depositphotos.com/1954927/15490/v/950/depositphotos_154904942-stock-illustration-smileysad-emoticon-yellow-face-with.jpg",
  },
  {
    id: 2,
    title: "Disgusto",
    image: "https://previews.123rf.com/images/photocatcher/photocatcher1710/photocatcher171000023/87654728-retrato-de-hombre-barbudo-con-expresi%C3%B3n-de-disgusto-en-la-cara.jpg",
    url: "https://blog.faztweb.com",
  },
  {
    id: 3,
    title: "Miedo ",
    image: "https://previews.123rf.com/images/ulochka/ulochka1704/ulochka170400203/76873846-ni%C3%B1o-preadolescente-con-miedo-expresi%C3%B3n-miedo-de-cerca-retrato.jpg",
    url: "https://youtube.com/fazttech",
  },
  {
    id: 3,
    title: "Feliz",
    image: "https://previews.123rf.com/images/milkos/milkos1704/milkos170401690/76738985-persona-alegre-hombre-con-la-expresi%C3%B3n-facial-feliz-mirando-directamente-a-la-c%C3%A1mara-sobre-fondo.jpg",
    url: "https://youtube.com/fazttech",
  },
  { id: 3,
  title: "Triste ",
  image: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Face_of_fatigue.jpg/1200px-Face_of_fatigue.jpg",
  url: "https://youtube.com/fazttech",
},
{ id: 3,
  title: "Sorpresa ",
  image: "https://thumbs.dreamstime.com/z/retrato-sorpresa-y-chica-con-expresi%C3%B3n-facial-felicidad-contra-un-fondo-de-estudio-azul-cara-femenina-enfrentarse-una-ni%C3%B1a-273424603.jpg",
  url: "https://thumbs.dreamstime.com/z/retrato-sorpresa-y-chica-con-expresi%C3%B3n-facial-felicidad-contra-un-fondo-de-estudio-azul-cara-femenina-enfrentarse-una-ni%C3%B1a-273424603.jpg",
},
{ id: 3,
  title: "Neutral",
  image: "https://t4.ftcdn.net/jpg/05/95/54/59/360_F_595545902_EbcJu3vTGJumx9SUybRXoRB6ZIsiAI4w.jpg",
  url: "https://youtube.com/fazttech",
},

];

function Cards() {
  return (
    <div className="d-flex justify-content-center align-items-center h-100">
      <Grid container spacing={3}>
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