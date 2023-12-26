import NavBar from '../components/NavBar';
import PainelBox from '../components/PainelBox';
import '../styles/PainelAlunos.scss'
import axios from 'axios';
import { useState,useContext, useEffect } from 'react';
import { UserContext, InfoContext } from '../App';
import OperacionalTitle from '../components/OperacionalTitle';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Button from '@mui/material/Button';
import SendIcon from '@mui/icons-material/Send';
import Stack from '@mui/material/Stack';
import { DataGrid } from '@mui/x-data-grid';
import Select from '@mui/material/Select';

function Alunos(){
    const [user,setUser] = useContext(UserContext)
    const [info,setInfo] = useContext(InfoContext)
    const [alunos,setAlunos] = useState("")
    const [unidadeid,setUnidadeId] = useState("")

    const handleChangeUnidadeId = (event) => {
        setUnidadeId(event.target.value);
        console.log(event.target.value)
    };

    const columnsAlunos = [
        { field: 'id', headerName: 'CPF', width: 180 },
        { field: 'nome', headerName: 'Nome', width: 300 },
        { field: 'nascimento', headerName: 'Nascimento', width: 260 },
        { field: 'email', headerName: 'Email', description: 'This column has a value getter and is not sortable.', width: 300},
        { field: 'senha', headerName: 'Senha', width: 200 },
        { field: 'unidade_id', headerName: 'Unidade ID', width: 130
        },
      ];
    
    const get_alunos = () => {
        var parametro = ""
        if(unidadeid != ""){
            var parametro = "?unidade_id="+unidadeid 
        }
        axios({
			method: "get",
			url: "http://127.0.0.1:5000/alunos/consulta"+parametro,
			headers: { "Content-Type": "multipart/form-data",'email-usuario':user.email,'senha-usuario':user.senha},
		  })
			.then(function (response) {
                var alunos = response.data.data
                info.alunos = alunos
                var lista_alunos = []
                
                    alunos.map((aluno) => {
                        lista_alunos.push({
                            id: aluno['cpf'],
                            nome: aluno['nome'],
                            email: aluno['email'],
                            nascimento: aluno['nascimento'],
                            senha: aluno['senha'],
                            unidade_id: aluno['unidade_id'],
                        }
                            )
                    })
                setAlunos(lista_alunos)
                setInfo(info)
			})
    }
    
    
    const get_unidades = () => {
        axios({
			method: "get",
			url: "http://127.0.0.1:5000/unidades/consulta",
			headers: { "Content-Type": "multipart/form-data",'email-usuario':user.email,'senha-usuario':user.senha},
		  })
			.then(function (response) {
				setInfo({'unidades':response.data.data})
                console.log(response)
			})
    }

    useEffect(() => {
        get_unidades()
    },[])

    useEffect(() => {
        console.log(info)
    },[info])

    return(
        <div className="home">
            <NavBar/>
            <OperacionalTitle title={'Alunos'}/>
            <PainelBox page={false}>
                <Stack direction={'row'} spacing={2}>
                    <FormControl sx={{ m: 1, minWidth: 220 }}>
                        <InputLabel id="demo-simple-select-autowidth-label">Unidade</InputLabel>
                        <Select
                        labelId="demo-simple-select-autowidth-label"
                        id="demo-simple-select-autowidth"
                        value={unidadeid}
                        onChange={handleChangeUnidadeId}
                        autoWidth
                        label="Unidade"
                        >
                            <MenuItem value="">
                                <em>None</em>
                            </MenuItem>
                            {(info.unidades.length != 0) ? (info.unidades.map((unidade) => {
                                return(<MenuItem value={unidade.id}>{unidade.nome}</MenuItem>)
                            })) : (null)}
                        </Select>
                    </FormControl>
                    <Button variant="contained" endIcon={<SendIcon />} onClick={get_alunos}>
                        Buscar
                    </Button>
                </Stack>
                {(alunos.length != 0) ? 
                (<DataGrid
                        rows={alunos}
                        columns={columnsAlunos}
                        initialState={{
                        pagination: {
                            paginationModel: { page: 0, pageSize: 5 },
                        },
                        }}
                        pageSizeOptions={[5, 10]}
                        checkboxSelection
                    />) : (null)}
            </PainelBox>
        </div>
    )
}

export default Alunos;