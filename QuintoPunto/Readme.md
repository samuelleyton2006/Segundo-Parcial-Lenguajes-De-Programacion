#  Analizador Descendente Recursivo con Emparejamiento

##  Descripción general

Este proyecto implementa un **analizador sintáctico descendente recursivo**, capaz de procesar gramáticas libres de contexto **no recursivas por la izquierda**, calculando además los conjuntos **PRIMEROS**, **SIGUIENTES** y **PREDICCIÓN** de cada regla gramatical.

El objetivo es mostrar cómo un **algoritmo de emparejamiento** permite recorrer una cadena de entrada y verificar si pertenece al lenguaje generado por una gramática dada.

---

##  ¿Cómo funciona?

El programa sigue las siguientes etapas principales:

### 1️ Lectura de la gramática

Se lee un archivo `gramatica.txt` con producciones del tipo:


<img width="209" height="108" alt="image" src="https://github.com/user-attachments/assets/38e0d1c0-4759-43fb-8ec4-cf96e47d3b4e" />


Cada línea representa una **regla de producción**, y el símbolo `ε` representa la cadena vacía.

---

### 2️⃣ Cálculo de conjuntos teóricos

El programa calcula automáticamente los siguientes conjuntos:

- **PRIMEROS(X):** terminales que pueden aparecer al inicio de las cadenas derivadas de X.  
- **SIGUIENTES(X):** terminales que pueden seguir a X en alguna derivación.  
- **PREDICCIÓN(A → α):** conjunto de terminales que permiten seleccionar la producción A → α en el análisis.

Estos conjuntos se imprimen en pantalla y son la base para construir el **analizador predictivo**.

---

### 3️⃣ Emparejamiento y análisis descendente recursivo

Aquí entra en juego el **algoritmo de emparejamiento**, que es la parte práctica del ejercicio.

La idea es simple:
- El analizador **lee el token actual de la entrada**.
- Si coincide con el símbolo esperado, **consume (avanza)** el token.
- Si no coincide, **reporta un error sintáctico**.

Cada **no terminal** de la gramática se procesa con una función recursiva que consulta la **tabla de predicción** y selecciona la producción correcta.

---

### 4️⃣ Verificación de la cadena

Finalmente, el programa intenta reconocer toda la cadena de entrada.  
Si todos los tokens se consumen correctamente y se llega al final (símbolo `$`), la cadena se acepta.

Ejemplo:

```bash
python analizador.py gramatica.txt "num + num * num"
```
Salida:

<img width="461" height="539" alt="image" src="https://github.com/user-attachments/assets/54027230-816a-4870-9490-d4153596ce3c" />

<img width="357" height="605" alt="image" src="https://github.com/user-attachments/assets/98e2bcc9-867a-4972-8e7e-a0b014fea87c" />




