import { Circle } from "react-leaflet";


const CircleArea = ( { center, radius } ) => {

    // style options: https://leafletjs.com/reference.html#path
    const fillBlueOptions = { color: 'red', fillColor: 'red' }


    // radius w metrach

    return (
        <Circle center={center} pathOptions={fillBlueOptions} radius={radius} />
    )
}

export default CircleArea
