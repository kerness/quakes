import spinner from './spinner.gif'
const Spinner = () => {
  return (
    <div className="loader">
      <img src={spinner} alt='Loading' />
      <h1>Pobieranie danych...</h1>
    </div>
  )
}

export default Spinner
