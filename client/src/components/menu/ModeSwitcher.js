import React from 'react'
import Button from './Button'

const ModeSwitcher = ( {onClick, toUSGS, toGRSS, activeVendor} ) => {

  // const colorButton = () => {
  //   if (activeVendor === "GRSS")
  //     return "red"
  //   else
  //     return "blue"
  // }
  console.log("aktywny vendor", activeVendor);
  return (
    <div className='mode-switcher'>
      <Button text={"GRSS"}  onClick={toGRSS} className="grss"></Button>
      <Button text={"USGS"} onClick={toUSGS} className="usgs"></Button>
    </div>
  )
}

export default ModeSwitcher
