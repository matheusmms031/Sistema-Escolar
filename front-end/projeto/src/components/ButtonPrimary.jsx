import '../styles/ButtonPrimaryStyle.scss'

function ButtonPrimary(props){
    return(
        <div className="buttonprimary">
	    	{props.children}
	    </div>
    );
}

export default ButtonPrimary;