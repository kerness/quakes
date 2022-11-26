import { MapContainer, Marker, Popup, TileLayer, useMapEvents } from "react-leaflet";
import { CircleMarker } from 'react-leaflet/CircleMarker'
import MapEvents from "./MapEvents";

const QuakesMap = ({ center, zoom, quakesData }) => {
    console.log("Ilość obserwacji: " + quakesData.length)
    console.log("Center mapy:" + center)
    const markers = quakesData.map(quake => {
        const lat = quake.geometry.coordinates[1]
        const lng = quake.geometry.coordinates[0]
        return (
            <CircleMarker center={[lat, lng]} key={quake.id} radius={8}>
                <Popup
                    position={[
                        quake.geometry.coordinates[1],
                        quake.geometry.coordinates[0],
                    ]}
                >
                    <div className="popup">
                        <h6 style={{color: "black", fontWeight: "bold"}}>{quake.geometry.coordinates[1]}, {quake.geometry.coordinates[0]}</h6>
                        <p>{quake.properties.date}</p>
                        <p>Dostawca danych: {quake.properties.vendor}</p>
                        <p>Magnituda: {quake.properties.mag}</p>

                    </div>
                </Popup>

            </CircleMarker>
        )

    })
    

    return (

        // prefereCanvas miało być szybsze ale jakoś nie widzę
        <MapContainer className="map"
            center={center}
            zoom={zoom}
            preferCanvas={true}
        >
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {markers}
            <MapEvents/>
        </MapContainer>

    )
}

export default QuakesMap
