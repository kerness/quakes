import axios from 'axios';
import React, { useState } from "react";
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import useSWR from "swr";
import { Alert } from "react-bootstrap";
import "./App.css"

const fetcher = (url) =>axios.get(url).then((res) => res.data)

const App = () => {
  const [activeQuake, setActiveQuake] = useState(null);

  const { data, error } = useSWR("http://localhost:8000/quakes", fetcher);
  const quakes = data && !error ? data : {};
  if (error) {
    return <Alert variant="danger">There is a problem</Alert>;
 }
 if (!data) {
    return <Alert variant="danger">No data</Alert>;
 }
  return (
    <MapContainer center={[1, 1]} zoom={9}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
               {quakes.results.features.map((quake) => (
            <Marker
               key={quake.properties.name}
               position={[
                  quake.geometry.coordinates[1],
                  quake.geometry.coordinates[0],
               ]}
               onClick={() => {
                  setActiveQuake(quake);
               }}

            >
               <Popup
                  position={[
                     quake.geometry.coordinates[1],
                     quake.geometry.coordinates[0],
                  ]}
                  onClose={() => {
                     setActiveQuake(null);
                  }}
               >
                  <div>
                     <h6>{quake.geometry.coordinates[0]}, {quake.geometry.coordinates[1]}</h6>
                     <p>{quake.properties.date}</p>
                     <p>Dostawca danych:{quake.properties.vendor}</p>
                     <p>Magnituda: {quake.properties.mag}</p>

                  </div>
               </Popup>
            </Marker>
         ))}
    </MapContainer>
  );
};

export default App;
