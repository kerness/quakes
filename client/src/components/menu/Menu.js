import Button from "./Button"
import Header from "./Header"

const Menu = ({ onVendorChange }) => {
  return (
    <div className='menu'>
      <Header title="Mapa trzęsień ziemi" />
      <Button color="#e6ff0a" text="USGS/GRSS" onClick={onVendorChange} />

      
    </div>
  )
}

export default Menu
