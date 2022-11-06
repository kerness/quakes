
import { useState } from "react";
import { useForm } from "react-hook-form";

const Search = ( { getQuery }) => {


    const [queryData, setQueryData] = useState('')
    const { register, formState: { errors }, handleSubmit } = useForm();
    const onSubmit = (data) => {
        //alert(JSON.stringify(data))
        setQueryData(data)
        getQuery(data)
    };


    return (
        // TODO: zrobić tak żeby data druga nie mogła być wcześniejsza od pierwszej
        <form className="search-form" onSubmit={handleSubmit(onSubmit)}>
            <label htmlFor="start-date">Data początkowa:</label>
            <input type="date" id="start-date" name="start-date"
                { ...register('startdate', { required: true }) }
                aria-invalid={errors.startdate ? "true" : "false"}
            />
            { errors.startdate?.type === "required" && <p role="alert">Data początkowa jest wymagana.</p> }

            <label htmlFor="end-date">Data końcowa:</label>
            <input type="date" id="end-date" name="end-date"
                { ...register('enddate', { required: true }) }
                aria-invalid={errors.enddate ? "true" : "false"}
            />
            { errors.enddate?.type === "required" && <p role="alert">Data końcowa jest wymagana.</p> }

            <label htmlFor="min-mag">Minimalna magnituda:</label>
            <input type="number" id="min-mag" name="min-mag"
                {...register('minmag', { required: true, min: 0.1, max: 10 })}
                aria-invalid={errors.minmag ? "true" : "false"}
            />
            { errors.minmag?.type === "required" && <p role="alert">Podaj minimalną wartość magnitudy.</p> }


            <label htmlFor="max-mag">Maksymalna magnituda:</label>
            <input type="number" id="max-mag" name="max-mag"
                {...register('maxmag', { required: true, min: 0.1, max: 10 })}
                aria-invalid={errors.maxmag ? "true" : "false"}
            />
            { errors.maxmag?.type === "required" && <p role="alert">Podaj maksymalną wartość magnitudy.</p> }
            
            <input type="submit" id="submit" value="Szukaj" />
        </form>
    )
}

export default Search
