
***

# Lenguaje Crud (ANTLR4 + Python)

Este proyecto implementa un **lenguaje de programación en español** para realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre entidades de datos.  
Fue diseñado con **ANTLR 4** como generador de analizadores y se ejecuta utilizando la **librería de Python ANTLR4 Runtime**.

***

## Características principales

El lenguaje Crud define de forma sencilla la manipulación de entidades mediante palabras clave en español:

- **INICIAR ENTIDAD**: crea una entidad con sus atributos.  
- **OBTENER ENTIDAD**: consulta registros.  
- **CAMBIAR [entidad] CON**: actualiza valores de registros.  
- **BORRAR ENTIDAD**: elimina registros.  
- Las condiciones opcionales se declaran con **CONDICION**.  
- Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`.

Ejemplo:

```text
INICIAR ENTIDAD Persona (nombre TEXTO; edad NUMERO; activo BOOLEANO)
OBTENER ENTIDAD Persona CONDICION edad >= 18
CAMBIAR Persona CON nombre = "Luis"; activo = true CONDICION nombre == "Juan"
BORRAR ENTIDAD Persona CONDICION activo == false
```

***

## Estructura del proyecto

```
/lenguaje-crud
│
├── Crud.g4                 # Archivo con la gramática ANTLR4
├── main.py                 # Programa principal en Python
├── README.md               # Documentación del proyecto
├── Ejemplo.crud
│ 
└── Archivos generados por ANTLR:
    ├── CrudLexer.py
    ├── CrudParser.py
    ├── CrudListener.py
    ├── Crud.tokens
    └── Crud.interp
```

***

## Instalación y ejecución

### 1. Requisitos previos

- **Python 3.9+**
- **Java 11+**
- **ANTLR 4.13 o superior**

Instala el _runtime_ de ANTLR para Python:

```bash
pip install antlr4-python3-runtime
```

### 2. Generar los analizadores

Desde la terminal:

```bash
antlr4 -Dlanguage=Python3 Crud.g4
```

Esto generará archivos *Lexer*, *Parser* y *Listener* necesarios para interpretar el lenguaje.

### 3. Ejecutar el programa

```bash
python main.py Ejemplo.crud
```

El programa imprimirá el **árbol sintáctico** correspondiente al código ejecutado.

***

## Funcionamiento interno

El intérprete Crud se divide en tres componentes generados automáticamente por ANTLR:

1. **Lexer (CrudLexer.py)**  
   Convierte el texto de entrada en *tokens* (palabras clave, identificadores, números, cadenas).

2. **Parser (CrudParser.py)**  
   Usa esos tokens para construir un **árbol sintáctico** con base en las reglas definidas en la gramática `Crud.g4`.

3. **Listener / Visitor (opcional)**  
   Permiten recorrer el árbol para ejecutar acciones, como validar o simular las operaciones CRUD.

El archivo `main.py` usa estos componentes para analizar programas escritos en el lenguaje Crud y mostrar su estructura sintáctica.

***

## Ejemplo de salida

Usando el archivo `Ejemplos/ejemplo1.crud`, el programa mostrará algo como:

```
(programa 
  (instruccion (crear_entidad INICIAR ENTIDAD Persona ( ... )))
  (instruccion (consultar_entidad OBTENER ENTIDAD Persona CONDICION ...))
  (instruccion (modificar_entidad CAMBIAR Persona CON ...))
  (instruccion (eliminar_entidad BORRAR ENTIDAD Persona CONDICION ...))
)
```

***

## Cómo extender el lenguaje

Puedes ampliar el lenguaje agregando nuevas reglas a `Crud.g4`, por ejemplo:

- Soporte para comandos de impresión (`MOSTRAR`).
- Tipos de dato adicionales, como `FECHA` o `EMAIL`.
- Validaciones de integridad o ejecución en memoria simulada.

Cada vez que se edita la gramática, recuerda regenerar los analizadores con:

```bash
antlr4 -Dlanguage=Python3 Crud.g4
```

***

## Créditos

Proyecto desarrollado con **ANTLR4** y **Python** como parte de un ejercicio de lenguajes de programación.  
Basado en la gramática original de CRUD en español y adaptado para un entorno académico y demostrativo.

***

