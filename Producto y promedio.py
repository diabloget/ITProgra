#entrada: 3 valores numéricos.
#Salida: Calcular promedio y producto de dichos valores.
#Rest: Que las variables 1 y 2 sean mayores en suma a la variable 3.
def calcpromprod(a,b,c):
    if ((a+b)<c) or ((a+b)==c):
        print("Las primeras dos variables en suma son menores a la variable 3")
    else:
        prom = ((a+b+c)/3)
        prod = (a*b*c)
        print("El promedio es:", prom, "y el producto es igual a:", prod)
        
        
