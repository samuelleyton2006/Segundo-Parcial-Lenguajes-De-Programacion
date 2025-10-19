
import sys
import time
import random
import numpy as np

class AnalizadorLL1:
    def __init__(self, archivo_gramatica):
        self.gramatica = self._leer_gramatica(archivo_gramatica)
        self.simbolo_inicial = list(self.gramatica.keys())[0]
        self.tokens = []
        self.indice = 0

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
        self.tokens = cadena + ["$"]
        self.indice = 0
        resultado = self._analizar_no_terminal(self.simbolo_inicial)
        return resultado and self.tokens[self.indice] == "$"

    def _token_actual(self):
        return self.tokens[self.indice]

    def _consumir(self, token):
        if self._token_actual() == token:
            self.indice += 1
            return True
        return False

    def _analizar_no_terminal(self, simbolo):
        if simbolo not in self.gramatica:
            if self._token_actual() == simbolo or (
                simbolo == "num" and self._token_actual().isdigit()
            ):
                self.indice += 1
                return True
            return False

        for produccion in self.gramatica[simbolo]:
            pos_backup = self.indice
            exito = True
            for s in produccion:
                if s == "ε":
                    continue
                if not self._analizar_no_terminal(s):
                    exito = False
                    break
            if exito:
                return True
            self.indice = pos_backup
        return False 

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


# =====================================================
# EJECUCIÓN PRINCIPAL
# =====================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python parser_ll1.py gramatica.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    analizador = AnalizadorLL1(archivo)

    for n in [10, 50, 100, 200]:
        entrada = generar_cadena(n)
        promedio, desviacion = medir_tiempo(lambda: analizador.analizar(entrada))
        print(f"n={n:4} | LL(1): {promedio:.6e} ± {desviacion:.1e} s")

    print("\n✅ Pruebas completadas para Analizador LL(1).")
