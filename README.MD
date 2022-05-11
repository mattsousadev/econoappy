# EconoAPY
## API Rest para gerenciamento de finanças pessoais
Esse repositório foi criado com um treino para a utilização das bibliotecas [FastAPI](https://https://fastapi.tiangolo.com/) e [SQLAlchemy](https://https://www.sqlalchemy.org/).

Gerenciador de finanças pessoais onde é possível:
- Cadastrar créditos e débitos;
- Cadastrar operações recorrentes;
- Listar as operações realizadas filtrando por período.

### I. Pré requisitos
Instale os seguintes softwares

- Python 3.8
- PyPi 20.0.2

### II. Instalando dependências
Execute o comando abaixo

`pip install -r requirementes.txt`

### III. Rodando
#### Usando o Uvicorn
Execute o comando abaixo

`uvicorn main:app --reload`

#### Usando o Python
Execute o comando abaixo

`python3 main.py`

Caso rode corretamente, acesse seu navegador no endereço http://localhost:8000/