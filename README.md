# aihelp

Herramienta CLI desarrollada en Python para analizar la estructura y el contenido de proyectos de software.

## Funcionalidades

- `context --tree`: muestra el árbol de directorios y archivos del proyecto.
- `context --files`: muestra el contenido de los archivos.
- `ignore`: genera un fichero `.aihelpignore` para personalizar las exclusiones.

## Instalación

Requisitos: Python 3.10 o superior.

```bash
pipx install .
```

## Uso

```bash
# Mostrar ayuda
aihelp --help

# Mostrar estructura del proyecto
aihelp context --tree

# Mostrar contenido de los archivos
aihelp context --files

# Mostrar estructura y contenido
aihelp context --tree --files

# Crear fichero de exclusiones
aihelp ignore
```

Para sobrescribir un fichero `.aihelpignore` existente:

```bash
aihelp ignore --force
```

## Desarrollo

El proyecto utiliza Python y setuptools. La configuración del paquete y sus dependencias se encuentran en `pyproject.toml`.

