
import sys
import time
import random
import numpy as np

class AnalizadorCYK:
    def __init__(self, archivo_gramatica):
        self.gramatica = self._leer_gramatica(archivo_gramatica)
        self.simbolo_inicial = list(self.gramatica.keys())[0]

    def _leer_gramatica(self, archivo):
        gramatica = {}
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or "->" not in linea:
                    continue
                izquierda, derecha = linea.split("->")
                izquierda = izquierda.strip()
                producciones = [p.strip().split() for p in derecha.split("|")]
                gramatica[izquierda] = producciones
        return gramatica

    def analizar(self, cadena):
        n = len(cadena)
        P = [[set() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for A, producciones in self.gramatica.items():
                for prod in producciones:
                    if len(prod) == 1 and prod[0] == cadena[i]:
                        P[i][i].add(A)

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    for A, producciones in self.gramatica.items():
                        for prod in producciones:
                            if len(prod) == 2:
                                B, C = prod
                                if B in P[i][k] and C in P[k + 1][j]:
                                    P[i][j].add(A)

        return self.simbolo_inicial in P[0][n - 1]



# FUNCIONES AUXILIARES PARA MEDIR EL RENDIMIEnto
def generar_cadena(n):
    simbolos = [str(random.randint(0, 9)) for _ in range(n)]
    ops = ['+', '-', '*', '/']
    expresion = []
    for s in simbolos:
        expresion.append(s)
        if random.random() < 0.5:
            expresion.append(random.choice(ops))
    return [x for x in expresion if x != '']

def medir_tiempo(funcion, repeticiones=10):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return np.mean(tiempos), np.std(tiempos)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python parser_cyk.py gramatica_cyk.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    analizador = AnalizadorCYK(archivo)

    for n in [10, 50, 100, 200]:
        entrada = generar_cadena(n)
        promedio, desviacion = medir_tiempo(lambda: analizador.analizar(entrada))
        print(f"n={n:4} | CYK: {promedio:.6e} ± {desviacion:.1e} s")

    print("\n✅ Pruebas completadas para Analizador CYK.")
