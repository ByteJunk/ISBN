import sys

def validarISBN10(valor):
    total = total_m = 0
    for i in range(0, len(valor)):
        total += int(valor[i])
        total_m += total
    return (int(total_m) % 11) == 0

def validarISBN13(valor):
    total = 0
    for i in range(0,len(valor)):
        if i & 1:
            total += int(valor[i])*3
        else:
            total += int(valor[i])
    return (int(total) % 10) == 0


print("Insira o ISBN10 ou ISBN13 que pretende validar.")
x = input("ISBN: ")

x = x.strip()   # Remove espaços antes e depois

y = x.replace("-", "")

if len(y) == 10:
    print("Temos um ISBN10 para validar.")
    if validarISBN10(y):
        print("ISBN10 válido.")
    else:
        print("ISBN10 inválido.")
elif len(y) == 13:
    print("Temos um ISBN13 para validar.")
    if validarISBN13(y):
        print("ISBN13 válido.")
    else:
        print("ISBN13 inválido.")
else:
    sys.exit("Número de caracteres inválido.")

