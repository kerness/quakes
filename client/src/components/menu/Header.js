import PropTypes from 'prop-types'

const Header = ({ title, onAdd, showAdd }) => { // the same like (props) and then props.title
    
    return (
        <header className = "header">
            <h1>{title}</h1>
        </header>
    )
}

Header.defaultProps = {
    title: 'Task Tracker'
}
Header.propTypes = {
    title: PropTypes.string.isRequired,
}
// CSS in JS
// const headingStyle = {
//     color: 'red', backgroundColor: 'black'
// }
export default Header
