# Netflix Django

A ideia é construir uma réplica do site da Netflix utilizando o ecossistema do Python.

## Instalação

Seguir as instruções abaixo para criar um projeto em Django

```bash
  pip install django

  django-admin startproject <project_name>

  django-admin startapp <app_name>
```
Para quando houver modificações no banco de dados rodar:

```bash
  python manage.py <makemigrations / migrate>
```

Criar um super user:

```bash
  python manage.py createsuperuser
```