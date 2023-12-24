import "../styles/Home.scss";
import Image from '../assets/image.png'
import ButtonPrimary from '../components/ButtonPrimary.jsx'
import { useState } from "react";
import axios from 'axios';


function Home() {
	const [email, setEmail] = useState("")
	const [senha, setSenha] = useState("")
	const [dados, setDados] = useState({})

	const handleChangeEmail = (event) => {
		setEmail(event.target.value);
	};

	const handleChangeSenha = (event) => {
		setSenha(event.target.value);
	};

	const login = () => {
		var bodyFormData = new FormData();
		bodyFormData.append('email',email)
		bodyFormData.append('senha',senha)
		console.log(email,senha)
		axios({
			method: "post",
			url: "http://127.0.0.1:5000/login",
			data: bodyFormData,
			headers: { "Content-Type": "multipart/form-data" },
		  })
			.then(function (response) {
			  //handle success
			  if (response.data.status_code == 200){
				setDados(response.data.data)
				console.log(dados)
			  }
			})
	}

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
					<span className="autor">By: Matheus Magalhães</span>
				</div>
			</div>
		</section>
		<section className="direita">
			<div className="titulos">
				<h1>LOGIN DA PLATAFORMA</h1>
				<span>SISTEMA-ESCOLAR</span>
			</div>
			<div className="content">
				<div className="content-box">
					<div className="box-input">
						<span className="titulo">Email</span>
						<input type="text" placeholder="Escreva seu email" onChange={handleChangeEmail}/>
					</div>
				</div>
				<div className="content-box">
					<div className="box-input">
						<span className="titulo">Senha</span>
						<input type="text" placeholder="Escreva sua senha" onChange={handleChangeSenha}/>
					</div>
				</div>
				<ButtonPrimary onClick={login}>
					<svg xmlns="http://www.w3.org/2000/svg" width="21" height="20" viewBox="0 0 21 20" fill="none">
						<path d="M13 2.5H16.3333C16.7754 2.5 17.1993 2.67559 17.5118 2.98816C17.8244 3.30072 18 3.72464 18 4.16667V15.8333C18 16.2754 17.8244 16.6993 17.5118 17.0118C17.1993 17.3244 16.7754 17.5 16.3333 17.5H13" stroke="#FEFEFE" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M8.83337 14.1666L13 9.99998L8.83337 5.83331" stroke="#FEFEFE" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
						<path d="M13 10H3" stroke="#FEFEFE" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
					</svg>
					<span>Entrar</span>
				</ButtonPrimary>
			</div>
		</section>
    </div>
  );
}

export default Home;
