¿Qué es este punto y en qué se basa?


El ejercicio consiste en crear las reglas sintácticas (producciones) de un lenguaje que permita escribir instrucciones para manejar los datos en una base de datos, específicamente las operaciones CRUD:


	•	Crear (Create): añadir registros.

	
	•	Leer (Read): consultar datos.

	
	•	Actualizar (Update): modificar registros existentes.

	
	•	Eliminar (Delete): borrar registros.

	
La gramática debe describir la estructura de los comandos, identificando cómo se construyen sintácticamente las instrucciones CRUD. Esto suele representarse mediante una gramática formal, normalmente en Notación de Backus-Naur (BNF) o EBNF, usando no terminales y terminales que modelen las palabras claves (“CREATE”, “READ”, etc.), identificadores, valores, condiciones, y otros elementos del lenguaje.


Explicación y Fundamentos : 


Diseñar una gramática formal es fundamental para definir cómo se escriben correctamente los comandos de un lenguaje. Es el primer paso para que posteriormente se pueda implementar un compilador o intérprete que entienda ese lenguaje. En contextos de bases de datos, estos lenguajes suelen estar inspirados en SQL, pero podrías diseñar uno más sencillo para este ejercicio académico.
