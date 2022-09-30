import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import "./App.css"


const App = () => {
  return (
    <MapContainer>
            <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
    </MapContainer>
  );
};

export default App;
