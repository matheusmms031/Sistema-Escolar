import "../styles/Home.css";
import Image from '../assets/image.png'

function Home() {
  return (
    <div className="login">
		<section className="esquerda">
			<div className="box">
				<div className="box-imagem">
					<img src={Image}/>
				</div>
				<div className="box-textos">
					<h1>LOGIN DA PLATAFORMA</h1>
					<span>SISTEMA-ESCOLAR</span>
				</div>
			</div>
		</section>
		<section className="direita">
			<div className="titulos">
				<h1>LOGIN DA PLATAFORMA</h1>
				<span>SISTEMA-ESCOLAR</span>
			</div>
			<div className="content">
				<p>TEste</p>
			</div>
		</section>
    </div>
  );
}

export default Home;
