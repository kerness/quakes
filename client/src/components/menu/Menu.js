import Button from "./Button"
import Header from "./Header"
import Search from "./Search"

const Menu = ({ onVendorChange, vendor, getQuery }) => {
  return (
    <div className='menu'>
      <Header title="Mapa trzęsień ziemi" />
      <Button color="#e6ff0a" text={vendor} onClick={onVendorChange} />
      <Search getQuery={getQuery}/>
      
    </div>
  )
}

export default Menu
