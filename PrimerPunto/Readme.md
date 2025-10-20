Aquí tienes un README listo para GitHub que explica el funcionamiento del lenguaje CRUD basado en la gramática en español que diseñamos, junto con detalles de la gramática y uso general. Este texto es ideal para documentar tu proyecto en un repositorio.

***

# Lenguaje CRUD en español - Gramática y Analizador

Este proyecto define un lenguaje de programación simple en español para operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre bases de datos. Se creó una gramática única para este lenguaje con sintaxis en español, que luego puede ser implementada con herramientas como ANTLR4 o BISON para análisis sintáctico.

***

## Funcionamiento del lenguaje

El lenguaje permite manipular entidades de bases de datos mediante comandos en español claros y fáciles de entender. Los comandos principales son:

- **INICIAR ENTIDAD**: Define una nueva entidad (tabla) con atributos y tipos.
- **OBTENER ENTIDAD**: Consulta registros de una entidad, con opción a incluir filtros.
- **CAMBIAR [entidad] CON**: Modifica atributos de registros de una entidad condicionados.
- **BORRAR ENTIDAD**: Elimina registros de una entidad con filtro opcional.

Los filtros se especifican con la palabra clave `CONDICION` seguida de expresiones comparativas para identificar qué registros afectan los comandos.

***

## Gramática del lenguaje

La gramática está escrita para definir la estructura sintáctica que debe seguir cada comando. Aquí un resumen de las reglas principales:

```
programa          ::= instrucciones*

instrucciones     ::= instruccion | instrucciones instruccion

instruccion       ::= crear_entidad
                   | consultar_entidad
                   | modificar_entidad
                   | eliminar_entidad

crear_entidad     ::= "INICIAR" "ENTIDAD" nombre_entidad "(" lista_atributos ")"
lista_atributos   ::= atributo (";" atributo)*
atributo          ::= nombre_atributo tipo_dato

consultar_entidad ::= "OBTENER" "ENTIDAD" nombre_entidad [ "CONDICION" expresion_condicion ]

modificar_entidad ::= "CAMBIAR" nombre_entidad "CON" lista_modificaciones [ "CONDICION" expresion_condicion ]
lista_modificaciones ::= modificacion (";" modificacion)*
modificacion      ::= nombre_atributo "=" valor

eliminar_entidad  ::= "BORRAR" "ENTIDAD" nombre_entidad [ "CONDICION" expresion_condicion ]

expresion_condicion ::= nombre_atributo operador_comparacion valor
operador_comparacion ::= "==" | "!=" | "<" | ">" | "<=" | ">="

valor            ::= texto | numero | nombre_atributo

tipo_dato        ::= "NUMERO" | "TEXTO" | "DECIMAL" | "BOOLEANO"
```

***

## Características destacadas

- Sintaxis completamente en español, desde palabras clave hasta tipos de datos.
- Uso de `;` para separar atributos/modificaciones en listas.
- Condiciones expresadas con `CONDICION` y operadores que incluyen `==` para igualdad.
- Diseñado para ser claro y legible, fácil de implementar en analizadores sintácticos.

***

## Implementación

Este lenguaje puede ser implementado con herramientas como:

- **ANTLR4**: Genera analizadores en múltiples lenguajes usando la gramática ANTLR.
- **BISON y FLEX**: Para análisis sintáctico y léxico en C/C++.

Se incluyen archivos de gramática en ANTLR4 y BISON preparados para hacer el análisis de programas escritos en este lenguaje.

***

## Uso y pruebas

Para probar el lenguaje, escribe comandos con esta sintaxis. Algunos ejemplos válidos:

```
INICIAR ENTIDAD Persona (nombre TEXTO; edad NUMERO; activo BOOLEANO)
OBTENER ENTIDAD Persona CONDICION edad >= 18
CAMBIAR Persona CON nombre = "Luis"; activo = true CONDICION nombre == "Juan"
BORRAR ENTIDAD Persona CONDICION activo == false
```

***

## Contribuciones y mejoras

Este proyecto es una base para aprender diseño e implementación de lenguajes de programación con gramáticas personalizadas. Se pueden agregar características como manejo de errores, tipos más complejos o integración con bases de datos reales.

***

Este README te ayudará a documentar claramente tu proyecto y explicar su diseño y uso con un lenguaje CRUD en español basado en una gramática customizada. Si deseas, puedo ayudarte a generar los archivos de ejemplo o código para pruebas.

Sources
[1] Lenguaje de programación de código abierto para latinos ... https://github.com/lenguaje-latino/latino
[2] fernandocar86/seminario-gramaticas-formales https://github.com/fernandocar86/seminario-gramaticas-formales
[3] lenguaje-de-programacion https://github.com/topics/lenguaje-de-programacion?l=c
[4] CarlosSanabriaM/Compilador https://github.com/CarlosSanabriaM/Compilador
[5] Jocagi/ProyectoLFYA: Proyecto del curso Lenguajes ... https://github.com/Jocagi/ProyectoLFYA
[6] Lunfardo es un lenguaje de programación esotérico ... https://github.com/WhiteHeadbanger/Lunfardo
[7] PabloMuralles/Compiladores https://github.com/PabloMuralles/Compiladores
[8] Truco para Documentación Rápida en GitHub https://www.tiktok.com/@midudev/video/7521379381806173462
[9] Matiascba27/guias-y-recursos-programacion https://github.com/Matiascba27/guias-y-recursos-programacion
[10] 5 Markdown - lenguaje de marcado https://gf0604-procesamientodatosgeograficos.github.io/2023-i/05-markdown.html
