# TC3002B-Compilador Patito

**Autor**: Erick Alfredo García Huerta - A01708119

## Acerca de este repositorio

Patito es un compilador en python y ANTLR

## Requerimientos
* Java 11+
* Python 3.13+

## Generación de árbol

``java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 patito.g4 -listener -o antlr_files``

## Ejecución de pruebas

``python main.py .\test\<Archivo entrada.txt>``

