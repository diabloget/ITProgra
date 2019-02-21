#Entrada: Valor númerico de x
#Salida: Falso o verdadero para valor de x par
#Restricciones: Usar números.
def espar(x):
    if(x%2==0):
        return True
    else:
        return False

#Entrada: 6 variables numéricas.
#Salida: Rectángulo de asteriscos.
#Rest: Usar números.
def rectángulo(a,b,c,d,e,f):
    if (espar(a)):
        print("*****\n")
    else: 
        print("* * *\n")
    if (espar(b)):
        print("*****\n")
    else: 
        print("* * *\n")
    if (espar(c)):
        print("*****\n")
    else: 
        print("* * *\n")
    if (espar(d)):
        print("*****\n")
    else: 
        print("* * *\n")
    if (espar(e)):
        print("*****\n")
    else: 
        print("* * *\n")
    if (espar(f)):
        print("*****\n")
    else: 
        print("* * *\n")
        
