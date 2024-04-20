// AppRouter.js
import React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";

import Login from "./login";
import Registro from "./registro";
import Inicio from "./Inicio";
import Principal from "./principal";
export const AppRouter = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Inicio/>} />
        <Route path="/Login" element={<Login />} />
        <Route path="/registro" element={<Registro />} />   
        <Route path="/home" element={<Principal/>} />   
      

      </Routes>
    </BrowserRouter>
    
  );
};