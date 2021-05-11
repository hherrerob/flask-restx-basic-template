# Flask RESTX basic template

Plantilla para crear servidores de [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/).

---

### Instalación

Clona el Repositorio GitHub

    $ git clone {repo}
    
Instala el paquete de python (es necesario estar dentro del repositorio)

    $ pip install -e .
    
---

### Ejecución del proyecto

El siguiente comando inicia el servidor de desarrollo de Flask (es necesario estar dentro del repositorio):

    $ {project-name}
    
Para desplegar con [gunicorn](https://gunicorn.org/):

    $ gunicorn --workers 4 --bind 0.0.0.0:5000 --timeout 600 run:app

La documentación en swagger se puede encontrar por defecto en [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---
