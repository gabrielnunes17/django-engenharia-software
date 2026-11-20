# Sistema de Biblioteca

Projeto acadêmico desenvolvido como atividade da disciplina de Engenharia de Software da Faculdade Senac Pernambuco. O projeto usa Django e apresenta um protótipo inicial de um sistema relacionado a uma biblioteca.

## Funcionalidades atuais

- Página inicial com formulário visual de login (`/`).
- Página Sobre com informações gerais sobre o sistema (`/sobre/`).
- Navegação entre as páginas.

O formulário de login ainda não autentica usuários, e funcionalidades como catálogo e empréstimos não estão implementadas.

## Tecnologias

- Python
- Django 6.1.3
- SQLite

As dependências Python estão listadas em `requirements.txt`.

## Como executar

### Windows (PowerShell)

Na pasta raiz do projeto, crie e ative um ambiente virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências e prepare o banco de dados:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

Inicie o servidor de desenvolvimento:

```powershell
python manage.py runserver
```

Abra <http://127.0.0.1:8000/> no navegador. A página Sobre está em <http://127.0.0.1:8000/sobre/>.

### Linux ou macOS

Na pasta raiz do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Estrutura principal

```text
cadastro/
├── static/                 # CSS e imagens
├── templates/cadastro/     # Templates das páginas
├── urls.py                 # Rotas do app
└── views.py                # Views das páginas
sistema/
└── settings.py             # Configurações do Django
manage.py                   # Comandos de gerenciamento
requirements.txt            # Dependências Python
```
