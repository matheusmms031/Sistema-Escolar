import '../styles/PainelBoxStyle.scss'


function PainelBox(props) {
    var justifycontent = ''
    var flexdirection = ''
    if(props.page == true){
        justifycontent = 'center'
        flexdirection = 'row'
    }
    else{
        justifycontent = 'flex-start'
        flexdirection = 'column'
    }




    return(
        <section className="painelbox" style={{'justifyContent':justifycontent,'flexDirection':flexdirection}}>
            {props.children}
        </section>
    )
}

export default PainelBox;