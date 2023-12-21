# O Projeto
A ideia do projeto é ensinar por meio prático o funcionamento de um sistema administrativo de uma escola, como funciona o back-end, o front-end e além de tudo isso
como funciona o o banco de dados criado para o projeto

![Escola por dentro](https://static.mundoeducacao.uol.com.br/mundoeducacao/2022/03/dia-escola.jpg)

## Tecnologias
As tecnologias empregadas são:
- Python3(Flask e mysqlconnector...)
- MySQL
- ReactJS

## Funcionamento do banco
O banco de dados foi construido apartir da ideia de que a escola contenha 2 tipos de funcionários dividos em tabelas, sendo eles os:
- Coordenadores
- Professores

Além disso foi divido em tabela os boletins, as unidades da escola(supondo que seja uma rede de escolas), a solicitação de segunda chamada das provas e solicitação de reunião, como na foto abaixo:

![imagem](bancorep.png)


## Como rodar o projeto?

Os requisitos para utilizar o [setup.py](/Back-End/api/setup.py) é preciso a versão *3.12* do Python e os requisitos de bibliotecas estão em  **/back-end/config/requirements.txt**, agora para criar o banco e rodar na máquina é *necessário a versão 8.0 ou superior do MySQL*, e o [arquivo para configurar](/back-end/config/banco/script.sql) está em **/back-end/config/banco/script.sql**.