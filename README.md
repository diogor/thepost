# thepost
Sistema de blog/news site baseado em Django


# Instalação
## Requisitos
- poetry (https://python-poetry.org/docs/)

## Instalação
- ```poetry install```

## Configuração
Crie um arquivo ```.env``` e edite de acordo com as suas necessidades, ex:
```bash
DATABASE_URL=postgres://thepost@localhost/thepost
ALLOWED_HOSTS=127.0.0.1,thepost.exemplo.com.br
DEBUG=false
CACHE_SECONDS=120
```

Crie o banco de dados e os arquivos estáticos:
```bash
poetry run python manage.py migrate
poetry run python manage.py collectstatic
```

Crie um usuário administrador:
```bash
poetry run python manage.py createsuperuser
```

Vá até ```/admin/``` para logar com seu usuário admin.
