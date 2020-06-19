# thepost
Sistema de blog/news site baseado em Django


# Instalação
## Requisitos
- pipenv (https://github.com/pypa/pipenv)

## Instalação
- ```pipenv install```

## Configuração
Crie um arquivo ```.env``` e edite de acordo com as suas necessidades, ex:
```bash
DATABASE_URL=postgres://thepost@localhost/thepost
ALLOWED_HOSTS=127.0.0.1,thepost.exemplo.com.br
DEBUG=false
```

Crie o banco de dados e os arquivos estáticos:
```bash
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic
```

Crie um usuário administrador:
```bash
pipenv run python manage.py createsuperuser
```

Vá até ```/admin/``` para logar com seu usuário admin.
