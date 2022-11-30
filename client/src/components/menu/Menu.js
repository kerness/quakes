import Button from "./Button"
import Header from "./Header"
import Search from "./Search"
import CircleSearch from "./CircleSearch";
import SubHeader from "./SubHeader";
import ModeSwitcher from "./ModeSwitcher";
const Menu = ({ onVendorChange, vendor, getQuery, toUSGS, toGRSS, activeVendor }) => {
  return (
    <div className='menu'>
      <Header title="Trzęsienia Ziemi" />
      {/* <Button color="#a1acbd" text={vendor} onClick={onVendorChange} /> */}
      <h4>Wybierz dostawcę danych</h4>
      <ModeSwitcher activeVendor={activeVendor} toUSGS={toUSGS} toGRSS={toGRSS}/>
      <Search getQuery={getQuery}/>
      {/* <SubHeader title="Wyszukaj trzęsienie w kole!"/> */}
      {/* <CircleSearch getCircleQuery={getCircleQuery}/> */}
    </div>
  )
}

export default Menu
