
import { useState } from 'react'
import { useForm } from "react-hook-form";
const CircleSearch = ({ getCircleQuery }) => {
    const [circleQueryData, setCircleQueryData] = useState('')
    const { register, formState: { errors }, handleSubmit } = useForm();
    const onSubmit = (data) => {
        //alert(JSON.stringify(data))
        setCircleQueryData(data)
        getCircleQuery(data)
    };


    return (
        <form className="search-form" onSubmit={handleSubmit(onSubmit)}>
            <label htmlFor="lat">Szerokość geograficzna:</label>
            <input type="number" id="lat" name="lat" {...register('lat', { required: false })} />

            <label htmlFor="lng">Długość geograficzna:</label>
            <input type="number" id="lng" name="lng" { ...register('lng', { required: false }) }/>

            <label htmlFor="radius">Promień:</label>
            <input type="number" id="radius" name="radius" { ...register('radius', { required: false }) }/>

            <input type="submit" id="submit" value="Szukaj" />
        </form>
    )
}

export default CircleSearch
