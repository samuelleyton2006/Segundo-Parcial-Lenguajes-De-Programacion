import sys
from collections import defaultdict


# Mapeo de acciones: Por cada estado (0-11), define las acciones a hacer dependiendo del simbolo

mapeo_acciones = {
    0: {'id': ('shift', 5), '(': ('shift', 4)},
    1: {'+': ('shift', 6), '$': ('accept',)},
    2: {'+': ('reduce', 2), '*': ('shift', 7), '$': ('reduce', 2)},
    3: {'+': ('reduce', 4), '*': ('reduce', 4), ')': ('reduce', 4), '$': ('reduce', 4)},
    4: {'id': ('shift', 5), '(': ('shift', 4)},
    5: {'+': ('reduce', 6), '*': ('reduce', 6), ')': ('reduce', 6), '$': ('reduce', 6)},
    6: {'id': ('shift', 5), '(': ('shift', 4)},
    7: {'id': ('shift', 5), '(': ('shift', 4)},
    8: {'+': ('shift', 6), ')': ('shift', 11)},
    9: {'+': ('reduce', 1), '*': ('shift', 7), ')': ('reduce', 1), '$': ('reduce', 1)},
    10: {'+': ('reduce', 3), '*': ('reduce', 3), ')': ('reduce', 3), '$': ('reduce', 3)},
    11: {'+': ('reduce', 5), '*': ('reduce', 5), ')': ('reduce', 5), '$': ('reduce', 5)},
}

# GOTO: estado -> {nonterminal: estado_destino}
GOTO = {
    0: {'E': 1, 'T': 2, 'F': 3},
    4: {'E': 8, 'T': 2, 'F': 3},
    6: {'T': 9, 'F': 3},
    7: {'F': 10},
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

        
def crear_simbolo_inicial(gramatica, inicial):
    nueva_gramatica = defaultdict(list, gramatica)
    inicial_aumentado = inicial + "'"
    nueva_gramatica[inicial_aumentado] = [[inicial]]
    return nueva_gramatica, inicial_aumentado


def tokenize(expr):
    # Tokenizador simple para la expresion de entrada
    import re
    # también capturamos cualquier otro carácter no espacial como 
    # token (p. ej. '-' u otros) para no ignorarlos accidentalmente
    raw = re.findall(r"id|[a-zA-Z_]\w*|\+|\*|\(|\)|\S", expr)
    tokens = []
    for t in raw:
        if re.fullmatch(r"\+|\*|\(|\)", t):
            tokens.append(t)
        elif re.fullmatch(r"id|[a-zA-Z_]\w*", t):
            # cualquier identificador se mapea al token 'id'
            tokens.append('id')
        else:
            # token desconocido (por ejemplo '-') lo dejamos tal cual
            tokens.append(t)
    return tokens


def parse_with_stack(tokens, verbose=True):
    producciones = {
        1: ('E', ['E', '+', 'T']),
        2: ('E', ['T']),
        3: ('T', ['T', '*', 'F']),
        4: ('T', ['F']),
        5: ('F', ['(', 'E', ')']),
        6: ('F', ['id']),
    }

    tokens = list(tokens) + ['$']
    state_stack = [0]
    symbol_stack = []
    ip = 0

    if verbose:
        print(f"{'Pila de estados':20} {'Pila de simbolos':30} {'Proximo Token':10} {'Accion'}")

    while True:
        s = state_stack[-1]
        a = tokens[ip]
        accion = mapeo_acciones.get(s, {}).get(a)

        # imprimir estado actual
        if verbose:
            st = ' '.join(map(str, state_stack))
            sy = ' '.join(symbol_stack)
            print(f"{st:20} {sy:30} {a:10} {accion}")

        if accion is None:
            raise SyntaxError(f"Error de sintaxis: estado={s}, simbolo={a}")

        if accion[0] == 'shift':
            _, t = accion
            symbol_stack.append(a)
            state_stack.append(t)
            ip += 1
            continue

        if accion[0] == 'reduce':
            _, prod_n = accion
            A, rhs = producciones[prod_n]
            # pop por cada símbolo de rhs
            for _ in rhs:
                if symbol_stack:
                    symbol_stack.pop()
                if state_stack:
                    state_stack.pop()
            # push A
            symbol_stack.append(A)
            s_top = state_stack[-1]
            goto_state = GOTO.get(s_top, {}).get(A)
            if goto_state is None:
                raise SyntaxError(f"GOTO no definido para estado {s_top} y no-terminal {A}")
            state_stack.append(goto_state)
            continue

        if accion[0] == 'accept':
            if verbose:
                st = ' '.join(map(str, state_stack))
                sy = ' '.join(symbol_stack)
                print(f"{st:20} {sy:30} {'$':10} {accion}")
                print('\nEntrada aceptada.')
            return True


if __name__ == "__main__":
    
        
        
    if len(sys.argv) < 1:
        expr = sys.argv[1]
    else:
        try:
            expr = input('\nIngrese cadena a analizar: ')
        except EOFError:
            expr = ''

    if expr.strip() == '':
        print('No se proporciono cadena para analizar')
        sys.exit(0)

    tokens = tokenize(expr)
    print(f"\nTokens: {tokens}\n")
    try:
        aceptada = parse_with_stack(tokens, verbose=True)
        if aceptada:
            print('\nResultado: Cadena aceptada')
            sys.exit(0)
        else:
            print('\nResultado: Cadena rechazada')
            sys.exit(1)
    except SyntaxError as e:
        print(f"\nResultado: Cadena rechazada -> {e}")
        sys.exit(1)