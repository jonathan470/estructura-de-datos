def prod(a, b):
    c = 0
    while (a > 0):
        a -= 1
        c = c + b
    return c
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

print (prod(a, b))    
        
