# Projeto - Módulo de Conteinerização - Ada Devops

# Sobre
Esse projeto é do curso de Devops da Ada, do módulo de conteinerização ministrado pela professora Thayse Frankenberger. Com o objetivo de colocar em prática a criação de imagens e contêineres, foi desenvolvido uma aplicação com banco de dados, seguindo os requisitos abaixo.


## Requisitos
- Todo o conteúdo do projeto precisa estar no GitHub, isso inclui os arquivos do docker, links do Docker Hub e documentação;
- O projeto precisa estar público;
- Possuir duas imagens próprias, sendo uma de uma aplicação e outra de um banco de dados;
- A aplicação precisa enviar dados para o banco de dados por obrigatório;
- As imagens precisam estar no Docker Hub;
- É necessário que seja feito o uso de docker compose;
- Os contêineres precisam se comunicar e o contêiner do banco precisa ter um volume do tipo named;
- No docker compose o banco de dados precisa subir antes da aplicação;
- É necessário que tenha documentação do uso das imagens, da aplicação e de pontos que você julgar importante;


## Docker Hub:
- Aplicação Flask: https://hub.docker.com/repository/docker/naiie/ada_docker_app/general
- Banco de dados: https://hub.docker.com/repository/docker/naiie/ada_docker_db/general

# Descrição
Este projeto é uma aplicação web "Chamada online" que salva no banco os nome de cada pessoa que preencher o campo informado. Feito utilizando o framework Flask e o banco de dados PostgreSQL.

# Instalação

## Pré-requisito:
É necessário ter o Docker e Docker Compose instalado para que possa executar o projeto.
- [Instalação do Docker](https://docs.docker.com/engine/install/)
- [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

## Clonar repositório

Para clonar o repositório você ser baixando via interface github diretamente no seu computador ou via html via comando `git clone <url_repositorio>`.

```
git clone https://github.com/naiieandrade/ada_docker.git
```

Entra na pasta do projeto
```
cd ada_docker
```
Para fazer a criação das imagens é preciso dar um build 
```
docker-compose build
```
Para subir as contêineres segue o comando do docker-compose
```
docker-compose up
```

A aplicação vai estar rodando em [http://localhost:5000/](http://localhost:5000/)

Ao informar o seu nome na aplicação de Chamada online, será possível ver no banco todos os nomes informados.

## Banco de dados

Para acessar o banco de dados é possível via bash do contêiner do banco de dados:
```
docker exec -t ada_docker_db_1 bash
```

Depois que entrar no bash
```
psql -U user_ada -d db_ada
```

Para ver os nomes na tabela "Dados", digite
```
select * from Dados;
```

E para sair do banco digite `\q`.


Para derrubar os contêineres
```
docker-compose down
```