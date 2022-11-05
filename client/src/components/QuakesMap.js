import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";
import LocationMarker from "./LocationMarker";

const QuakesMap = ({ center, zoom, quakesData }) => {
    const markers = quakesData.map(quake => {
        const lat = quake.geometry.coordinates[1]
        const lng = quake.geometry.coordinates[0]
        return (
            <Marker position={[lat, lng]} key={quake.id}>
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

            </Marker>
        )

    })

    return (

        <MapContainer className="map"
            center={center}
            zoom={zoom}
            style={{ height: "100vh" }}
        >
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            {markers}

        </MapContainer>

    )
}

export default QuakesMap
