import sys
from collections import defaultdict

mapeo_acciones = {
    0: {"id": ("shift", 5)},
    1: {"+": ("shift", 6), "$": ("accept",)},
    2: {"+": ("reduce", "E", ["T"]), "$": ("reduce", "E", ["T"])},
    3: {"+": ("reduce", "T", ["id"]), "$": ("reduce", "T", ["id"])},
    4: {"+": ("reduce", "E", ["E", "+", "T"]), "$": ("reduce", "E", ["E", "+", "T"])},
    5: {"+": ("reduce", "T", ["id"]), "$": ("reduce", "T", ["id"])},
    6: {"id": ("shift", 5)},
}

GOTO = {
    0: {"E": 1, "T": 2},
    6: {"T": 4},
}



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
def imprimir_gramatica(gramatica):
    for izq, der in gramatica.items():
        print(f"{izq} -> {' | '.join(' '.join(prod) for prod in der)}")
        
def crear_simbolo_inicial(gramatica, inicial):
    nueva_gramatica = defaultdict(list, gramatica)
    inicial_aumentado = inicial + "'"
    nueva_gramatica[inicial_aumentado] = [[inicial]]
    return nueva_gramatica, inicial_aumentado

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python analizador.py gramatica.txt")
        sys.exit(1)
        
        
        
    archivo = sys.argv[1]
    gramatica, inicial = leer_gramatica(archivo)
    gramatica_aum, inicial_aum = crear_simbolo_inicial(gramatica, inicial)
    
    imprimir_gramatica(gramatica_aum)