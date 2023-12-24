import '../styles/ButtonPrimaryStyle.scss'

function ButtonPrimary(props){
    return(
        <div className="buttonprimary" onClick={props.onClick}>
	    	{props.children}
	    </div>
    );
}

export default ButtonPrimary;