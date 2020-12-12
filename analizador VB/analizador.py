import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['MODULE','SUB','END','MOD','IMPORTS','PROGRAM','MAIN','ARGS','AS','STRING',
'CONSOLE','WRITELINE','VBCRLF','DIM','READLINE','DATETIME','NOW','READKEY','TRUE','FALSE','BOOLEAN'
		]

tokens = reservadas+['ID','ENTERO','SUMA','RESTA','DIV','MULTI','MENORQ','MAYORQ','IGUAL','NOIGUAL',
'PIZQ','PDER','LLIZQ','LLDER','PUNTO','DOUBLE','CADENA','CLASS','CARACTER','PUBLIC','PRIVATE','VARIABLE','UPDATE'
		]

t_PUNTO = r'\.'
t_LLIZQ = r'\{'
t_LLDER = r'\}'
t_ignore = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'/'
t_IGUAL = r'='
t_MENORQ = r'<'
t_MAYORQ = r'>'
t_NOIGUAL = '~='
t_UPDATE = r':='
t_PIZQ = r'\('
t_PDER = r'\)'





def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\'.*'
	pass

def t_DOUBLE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_BOOLEAN(t):
    r'TRUE|FALSE'
    t.value = (t.value)
    return t

def t_CLASS(t):
    r'Class'
    return t

def t_PUBLIC(t):
    r'Public'
    return t

def t_PRIVATE(t):
    r'Private'
    return t

def t_CADENA(t):
    r'\".+\"'
    t.value = (t.value)
    return t

def t_VARIABLE(t):
    r'\s[A-Za-z]+\,|[a-zA-Z]\='
    t.value = (t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):	
	t.lexer.skip(1)

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()		
		t.type = t.value
	return t






# pruebas
direccion ='prueba.vb'
prueba = direccion
fp = codecs.open(prueba, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)