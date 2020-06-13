

# Controle Financeiro para Restaurante

[![Python Version][python-image]][python-url]
[![Django Version][django-image]][django-url]

Sistema web para abertura e fechamento de caixa, cadastro de mercadorias, fornecedores e notas fiscais, um maior controle automatizado para compreender a saúde do restaurante.

## Instalação do Python e Pip

Linux(Debian, Ubuntu):

```sh
$ sudo apt install python3-dev python3-pip
```

Windows:

- [Python](https://dicasdepython.com.br/como-instalar-o-python-no-windows-10/)
- [Pip](https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/)

Geralmente quando instalar o python no Windows, também instalará o Pip, mas caso o comando dele não seja reconhecido no terminal, utilize o segundo link para fazer funcionar.


## Preparando o projeto

Baixe o projeto ou dê `git clone` e entre no diretório.

Linux:

Criando o ambiente virtual:

```sh
$ python3 -m venv /venv
$ source venv/bin/activate  # Vai ficar (venv) antes do usuário no terminal
```

Agora instale as dependências:

```sh
$ pip install -r requirements.txt
```

Está pronto, mas antes de subir o servidor dê o comando do Django `collectstatic`, para instalar arquivos estáticos de algumas dependências:

```sh
$ python3 manage.py collectstatic
```

Windows(cmd):

Ative o ambiente virtual:

```sh
c:\> python -m venv c:\\path\\to\\myenv   # pode ser também 'py' ao invés de 'python'
c:\> venv\\Scripts\\activate.bat  # Vai ficar (venv) antes do usuário no terminal
```

Agora instale as dependências:

```sh
c:\> pip install -r requirements.txt
```

Utilize este comando para finalizar:

```sh
c:\> python manage.py collectstatic  # ou 'py' ao invés de 'python'
```


## Subir servidor local

##### Variáveis de ambiente:

Primeiro, copie o arquivo __./caixa/.env.example__ com o nome de apenas `.env` e verifique se os valores das variáveis de ambiente estão corretos. 

##### Runserver

Será necessário dois terminais, um para o django e o outro para o Vue.

```sh
cd frontend
npm run serve
```

Agora no outro terminal. Caso não esteja no ambienten virtual(venv), entre para dar o comando:

```sh
python manage.py runserver
```

Agora vá no navegador e coloque: `localhost:8000` 

## Requirements.txt

- Django==3.0.7
- djangorestframework==3.11.0
- mysqlclient==1.4.6
- python-dotenv==0.13.0
- django-adminlte3==0.1.6


## Contribuidores

* **Fábio Sales** - [fsalesalmeida](https://github.com/fsalesalmeida)
* **Felipe Ramos** - [Feliperc7](https://github.com/Feliperc7)
* **Henrique Berg** - [DoppelStrix](https://github.com/DoppelStrix)
* **Matheus Mazoni** - [MMazoni](https://github.com/MMazoni)


[python-image]: https://img.shields.io/badge/python-v3.7-blue
[python-url]: https://www.python.org/
[django-image]: https://img.shields.io/badge/django-v3.0.7-green
[django-url]: https://www.djangoproject.com/
