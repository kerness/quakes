import { useState, useEffect } from 'react'
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import QuakesMap from "./components/QuakesMap";
import axios from 'axios'
import Spinner from "./components/Spinner"
import TopBar from './components/TopBar';
import Menu from './components/menu/Menu';

function App() {
   const [quakesData, setQuakesData] = useState([])
   const [loading, setLoading] = useState(false)
   const [activeQuake, setActiveQuake] = useState(null);
   const [activeVendor, setActiveVendor] = useState('GRSS');
   const [zoom, setZoom] = useState(8)
   const [center, setCenter] = useState([50.505, 19.09])


   useEffect(() => {
      const fetchData = async () => {
         setLoading(true)
         const result = await axios(`http://localhost:8000/quakes/?format=json&limit=60&offset=3000&vendor=${activeVendor}`)
         //console.log(result.data.results.features);
         setQuakesData(result.data.results.features)
         setLoading(false)
      }
      fetchData()
   }, [activeVendor])

   // change Vendor
   const changeVendor = () => {
      if (activeVendor === 'GRSS') {
         setActiveVendor('USGS')
         setZoom(2)
         setCenter([19.00, 19.00])
      } 
      else if (activeVendor === 'USGS') {
         setActiveVendor('GRSS')
         setZoom(8)
         setCenter([50.505, 19.09])
      } 
      console.log(activeVendor);
   }


   const position = [50.505, 19.09]
   return (

      <div className='app-container'>
        <Menu onVendorChange={changeVendor} vendor={activeVendor}/>
      { !loading ? <QuakesMap center={center} zoom={zoom} quakesData={quakesData}/> : <Spinner />}
      


      </div>
   )
}

export default App;