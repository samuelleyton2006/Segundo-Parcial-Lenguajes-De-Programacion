grammar CRUD;

programa: instruccion+ ;
instruccion: crear
           | leer
           | actualizar
           | eliminar ;
crear: 'CREATE' 'INTO' tabla 'VALUES' '(' lista_valores ')' ;
leer: 'READ' 'FROM' tabla ('WHERE' condicion)? ;
actualizar: 'UPDATE' tabla 'SET' asignaciones ('WHERE' condicion)? ;
eliminar: 'DELETE' 'FROM' tabla ('WHERE' condicion)? ;

tabla: ID ;
lista_valores: valor (',' valor)* ;
valor: NUMBER | STRING ;
asignaciones: asignacion (',' asignacion)* ;
asignacion: ID '=' valor ;
condicion: ID '=' valor ;

// Tokens
ID: [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER: [0-9]+ ;
STRING: '"' .*? '"' ;
WS: [ \t\r\n]+ -> skip ;
