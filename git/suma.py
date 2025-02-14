def sum(a, b):
    c = b
    while (a > 0):
        a -= 1
        c += 1
    return c

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

print (sum(a, b))    