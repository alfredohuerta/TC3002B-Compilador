grammar patito;

// Regla inicial del programa
programa: PROGRAMA ID ';' vars? funcs* INICIO cuerpo FIN
        | PROGRAMA ID ';' funcs* programaBis
        | PROGRAMA ID ';' funcs* INICIO cuerpo* FIN
        | PROGRAMA ID ';' INICIO cuerpo FIN
        | PROGRAMA ID ';' vars? INICIO cuerpo FIN
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

// Cuerpo de código principal
cuerpo: '{' estatuto '}'
      | '{' estatutoBis '}'
      ;

// Reglas para funciones adicionales
programaBis: funcs programaBis
        | INICIO cuerpo FIN
        ;

// Reglas para múltiples estatutos
estatutoBis: estatuto estatutoBis
           | estatuto
           ;

// Diferentes tipos de estatutos dentro del cuerpo
estatuto: asigna
        | llamada
        | condicion
        | ciclo
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
termino: factor
       | factor divmult
       ;

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
PROGRAMA: 'Programa' ;
VARS: 'Vars' ;
NULA: 'Nula' ;
INICIO: 'Inicio' ;
FIN: 'Fin' ;
ESCRIBE: 'Escribe' ;
MIENTRAS: 'Mientras' ;
HAZ: 'Haz' ;
SI: 'Si' ;
SINO: 'Sino' ;

// Tokens para tipos de datos
INT_TOK: 'int' ;
FLOAT_TOK:  'float' ;
ID: [a-zA-Z] [a-zA-Z0-9_]*;
CTE_FLOT: '-'? [0-9]+ '.' [0-9]+;
CTE_ENT: '-'? [0-9]+;
LETRERO: '"' ~[\r\n"]* '"';

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip ;
