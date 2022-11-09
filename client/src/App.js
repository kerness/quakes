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
   const [query, setQuery] = useState({
      minmag: 0,
      maxmag: 10,
      startdate: '',
      enddate: '',
      lat: '',
      lng: '',
      radius: ''
   })

   // const [circleQuery, setCircleQuery] = useState({
   //    lat: '',
   //    lng: '',
   //    radius: ''
   // })


   useEffect(() => {
      const fetchData = async () => {
         setLoading(true)
         const url = `http://localhost:8000/quakes/?format=json` +
            `&date_after=${query.startdate}` +
            `&date_before=${query.enddate}` +
            `&mag_min=${query.minmag}` +
            `&mag_max=${query.maxmag}` +
            `&lat=${query.lat}` +
            `&lng=${query.lng}` +
            `&radius=${query.radius}` +
            `&vendor=${activeVendor}` +
            `&ordering=-${query.mag}`
         console.log(url);
         const result = await axios(url)
         //const result = await axios(`http://localhost:8000/quakes/?format=json&limit=60&offset=3000&vendor=${activeVendor}`)
         //console.log(result.data.results.features);
         setQuakesData(result.data.features)
         setLoading(false)
      }
      fetchData()
      console.log(query)
   }, [activeVendor, query])

   // change Vendor
   const changeVendor = () => {
      if (activeVendor === 'GRSS') {
         setActiveVendor('USGS')
         setZoom(3)
         setCenter([19.00, 19.00])
      } 
      else if (activeVendor === 'USGS') {
         setActiveVendor('GRSS')
         setZoom(8)
         setCenter([50.505, 19.09])
      } 
      console.log(activeVendor);
   }

   // getQuer


   return (

      <div className='app-container'>
      <Menu onVendorChange={ changeVendor } vendor={ activeVendor } getQuery={ (q) => setQuery(q) }/>
      {/* <Menu onVendorChange={changeVendor} vendor={activeVendor} getQuery={(q) => setQuery(q)} getCircleQuery={(q) => setCircleQuery(q)}/> */}

      { !loading ? <QuakesMap center={center} zoom={zoom} quakesData={quakesData}/> : <Spinner />}
      


      </div>
   )
}

export default App;