import Button from "./Button"
import Header from "./Header"

const Menu = ({ onVendorChange, vendor }) => {
  return (
    <div className='menu'>
      <Header title="Mapa trzęsień ziemi" />
      <Button color="#e6ff0a" text={vendor} onClick={onVendorChange} />

      
    </div>
  )
}

export default Menu
