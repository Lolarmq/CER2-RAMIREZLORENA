# Patrimonio Vivo

## Descripción del proyecto

Patrimonio Vivo es una aplicación web desarrollada para la Fundación Patrimonio Vivo, cuyo objetivo es identificar, documentar y difundir lugares de interés patrimonial de Chile.

La plataforma permite a los visitantes explorar lugares patrimoniales, consultar sus características y conocerlos según distintas categorías. Además, cuenta con un área de gestión para usuarios autorizados.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5.3.8

## Estructura del proyecto

- `PatrimonioVivo/`: configuración principal del proyecto Django.
- `patrimonio/`: aplicación principal.
- `patrimonio/models.py`: modelos de la base de datos.
- `patrimonio/views.py`: vistas de la aplicación.
- `patrimonio/templates/`: plantillas HTML.
- `patrimonio/static/`: archivos CSS y recursos estáticos.
- `manage.py`: archivo para ejecutar comandos de Django.

## Instalación y configuración

### 1. Requisitos previos

Tener instalado Python y pip.

### 2. Instalar Django

Abrir una terminal en la carpeta principal del proyecto y ejecutar:

```bash
pip install Django==6.1.2
```

### 3. Preparar la base de datos

Ejecutar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear un usuario administrador

Ejecutar:

```bash
python manage.py createsuperuser
```

Seguir las instrucciones para crear las credenciales del administrador.

### 5. Ejecutar el servidor

Ejecutar:

```bash
python manage.py runserver
```

Abrir el navegador e ingresar a:

`http://127.0.0.1:8000/`

## Funcionalidades principales

- Página de inicio.
- Catálogo dinámico de lugares patrimoniales.
- Consulta de detalles de cada lugar.
- Visualización y filtrado por categorías.
- Administración de categorías y lugares mediante Django Admin.
- Inicio y cierre de sesión.
- Área de gestión para usuarios autenticados.
- Registro y edición de lugares patrimoniales mediante permisos.

## Administración

Para acceder al panel de administración:

`http://127.0.0.1:8000/admin/`

Es necesario contar con un usuario administrador.

## Autora

Lorena Ramírez

Proyecto desarrollado para el Certamen N°2 de Taller de Lenguaje de Programación.