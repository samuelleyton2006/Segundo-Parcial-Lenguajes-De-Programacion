# Comparación de Parsers: LL(1) vs CYK

Este repositorio contiene la implementación de **dos analizadores sintácticos** basados en diferentes enfoques de análisis de gramáticas libres de contexto:

1. **Parser LL(1)** → Análisis descendente predictivo  
2. **Parser CYK (Cocke–Younger–Kasami)** → Análisis ascendente basado en programación dinámica

El objetivo principal del proyecto es **comparar el rendimiento de ambos métodos** al procesar expresiones aritméticas de diferentes longitudes.

---

##  Descripción general del proyecto

Cada analizador utiliza una **gramática diferente** para representar las operaciones aritméticas básicas (+, −, ×, ÷, paréntesis).  
Ambos cargan su gramática desde un archivo `.txt`, procesan una serie de cadenas de prueba y miden su **tiempo de ejecución promedio y desviación estándar**.

Posteriormente, los resultados se analizan y visualizan mediante una **gráfica comparativa**.

---

##  Parsers implementados

| Parser | Tipo de análisis | Complejidad | Forma de gramática | Características |
|--------|------------------|--------------|--------------------|-----------------|
| **LL(1)** | Descendente predictivo | O(n) | Libre de recursión izquierda | Rápido y eficiente |
| **CYK** | Ascendente (bottom-up) | O(n³) | Forma Normal de Chomsky (FNC) | Más general, pero lento |

---

##  Resultados experimentales

Los siguientes resultados fueron obtenidos ejecutando ambos parsers con diferentes longitudes de entrada (`n`):

| n | LL(1) (s) | CYK (s) |
|---:|-----------:|-----------:|
| 10 | 2.034110e-05 | 4.792034e-03 |
| 50 | 3.529630e-05 | 4.865007e-02 |
| 100 | 1.958430e-05 | 2.811114e+00 |
| 200 | 3.732080e-05 | 3.009870e+01 |

**Pruebas completadas satisfactoriamente** para ambos analizadores.

---

##  Análisis gráfico
<img width="790" height="490" alt="image" src="https://github.com/user-attachments/assets/53689160-0aa8-4df0-86f8-34570d11a793" />


## Interpretación de resultados

- El parser LL(1) presenta un crecimiento casi lineal respecto al tamaño de la entrada (O(n)).

- El parser CYK muestra un aumento exponencial del tiempo de ejecución (O(n³)), lo que concuerda con su complejidad teórica.

- Para cadenas pequeñas, ambos funcionan sin problemas, pero a medida que n crece, CYK se vuelve significativamente más lento.

- Esta diferencia evidencia que LL(1) es más eficiente para análisis deterministas, mientras que CYK es más versátil para gramáticas complejas o ambiguas.

## Conclusiones finales

- Ambos analizadores cumplen correctamente su función de validar cadenas conforme a su gramática.

- LL(1) es ideal para parsers ligeros, compiladores y expresiones simples.

- CYK, aunque más costoso, garantiza la verificación de pertenencia incluso para gramáticas no LL(1).

- Las mediciones experimentales confirmaron la diferencia entre eficiencia práctica y potencia teórica.

- En términos de rendimiento, LL(1) supera ampliamente a CYK, mientras que CYK ofrece mayor generalidad.
