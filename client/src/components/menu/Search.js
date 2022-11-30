
import { useState } from "react";
import { useForm } from "react-hook-form";

const Search = ( { getQuery }) => {


    const [queryData, setQueryData] = useState('')
    const { register, formState: { errors }, handleSubmit, getValues } = useForm();
    const onSubmit = (data) => {
        //alert(JSON.stringify(data))
        setQueryData(data)
        getQuery(data)
        console.log(data);
    };

    // jeśli jest podane choć jedo z pól służących do CircleSearch to tylko wtedy sprawdź czy są podane pozostałe dwa xd
    const areCircleSearchData =  (v) => {
        console.log(v === '');
        console.log(getValues('lat')==='')
        if (v != '' || getValues('lat') != '' || getValues('radius')) {
            if (v != '' && getValues('lat') != '' && getValues('radius')) {
                console.log("Koord są poprawne")
                return true
            }
            return false
        }
        return true
      };
      


    return (
        // TODO: zrobić tak żeby data druga nie mogła być wcześniejsza od pierwszej
        <form className="search-form" onSubmit={handleSubmit(onSubmit)}>
            <h4>Wyszukaj trzęsienia o zadanych parametrach</h4>
            <label htmlFor="start-date">data początkowa</label>
            <input type="date" id="start-date" name="start-date"
                { ...register('startdate', { 
                    required: true 
                    }) 
                }
            />
            { errors.startdate?.type === "required" && <p role="alert">Data początkowa jest wymagana.</p> }

            <label htmlFor="end-date">data końcowa</label>
            <input type="date" id="end-date" name="end-date"
                { ...register('enddate', {
                    required: true,
                    validate: value => value > getValues("startdate") || "Wybierz datę późniejszą niż data początkowa",// make sure that enddate is later then startdate
                    deps: ["startdate"]
                    }) 
                }
            />
            { errors.enddate?.type === "required" && <p role="alert">Data końcowa jest wymagana.</p> }
            { errors.enddate?.type === "validate" && <p role="alert">{errors.enddate?.message}</p> }

            <label htmlFor="min-mag">minimalna magnituda</label>
            <input type="number" step="0.01" id="min-mag" name="min-mag"
                {...register('minmag', { required: false, min: 0.1, max: 10 })}
            />

            <label htmlFor="max-mag">maksymalna magnituda</label>
            <input type="number" step="0.01" id="max-mag" name="max-mag"
                {...register('maxmag', { required: false, min: 0.1, max: 10 })}
            />






            {/* TODO: jakoś to wyróżnić */}
            <h4>Wyszukaj trzęsienia w zadanym okręgu</h4>
            <label htmlFor="lng">szerokość geograficzna</label>
            <input type="number" step="0.01" id="lng" name="lng" 
                { ...register('lng', { required: false,
                    min: {value: -90, message: "Szerokość geograficzna nie może być mniejsza niż -90." },
                    max: {value: 90, message: "Szerokość geograficzna nie może być większa niż 90." },
                    validate: {
                        circleSearchData: areCircleSearchData
                    }
                    })
                }
            />
            { errors.lng?.type === "max" && <p role="alert">{errors.lng?.message}</p> }
            { errors.lng?.type === "min" && <p role="alert">{errors.lng?.message}</p> }


            <label htmlFor="lat">długość geograficzna</label>
            <input type="number" step="0.01" id="lat" name="lat" 
                {...register('lat', { required: false ,
                    min: {value: -180, message: "Długość geograficzna nie może być mniejsza niż -180." },
                    max: {value: 180, message: "Długość geograficzna nie może być większa niż 180." },

                    }) 
                } 
            />

            <label htmlFor="radius">promień</label>
            <input type="number" id="radius" name="radius"
                { ...register('radius', { required: false,
                    min: {value: 1, message: "Promień nie może być mniejszy od 1." },
                    max: {value: 3000, message: "Promień nie może być większy od 3000" },
                    })
                }
            />

            { errors.lng?.type === "circleSearchData" && <p role="alert">Upewnij się, że podałeś długość, szerokość i promień </p> }           

            <input type="submit" id="submit" value="Szukaj" />
        </form>
    )
}
export default Search
