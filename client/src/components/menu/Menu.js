import Button from "./Button"
import Header from "./Header"
import Search from "./Search"
import CircleSearch from "./CircleSearch";
import SubHeader from "./SubHeader";

const Menu = ({ onVendorChange, vendor, getQuery, getCircleQuery }) => {
  return (
    <div className='menu'>
      <Header title="Mapa trzęsień ziemi" />
      <Button color="#a1acbd" text={vendor} onClick={onVendorChange} />
      <Search getQuery={getQuery}/>
      {/* <SubHeader title="Wyszukaj trzęsienie w kole!"/> */}
      {/* <CircleSearch getCircleQuery={getCircleQuery}/> */}
    </div>
  )
}

export default Menu
