#  Analizador Sintáctico CYK (Cocke–Younger–Kasami)

Este proyecto implementa el **algoritmo CYK (Cocke–Younger–Kasami)** en Python, diseñado para analizar expresiones aritméticas simples basadas en una **gramática libre de contexto (GLC)** convertida a **Forma Normal de Chomsky (FNC)**.  
El objetivo principal es **verificar la pertenencia de una cadena a un lenguaje** y comparar su rendimiento frente al algoritmo predictivo LL(1).

---

## ¿Qué es el algoritmo CYK?

El **algoritmo CYK (Cocke–Younger–Kasami)** es un **analizador sintáctico ascendente** que verifica si una cadena puede ser generada por una gramática libre de contexto.  
Funciona únicamente con **gramáticas en Forma Normal de Chomsky (FNC)**, donde cada producción tiene una de las siguientes formas:

- `A → BC` (dos no terminales)  
- `A → a` (un terminal)

El CYK usa **programación dinámica**, construyendo una **tabla triangular** que representa todas las combinaciones posibles de subcadenas derivables de la entrada.

---

##  Características principales

-  Análisis **ascendente** (bottom-up)
-  Basado en **programación dinámica**
-  Compatible únicamente con **FNC**
-  Permite **verificar pertenencia** de una cadena al lenguaje
-  Ideal para gramáticas complejas y validación formal

---

##  Gramática utilizada (en FNC)

Esta gramática representa **expresiones aritméticas** con suma, resta, multiplicación, división y paréntesis, transformada a **Forma Normal de Chomsky** para su uso en el algoritmo.
<img width="149" height="226" alt="image" src="https://github.com/user-attachments/assets/95bd5d5f-d352-4828-a7a2-35fe0293d12a" />

> Nota: cada producción cumple con las reglas de la FNC:  
> - Solo produce **dos no terminales (A → BC)** o **un terminal (A → a)**.  
> - No hay epsilon-producciones (excepto las eliminadas durante la normalización).  
> - No hay recursión izquierda.

---

##  Funcionamiento del algoritmo CYK

El algoritmo CYK trabaja de forma ascendente:

1. **Lee la gramática** desde un archivo externo (`gramatica_cyk.txt`).  
2. **Inicializa una tabla triangular**, donde cada celda `[i][j]` representa los no terminales que pueden generar la subcadena `w[i:j]`.  
3. Llena la primera fila con las reglas que generan cada símbolo terminal.  
4. Iterativamente combina subcadenas más pequeñas para construir subcadenas más grandes.  
5. La cadena se acepta si el símbolo inicial `S` aparece en la celda superior de la tabla.

---

##  Ejemplo de entrada y salida

**Entrada:**
num + num * num

**Salida:**
Cadena aceptada por la gramática.
Tiempo de ejecución: 1.966458e-04 segundos

---

##  Medición de rendimiento

Se realizaron pruebas con cadenas de diferente longitud (n = 10, 50, 100, 200).  
Cada caso se ejecutó varias veces para obtener un promedio y desviación estándar.

<img width="333" height="85" alt="image" src="https://github.com/user-attachments/assets/b5dc43a3-b05f-47f6-9e8e-24c7184ea5e2" />


Los tiempos se muestran en **notación científica** para mantener claridad y permitir comparaciones directas con el parser LL(1).

---

##  Interpretación de resultados

- El **tiempo de ejecución crece exponencialmente** con respecto al tamaño de la entrada.  
- Esto se debe a la **complejidad cúbica del algoritmo**:  
  \[
  \text{Complejidad temporal} = O(n^3)
  \]
- La variación en los tiempos (desviación estándar) es mayor, reflejando la naturaleza combinatoria del método.  
- Aunque **más preciso y general**, CYK es **considerablemente más lento** que LL(1).

---

## Conclusiones parciales

- El algoritmo **CYK** es una herramienta poderosa para **verificar pertenencia** en gramáticas libres de contexto.  
- Su **principal ventaja** es que puede manejar gramáticas que **no son LL(1)** o incluso ambiguas.  
- Su **principal desventaja** es el **alto costo computacional**, especialmente con entradas largas.  
- En este proyecto se comprobó experimentalmente que CYK tiene un crecimiento cúbico del tiempo, mientras que LL(1) es lineal.  
- Los resultados de las mediciones confirman las diferencias teóricas entre ambos enfoques.

---





