// import axios from 'axios';
// import useSWR from "swr";
// import React, { useState } from "react";
// import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
// import { Alert } from "react-bootstrap";
// import "./App.css"




// // import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// // import Navbar from './components/Navbar';
// // import World from './pages/world'
// // import Silesia from './pages/silesia'

// const fetcher = (url) => axios.get(url).then((res) => res.data)




// const App = () => {
//    const [activeQuake, setActiveQuake] = useState(null);

//    const { data, error } = useSWR("http://localhost:8000/quakes/?vendor=GRSS&limit=300/", fetcher);
//    console.log("HE", data)
//    const quakes = data && !error ? data : {};
//    if (error) {
//       return <Alert variant="danger">There is a problem</Alert>;
//    }
//    if (!data) {
//       return <Alert variant="danger">No data</Alert>;
//    }
//    return (
//       <MapContainer center={[32, 18]} zoom={3}>
//          <TileLayer
//             attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
//             url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
//          />
//          {quakes.results.features.map((quake) => (
//             <Marker
//                key={quake.properties.name}
//                position={[
//                   quake.geometry.coordinates[1],
//                   quake.geometry.coordinates[0],
//                ]}
//                onClick={() => {
//                   setActiveQuake(quake);
//                }}

//             >
//                <Popup
//                   position={[
//                      quake.geometry.coordinates[1],
//                      quake.geometry.coordinates[0],
//                   ]}
//                   onClose={() => {
//                      setActiveQuake(null);
//                   }}
//                >
//                   <div>
//                      <h6>{quake.geometry.coordinates[0]}, {quake.geometry.coordinates[1]}</h6>
//                      <p>{quake.properties.date}</p>
//                      <p>Dostawca danych:{quake.properties.vendor}</p>
//                      <p>Magnituda: {quake.properties.mag}</p>

//                   </div>
//                </Popup>
//             </Marker>
//          ))}
//       </MapContainer>

//    );
// };

// export default App;



import { useState, useEffect } from 'react'
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import QuakesMap from "./components/QuakesMap";
import axios from 'axios'
import Spinner from "./components/Spinner"
function App() {
   const [quakesData, setQuakesData] = useState([])
   const [loading, setLoading] = useState(false)
   const [activeQuake, setActiveQuake] = useState(null);


   useEffect(() => {
      const fetchData = async () => {
         setLoading(true)
         const result = await axios('http://localhost:8000/quakes/?format=json&limit=20&offset=3482&vendor=GRSS')
         //console.log(result.data.results.features);
         setQuakesData(result.data.results.features)
         setLoading(false)
      }
      fetchData()
   }, [])


   const position = [50.505, 19.09]
   return (
      // <QuakesMap center={position} zoom={6} />
      <div>
      { !loading ? <QuakesMap center={position} zoom={8} quakesData={quakesData}/> : <Spinner />}
      </div>
   )
}

export default App;