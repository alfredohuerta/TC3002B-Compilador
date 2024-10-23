grammar patito;

// Regla inicial del programa
programa: PROGRAMA ID ';' vars? funcs* INICIO cuerpo FIN
        | PROGRAMA ID ';' INICIO cuerpo FIN
        | PROGRAMA ID ';' vars? INICIO cuerpo FIN
        | PROGRAMA ID ';' funcs* INICIO cuerpo* FIN
        | PROGRAMA ID ';' funcs* funcsBis
        ;

// Regla para la declaración de variables
vars: VARS cycle
    ;

cycle:  ID (',' ID)* ':' tipo ';' ( ID (',' ID)* ':' tipo ';' ) cycle?
     ;

// Definición de funciones
funcs: NULA ID '(' ID ':' tipo ')' '{' vars cuerpo '}' ';'
     | NULA ID '(' ID ':' tipo ')' '{' cuerpo '}' ';'
     ;

// Reglas para funciones adicionales
funcsBis: funcs funcsBis
        | INICIO cuerpo FIN
        ;

// Cuerpo de código principal
cuerpo: '{' estatuto '}'
      | '{' estatutoBis '}'
      ;

// Reglas para múltiples estatutos
estatutoBis: estatuto estatutoBis
           | estatuto
           ;

// Diferentes tipos de estatutos dentro del cuerpo
estatuto: asigna
        | condicion
        | ciclo
        | llamada
        | imprime
        ;

// Definición de tipos de datos
tipo: INT_TOK
    | FLOAT_TOK
    ;

// Reglas de expresión
expresion: exp
         | bool exp
         ;

// Operadores booleanos
bool: '>' exp
    | '<' exp
    | '>=' exp
    | '<=' exp
    | '==' exp
    ;

// Expresión aritmética
exp: termino
   | (termino op)*
   ;

// Operadores para las expresiones aritméticas
op: '+'
  | '-'
  |
  ;

// Términos de una expresión
termino: factor divmult ;

// Multiplicación o división dentro de un término
divmult: '*' factor
       | '/' factor
       |
       ;

// Factores en una expresión
factor: '(' expresion ')'
      | '+' ID
      | '-' ID
      | ID
      | cte
      ;

// Constantes en las expresiones
cte: CTE_ENT
    | CTE_FLOT
    ;

// Llamada a funciones
llamada: ID '(' expresion ')' ';'
       | ID '(' expresionBis ')' ';'
       ;

// Expresiones separadas por comas
expresionBis: expresion (',' expresion)* ;

// Declaración de condiciones
condicion: SI '(' expresion ')' cuerpo ';'
         | SI '(' expresion ')' cuerpo SINO cuerpo
         ;

// Impresión en pantalla
imprime: ESCRIBE '(' parametros ')' ';'
       ;

parametros: expresion
          | expresion ',' parametros
          | LETRERO
          | LETRERO ',' parametros
          ;

// Ciclo `mientras`
ciclo: MIENTRAS '(' expresion ')' HAZ cuerpo ';'
     ;

// Asignación de variables
asigna: ID '=' expresion ';'
      ;

// Definición de typeId
typeId: ',' ID ':' tipo typeId
      | ;

// Palabras reservadas
INICIO: 'Inicio' ;
FIN: 'Fin' ;
ESCRIBE: 'Escribe' ;
NULA: 'Nula' ;
PROGRAMA: 'Programa' ;
SI: 'Si' ;
SINO: 'Sino' ;
MIENTRAS: 'Mientras' ;
HAZ: 'Haz' ;
VARS: 'Vars' ;

// Tokens para tipos de datos
INT_TOK: 'int' ;
FLOAT_TOK:  'float' ;
ID: [a-zA-Z] [a-zA-Z0-9_]*;
LETRERO: '"' ~[\r\n"]* '"';
CTE_ENT: '-'? [0-9]+;
CTE_FLOT: '-'? [0-9]+ '.' [0-9]+;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip ;
