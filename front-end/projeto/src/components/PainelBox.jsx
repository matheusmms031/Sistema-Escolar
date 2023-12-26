import '../styles/PainelBoxStyle.scss'


function PainelBox(props) {
    var justifycontent = ''
    if(props.page == true){
        justifycontent = 'center'
    }
    else{
        justifycontent = 'flex-start'
    }


    return(
        <section className="painelbox" style={{'justifyContent':justifycontent}}>
            {props.children}
        </section>
    )
}

export default PainelBox;