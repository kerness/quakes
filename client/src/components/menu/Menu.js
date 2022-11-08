import Button from "./Button"
import Header from "./Header"
import Search from "./Search"
import CircleSearch from "./CircleSearch";
import SubHeader from "./SubHeader";

const Menu = ({ onVendorChange, vendor, getQuery }) => {
  return (
    <div className='menu'>
      <Header title="Mapa trzęsień ziemi" />
      <Button color="#e6ff0a" text={vendor} onClick={onVendorChange} />
      <Search getQuery={getQuery}/>
      <SubHeader title="Wyszukaj trzęsienie w kole!"/>
      <CircleSearch getQuery={getQuery}/>
    </div>
  )
}

export default Menu
