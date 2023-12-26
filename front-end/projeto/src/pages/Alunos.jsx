import NavBar from "../components/NavBar";
import PainelBox from "../components/PainelBox";
import "../styles/PainelAlunos.scss";
import axios from "axios";
import { useState, useContext, useEffect } from "react";
import { UserContext, InfoContext } from "../App";
import OperacionalTitle from "../components/OperacionalTitle";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Button from "@mui/material/Button";
import SendIcon from "@mui/icons-material/Send";
import DeleteIcon from "@mui/icons-material/Delete";
import Stack from "@mui/material/Stack";
import TextField from "@mui/material/TextField";
import { DataGrid, useGridApiRef, GridToolbar } from "@mui/x-data-grid";
import Select from "@mui/material/Select";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { darkTheme } from "./Painel";
import Box from "@mui/material/Box";
import Tab from "@mui/material/Tab";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import TabContext from "@mui/lab/TabContext";
import TabList from "@mui/lab/TabList";
import Alert from "@mui/material/Alert";
import TabPanel from "@mui/lab/TabPanel";
import { Link } from "react-router-dom";
import AddIcon from '@mui/icons-material/Add';

function Alunos() {
  const [user, setUser] = useContext(UserContext);
  const [info, setInfo] = useContext(InfoContext);
  const [alunos, setAlunos] = useState("");
  const [rowSelectionModel, setRowSelectionModel] = useState([]);
  const [unidadeid, setUnidadeId] = useState("");
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [value, setValue] = useState("1");

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleChangeUnidadeId = (event) => {
    setUnidadeId(event.target.value);
    console.log(event.target.value);
  };

  const handleChangeNome = (event) => {
    setNome(event.target.value);
  };
  const handleChangeEmail = (event) => {
    setEmail(event.target.value);
  };

  const columnsAlunos = [
    { field: "id", headerName: "CPF", width: 180 },
    { field: "nome", headerName: "Nome", width: 300, editable: true },
    { field: "nascimento", headerName: "Nascimento", width: 260, editable: true },
    {
      field: "email",
      headerName: "Email",
      description: "This column has a value getter and is not sortable.",
      width: 300,
    },
    { field: "senha", headerName: "Senha", width: 200 },
    { field: "unidade_id", headerName: "Unidade ID", width: 130 },
  ];

  const get_alunos = () => {
    var parametro = "";
    if (unidadeid != "") {
      parametro = "unidade_id=" + unidadeid;
    }
    if (nome != "") {
      parametro = "nome=" + nome;
    }
    if (email != "") {
      parametro = "email=" + email;
    }
    axios({
      method: "get",
      url: "http://127.0.0.1:5000/alunos/consulta?" + parametro,
      headers: {
        "Content-Type": "multipart/form-data",
        "email-usuario": user.email,
        "senha-usuario": user.senha,
      },
    }).then(function (response) {
      var alunos = response.data.data;
      info.alunos = alunos;
      var lista_alunos = [];

      alunos.map((aluno) => {
        lista_alunos.push({
          id: aluno["cpf"],
          nome: aluno["nome"],
          email: aluno["email"],
          nascimento: aluno["nascimento"],
          senha: aluno["senha"],
          unidade_id: aluno["unidade_id"],
        });
      });
      setAlunos(lista_alunos);
      setInfo(info);
    });
  };

  const get_unidades = () => {
    axios({
      method: "get",
      url: "http://127.0.0.1:5000/unidades/consulta",
      headers: {
        "Content-Type": "multipart/form-data",
        "email-usuario": user.email,
        "senha-usuario": user.senha,
      },
    }).then(function (response) {
      setInfo({ unidades: response.data.data });
      console.log(response);
    });
  };

  useEffect(() => {
    get_unidades();
  }, []);

  useEffect(() => {
    console.log(info);
  }, [info]);

  useEffect(() => {
    console.log(rowSelectionModel);
  }, [rowSelectionModel]);
  useEffect(() => {
    console.log(rowSelectionModel);
  }, [rowSelectionModel]);

  return (
    <div className="home">
      <NavBar />
      <OperacionalTitle title={"Alunos"} />
      <PainelBox page={false}>
        <ThemeProvider theme={darkTheme}>
          <CssBaseline />
          <Box sx={{ width: "100%", typography: "body1" }}>
            <TabContext value={value}>
              <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
                <TabList
                  onChange={handleChange}
                  aria-label="lab API tabs example"
                >
                  <Tab label="Consulta" value="1" />
                  <Tab label="Adicionar" value="2" />
                  <Tab label="Item Three" value="3" />
                </TabList>
              </Box>
              <TabPanel value="1">
                <div className="alunos-painel-interno">
                  <Stack direction={"row"} spacing={2}>
                    <TextField
                      id="outlined-basic"
                      label="Nome"
                      variant="outlined"
                      onChange={handleChangeNome}
                    />
                    <TextField
                      id="outlined-basic"
                      label="Email"
                      variant="outlined"
                      onChange={handleChangeEmail}
                    />
                    <FormControl sx={{ m: 1, minWidth: 220 }}>
                      <InputLabel id="demo-simple-select-autowidth-label">
                        Unidade
                      </InputLabel>
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
                        {info.unidades.length != 0
                          ? info.unidades.map((unidade) => {
                              return (
                                <MenuItem value={unidade.id}>
                                  {unidade.nome}
                                </MenuItem>
                              );
                            })
                          : null}
                      </Select>
                    </FormControl>
                    <Button
                      variant="contained"
                      endIcon={<SendIcon />}
                      onClick={get_alunos}
                    >
                      Buscar
                    </Button>
                  </Stack>
                  {alunos.length != 0 ? (
                    <div style={{ height: 400, width: "100%" }}>
                      <DataGrid
                        onRowSelectionModelChange={(newRowSelectionModel) => {
                          setRowSelectionModel(newRowSelectionModel);
                        }}
                        rowSelectionModel={rowSelectionModel}
                        rows={alunos}
                        columns={columnsAlunos}
						slots={{
							toolbar: GridToolbar,
						  }}
                        initialState={{
                          pagination: {
                            paginationModel: { page: 0, pageSize: 5 },
                          },
                        }}
                        pageSizeOptions={[5, 10]}
                        checkboxSelection
                      />
                    </div>
                  ) : (
                    <Alert severity="warning">Nada foi encontrado</Alert>
                  )}
                  <Button variant="outlined" startIcon={<DeleteIcon />}>
                    Delete
                  </Button>
                </div>
              </TabPanel>
              <TabPanel value="2">
              	<div className="alunos-painel-interno">
					<Stack direction={"row"} spacing={2}>
						<TextField id="outlined-basic" label="CPF" size="small"/>
						<TextField id="outlined-basic" label="NOME" variant="outlined"  size="small"/>
						<TextField id="outlined-basic" label="EMAIL" variant="outlined"  size="small"/>
						<TextField id="outlined-basic" label="SENHA" variant="outlined"  size="small"/>
						<TextField id="outlined-basic" label="NASCIMENTO" variant="outlined"  size="small"/>
						<TextField id="outlined-basic" label="UNIDADE_ID" variant="outlined"  size="small"/>
						<Button variant="contained" startIcon={<AddIcon/>}>Adicionar</Button>
					</Stack>
				</div>
              </TabPanel>
              <TabPanel value="3">Item Three</TabPanel>
            </TabContext>
          </Box>
          <Link to={"/painel/"}>
            <Button variant="contained" startIcon={<ArrowBackIcon />}>
              Voltar
            </Button>
          </Link>
        </ThemeProvider>
      </PainelBox>
    </div>
  );
}

export default Alunos;
