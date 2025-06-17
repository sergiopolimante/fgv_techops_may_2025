{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # calculadora.py\
\
def soma(a, b):\
    """\
    Realiza a soma de dois n\'fameros.\
\
    Args:\
        a (int/float): Primeiro n\'famero da opera\'e7\'e3o\
        b (int/float): Segundo n\'famero da opera\'e7\'e3o\
\
    Returns:\
        int/float: O resultado da soma de a + b\
\
    Examples:\
        >>> soma(5, 3)\
        8\
        >>> soma(-1, 1)\
        0\
        >>> soma(2.5, 3.7)\
        6.2\
    \
    Raises:\
        TypeError: Se os argumentos n\'e3o forem n\'fameros\
    """\
    return a + b\
\
def subtracao(a, b):\
    """\
    Realiza a subtra\'e7\'e3o de dois n\'fameros.\
\
    Args:\
        a (int/float): O minuendo (n\'famero do qual se subtrai)\
        b (int/float): O subtraendo (n\'famero a ser subtra\'eddo)\
\
    Returns:\
        int/float: O resultado da subtra\'e7\'e3o de a - b\
\
    Examples:\
        >>> subtracao(5, 3)\
        2\
        >>> subtracao(-1, 1)\
        -2\
        >>> subtracao(10.5, 3.2)\
        7.3\
    \
    Raises:\
        TypeError: Se os argumentos n\'e3o forem n\'fameros\
    """\
    return a - b\
\
# Exemplo de uso da fun\'e7\'e3o\
if _name_ == "_main_":\
    # Testando a fun\'e7\'e3o\
    resultado = soma(5, 3)\
    print(f"A soma de 5 e 3 \'e9: \{resultado\}")\
\
    resultado_subtracao = subtracao(10, 4)\
    print(f"A subtra\'e7\'e3o de 10 e 4 \'e9: \{resultado_subtracao\}")}