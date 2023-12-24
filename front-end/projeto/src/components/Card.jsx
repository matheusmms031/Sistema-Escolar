import '../styles/CardStyle.scss'
import Image from "../assets/image2.jpg"



function Card(props) {
    return(
        <div className="card-painel">
            <img src={Image}/>
            <div className='card-contents'>
                <h1>{props.title}</h1>
                <span>{props.about}</span>
            </div>
        </div>
    )
}

export default Card;