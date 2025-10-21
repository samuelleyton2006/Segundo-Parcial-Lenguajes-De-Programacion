grammar Crud;

options {
    language = Python3;
}

// ----------- Reglas del parser -----------

programa
    : instruccion* EOF
    ;

instruccion
    : crear_entidad
    | consultar_entidad
    | modificar_entidad
    | eliminar_entidad
    ;

crear_entidad
    : 'INICIAR' 'ENTIDAD' nombre_entidad '(' lista_atributos ')'
    ;

lista_atributos
    : atributo (';' atributo)*
    ;

atributo
    : nombre_atributo tipo_dato
    ;

consultar_entidad
    : 'OBTENER' 'ENTIDAD' nombre_entidad ('CONDICION' expresion_condicion)?
    ;

modificar_entidad
    : 'CAMBIAR' nombre_entidad 'CON' lista_modificaciones ('CONDICION' expresion_condicion)?
    ;

lista_modificaciones
    : modificacion (';' modificacion)*
    ;

modificacion
    : nombre_atributo '=' valor
    ;

eliminar_entidad
    : 'BORRAR' 'ENTIDAD' nombre_entidad ('CONDICION' expresion_condicion)?
    ;

expresion_condicion
    : nombre_atributo operador_comparacion valor
    ;

operador_comparacion
    : '==' | '!=' | '<' | '>' | '<=' | '>='
    ;

valor
    : TEXTO
    | NUMERO
    | nombre_atributo
    ;

tipo_dato
    : 'NUMERO'
    | 'TEXTO'
    | 'DECIMAL'
    | 'BOOLEANO'
    ;

nombre_entidad
    : IDENTIFICADOR
    ;

nombre_atributo
    : IDENTIFICADOR
    ;

// ----------- Reglas del lexer -----------

TEXTO
    : '"' (~["\\] | '\\' .)* '"'
    ;

NUMERO
    : [0-9]+ ('.' [0-9]+)?
    ;

IDENTIFICADOR
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
