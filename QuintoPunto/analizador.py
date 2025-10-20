# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

# ------------------------------
# Leer la gramática
# ------------------------------
def leer_gramatica(nombre_archivo):
    gramatica = defaultdict(list)
    simbolo_inicial = None
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if not linea.strip():
                continue
            izquierda, derecha = linea.split("->")
            izquierda = izquierda.strip()
            if simbolo_inicial is None:
                simbolo_inicial = izquierda
            alternativas = derecha.split("|")
            for alt in alternativas:
                gramatica[izquierda].append(alt.strip().split())
    return gramatica, simbolo_inicial

# ------------------------------
# PRIMEROS
# ------------------------------
def calcular_primeros(gramatica):
    primeros = defaultdict(set)

    for nt in gramatica:
        for prod in gramatica[nt]:
            for simbolo in prod:
                if simbolo not in gramatica and simbolo != "ε":
                    primeros[simbolo].add(simbolo)

    cambiado = True
    while cambiado:
        cambiado = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                puede_vacio = True
                for simbolo in prod:
                    if simbolo not in gramatica:
                        antes = len(primeros[nt])
                        primeros[nt].add(simbolo)
                        if len(primeros[nt]) > antes:
                            cambiado = True
                        puede_vacio = False
                        break
                    else:
                        antes = len(primeros[nt])
                        primeros[nt] |= (primeros[simbolo] - {"ε"})
                        if len(primeros[nt]) > antes:
                            cambiado = True
                        if "ε" not in primeros[simbolo]:
                            puede_vacio = False
                            break
                if puede_vacio:
                    if "ε" not in primeros[nt]:
                        primeros[nt].add("ε")
                        cambiado = True
    return primeros

# ------------------------------
# SIGUIENTES
# ------------------------------
def calcular_siguientes(gramatica, inicial, primeros):
    siguientes = defaultdict(set)
    siguientes[inicial].add("$")

    cambiado = True
    while cambiado:
        cambiado = False
        for nt in gramatica:
            for prod in gramatica[nt]:
                for i, simbolo in enumerate(prod):
                    if simbolo in gramatica:
                        beta = prod[i+1:]
                        if beta:
                            primeros_beta = set()
                            vacio = True
                            for b in beta:
                                primeros_beta |= (primeros[b] if b in primeros else {b})
                                if "ε" not in primeros[b]:
                                    vacio = False
                                    break
                            if vacio:
                                antes = len(siguientes[simbolo])
                                siguientes[simbolo] |= siguientes[nt]
                                if len(siguientes[simbolo]) > antes:
                                    cambiado = True
                            antes = len(siguientes[simbolo])
                            siguientes[simbolo] |= (primeros_beta - {"ε"})
                            if len(siguientes[simbolo]) > antes:
                                cambiado = True
                        else:
                            antes = len(siguientes[simbolo])
                            siguientes[simbolo] |= siguientes[nt]
                            if len(siguientes[simbolo]) > antes:
                                cambiado = True
    return siguientes

# ------------------------------
# PREDICCIÓN
# ------------------------------
def calcular_prediccion(gramatica, primeros, siguientes):
    pred = {}
    for nt in gramatica:
        for prod in gramatica[nt]:
            conjunto = set()
            vacio = True
            for s in prod:
                conjunto |= (primeros[s] if s in primeros else {s})
                if "ε" not in (primeros[s] if s in primeros else {s}):
                    vacio = False
                    break
            if vacio:
                conjunto |= siguientes[nt]
            conjunto.discard("ε")
            pred[(nt, tuple(prod))] = conjunto
    return pred

# ------------------------------
# EMPAREJAMIENTO Y ANALIZADOR DESCENDENTE
# ------------------------------
class AnalizadorRecursivo:
    def __init__(self, gramatica, pred, simbolo_inicial):
        self.gramatica = gramatica
        self.pred = pred
        self.simbolo_inicial = simbolo_inicial
        self.tokens = []
        self.pos = 0

    def analizar(self, entrada):
        self.tokens = entrada.split() + ["$"]
        self.pos = 0
        print("\nIniciando análisis sintáctico...\n")
        self._procesar(self.simbolo_inicial)
        if self.tokens[self.pos] == "$":
            print("✅ Cadena aceptada correctamente.")
        else:
            print("❌ Error: Tokens restantes sin procesar:", self.tokens[self.pos:])

    def emparejar(self, esperado):
        actual = self.tokens[self.pos]
        print(f"Emparejando: esperado='{esperado}', actual='{actual}'")
        if actual == esperado:
            self.pos += 1
        else:
            raise SyntaxError(f"Se esperaba '{esperado}' pero se encontró '{actual}'")

    def _procesar(self, simbolo):
        if simbolo not in self.gramatica:
            self.emparejar(simbolo)
        else:
            actual = self.tokens[self.pos]
            for prod in self.gramatica[simbolo]:
                if actual in self.pred[(simbolo, tuple(prod))]:
                    print(f"{simbolo} -> {' '.join(prod)}")
                    for s in prod:
                        if s != "ε":
                            self._procesar(s)
                    return
            raise SyntaxError(f"No hay regla válida para {simbolo} con token '{actual}'")

# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python analizador.py gramatica.txt 'cadena de entrada'")
        sys.exit(1)

    archivo = sys.argv[1]
    entrada = sys.argv[2]
    gramatica, inicial = leer_gramatica(archivo)

    primeros = calcular_primeros(gramatica)
    siguientes = calcular_siguientes(gramatica, inicial, primeros)
    pred = calcular_prediccion(gramatica, primeros, siguientes)

    print("Gramática cargada de:", archivo)
    for nt in gramatica:
        print(nt, "->", [" ".join(p) for p in gramatica[nt]])

    print("\n--- PRIMEROS ---")
    for nt in primeros:
        print(f"PRIMEROS({nt}) = {primeros[nt]}")

    print("\n--- SIGUIENTES ---")
    for nt in siguientes:
        print(f"SIGUIENTES({nt}) = {siguientes[nt]}")

    print("\n--- PREDICCIÓN ---")
    for (nt, prod), conj in pred.items():
        print(f"PRED({nt} -> {' '.join(prod)}) = {conj}")

    analizador = AnalizadorRecursivo(gramatica, pred, inicial)
    analizador.analizar(entrada)
