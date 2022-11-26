import { useState, useEffect } from 'react'
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import QuakesMap from "./components/QuakesMap";
import axios from 'axios'
import Spinner from "./components/Spinner"
import TopBar from './components/TopBar';
import Menu from './components/menu/Menu';

function parseDate(date) {
   let dd = String(date.getDate()).padStart(2, '0');
   let mm = String(date.getMonth() + 1).padStart(2, '0'); //January is 0!
   let yyyy = date.getFullYear();
   return yyyy + '-' + mm + '-' + dd;
}

function date() {
   // get startdate and enddate based on current date
   let startdate = new Date()
   startdate.setDate(startdate.getDate()-30);
   let enddate = new Date();

   // console.log(parseDate(startdate));
   // console.log(parseDate(enddate));
   return [parseDate(startdate), parseDate(enddate)];
   
}


function App() {
   const [dates, setDates] = useState(date())
   const [quakesData, setQuakesData] = useState([])
   const [loading, setLoading] = useState(false)
   const [activeQuake, setActiveQuake] = useState(null);
   const [activeVendor, setActiveVendor] = useState('GRSS');
   const [zoom, setZoom] = useState(8)
   const [center, setCenter] = useState([50.505, 19.09])
   const [query, setQuery] = useState({
      minmag: 0,
      maxmag: 10,
      startdate: dates[0],
      enddate: dates[1],
      lat: '',
      lng: '',
      radius: ''
   })


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

      changeCenter()
      console.log(query)
   }, [activeVendor, query])


   // change center
   // TODO: jakiś sensowny setZOOM
   const changeCenter = () => {
      if (query.lat != '' && query.lng != '') {
         setCenter([query.lng, query.lat])
         console.log(center);
         setZoom(7)
      }
   }

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

   // change to USGS
   const toUSGS = () => {
      setActiveVendor('USGS')
      setZoom(3)
      setCenter([19.00, 19.00])
      console.log(activeVendor);
   }

   // change to USGS
   const toGRSS = () => {
      setActiveVendor('GRSS')
      setZoom(8)
      setCenter([50.505, 19.09])
      console.log(activeVendor);
   }


   return (

      <div className='app-container'>
      <Menu activeVendor={activeVendor} toUSGS={toUSGS} toGRSS={toGRSS} onVendorChange={ changeVendor } vendor={ activeVendor } getQuery={ (q) => setQuery(q) }/>
      {/* <Menu onVendorChange={changeVendor} vendor={activeVendor} getQuery={(q) => setQuery(q)} getCircleQuery={(q) => setCircleQuery(q)}/> */}

      { !loading ? <QuakesMap center={center} zoom={zoom} quakesData={quakesData}/> : <Spinner />}
      


      </div>
   )
}

export default App;