# Carros
Projeto de carros, Sistema web possibilitando o registro de carros, onde conseguimos realizar ações com carros e marcas, além disso tem controle de estoque de veiculos.

## Instalação
Faça o clone deste projeto
```bash
  git clone https://github.com/Ramonlleopoldo/projeto-carros.git
```
Crie um ambiente virtual
```bash
  python -m venv venv
```
Ative o ambiente virtual
```bash
  ./venv/Scripts/activate
```
Instalaçao das dependencias do projeto
```bash
  pip install -r requirements.txt
```
Realize um migrate para criação das tabelas
```bash
  python manage.py migrate
```
Crie um SuperUser (Você tera que criar um usuario, email e senha)
```bash
  python manage.py createsuperuser
```
Rode o projeto (O projeto abrirá na porta 8000)
```bash
  python manage.py runserver
```

## Demonstração
Este é um exemplo do projeto
![Descrição do GIF](./files_readme/desktop.gif)

### Referências
Este projeto foi fornecido pela pycodebr no curso django master, onde obtive grande aprendizado sobre Django.
