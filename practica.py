# funcion que indica si una palabra es palindromo

def palindromo(palabra):
    palabra = palabra.lower().replace(' ', '')
    return palabra == palabra[::-1]

print(palindromo('Anita lava la tina')) # True

# crea una funcion que calcule el factorial de un numero
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120 


# crea una funcion que ordene por el metodo de la burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

print(burbuja([64, 34, 25, 12, 22, 11, 90])) # [11, 12, 22, 25, 34, 64, 90]

