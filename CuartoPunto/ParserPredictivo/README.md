# Analizador Sintáctico Predictivo LL(1)

Este proyecto implementa un **parser predictivo LL(1)** en Python, diseñado para analizar expresiones aritméticas simples basadas en una **gramática libre de contexto (GLC)**.  
El objetivo principal es **validar la correcta aplicación del algoritmo LL(1)** y medir su rendimiento frente a otros métodos de análisis sintáctico, como el algoritmo CYK.

---

##  ¿Qué es un parser LL(1)?

Un **parser LL(1)** es un tipo de **analizador sintáctico descendente predictivo** que lee la entrada **de izquierda a derecha (L)** y produce la derivación **más a la izquierda (L)** usando **una sola mirada de anticipación (1)**.  
En otras palabras, analiza una cadena carácter por carácter prediciendo qué producción aplicar en cada paso sin necesidad de retroceder.

---

##  Características principales

-  Lectura izquierda a derecha (Left-to-right)
-  Derivación más a la izquierda (Leftmost derivation)
-  Una sola mirada de anticipación (1 lookahead)
-  Basado en **tablas predictivas LL(1)**
-  Sin recursión izquierda
-  Ideal para compiladores, analizadores de expresiones y evaluadores aritméticos

---

##  Gramática utilizada

La gramática utilizada describe expresiones aritméticas con suma, resta, multiplicación, división y paréntesis.  
Es una **gramática libre de recursión izquierda** y adecuada para un parser LL(1):

<img width="367" height="102" alt="image" src="https://github.com/user-attachments/assets/7f1b35b2-10f5-445d-b6ab-3e13970b6049" />


###  Justificación de que es LL(1)

Esta gramática cumple con las condiciones para ser LL(1):

1. **No tiene recursión izquierda**, ya que las producciones nunca comienzan con el mismo no terminal (por ejemplo, `E → E + T` fue reemplazada por `E → T Ep`).
2. **Está factorizada a la izquierda**, es decir, no hay ambigüedad entre producciones que comienzan igual.
3. Los conjuntos **PRIMEROS** y **SIGUIENTES** de cada no terminal son disjuntos, lo que asegura que el parser pueda decidir la regla correcta con solo mirar el siguiente símbolo de entrada.

---

##  Funcionamiento del analizador

El analizador predictivo LL(1) se basa en los siguientes pasos:

1. **Cargar la gramática** desde un archivo `.txt` (por ejemplo `gramatica_ll1.txt`).
2. **Construir la tabla predictiva LL(1)** a partir de los conjuntos PRIMEROS y SIGUIENTES.
3. **Analizar una cadena de entrada**, aplicando las producciones de la tabla hasta aceptar o rechazar la cadena.
4. Mostrar mensajes detallados sobre cada paso del análisis.

Ejemplo de entrada aceptada:

num + num * ( num - num )


Salida:

Parser predictivo completado sin errores.
Tiempo de ejecución: 3.302751e-06 segundos


---

##  Medición de rendimiento

Se realizaron pruebas de tiempo para diferentes longitudes de cadenas (n = 10, 50, 100, 200).  
Cada medición se repitió múltiples veces y se calculó el promedio y desviación estándar.

<img width="366" height="83" alt="image" src="https://github.com/user-attachments/assets/7ba1b7f3-41c7-40b5-8720-efab55f35b63" />


Los tiempos se presentan en **notación científica** para mantener uniformidad y legibilidad.

---

##  Interpretación de resultados

- El **crecimiento del tiempo de ejecución** del parser LL(1) es **casi lineal**, lo que refleja la eficiencia esperada de este tipo de analizadores.
- La **baja desviación estándar** muestra que los resultados son consistentes y estables.
- La complejidad temporal es aproximadamente **O(n)**, ya que el analizador revisa cada token una sola vez.

---

##  Conclusiones parciales

- El **parser LL(1)** es **rápido, predecible y eficiente** para lenguajes bien estructurados.
- Gracias a su diseño sin retroceso, es ideal para expresiones matemáticas y lenguajes deterministas.
- Su principal limitación es que **no puede manejar gramáticas ambiguas o con recursión izquierda**.
- Este proyecto demuestra cómo un analizador predictivo puede construirse desde cero, cargando la gramática desde un archivo externo y verificando su desempeño con distintas entradas.

---
## Ejecucion 
```bash
python3 parser_ll1.py gramatica_ll1.txt
```
  



