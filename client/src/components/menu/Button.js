import PropTypes from 'prop-types'


const Button = ({ text, onClick}) => { // destructure props object
    
    return (
        <button 
            onClick={onClick}
            // style={{ backgroundColor: color}}
            className='btn'>
                {text}
        </button>
    )
}
Button.defaultProps = {
    color: 'steelblue'
}



Button.propTypes = {
    title: PropTypes.string,
    color: PropTypes.string,
    onClick: PropTypes.func,
}
export default Button
