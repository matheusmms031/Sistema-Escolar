import '../styles/OperacionalTitleStyle.scss'


function OperacionalTitle(props){
    return(
        <section className="operacional-title">
            <span>{props.title}</span>
        </section>
    )
}

export default OperacionalTitle