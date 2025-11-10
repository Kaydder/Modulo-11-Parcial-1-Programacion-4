# Sistema de Registro de Presupuesto

## Objetivo
Desarrollar una aplicación de línea de comandos en Python 3 que permita gestionar artículos dentro de un sistema de registro de presupuesto.  
El programa ofrece funcionalidades para registrar, buscar, editar, eliminar y listar artículos de forma persistente utilizando archivos JSON.

---

## Descripción General
Este proyecto permite llevar un control básico de los insumos o componentes de un presupuesto, guardando los datos localmente en un archivo `articulos.json`.  
Cada artículo incluye la siguiente información:

- ID (generado automáticamente)
- Nombre
- Categoría
- Cantidad
- Precio unitario
- Descripción

El sistema funciona completamente desde la terminal, con un menú interactivo.

---

## Funcionalidades

| Opción | Descripción |
|:------:|:-------------|
| 1 | Registrar un nuevo artículo |
| 2 | Buscar artículos por nombre o categoría |
| 3 | Editar la información de un artículo existente |
| 4 | Eliminar un artículo |
| 5 | Listar todos los artículos registrados |
| 6 | Salir del sistema |

---

## Estructura del Proyecto

