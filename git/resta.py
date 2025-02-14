def sbt (a, b):
    c = 0
    while (b < a):
        c+=1
        b+=1
    return c

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

print (sbt(a, b))


