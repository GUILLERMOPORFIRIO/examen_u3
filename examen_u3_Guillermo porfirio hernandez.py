

def gPrimo(N):
	i=1
	while i<N:
		if i%3==0:
			yield i
		i=i+1
g=gPrimo(10)
z=[e for e in g]



print(z)

from math import sqrt  
def esPrimo(n):  
 for i in range(3,int(sqrt(n))+1,2):  
  if n%i==0:  
   return False  
 return True  
def generaPrimos(n):  
 for i in filter(esPrimo, range(3,n+1,2)):  
  yield i  
print(2)  
for i in generaPrimos(10):  
 print(i)  
 
def badaboom(n):
     
     Bada = n % 3 ==0
     Boom = n % 5 ==0
     
     if Bada and Boom :
         return "BadaBoom!"
     elif Bada:
         return "Bada"
     elif Boom:
         return "Boom"
     else:
         return n
N = [ badaboom(i+1) for i in range(10)]     
     
print(N) 

from itertools import product

def permutaciones_repeticion(cadena, tamagnio):
    caracteres = list(cadena)
    permutaciones = []
    
    for c in product(caracteres, repeat =tamagnio):
        permutaciones.append(c)
        
        return permutaciones
    texto = "abc"
    pantalones = "negroazulcafeobscurocrema"
    camisas = "roja negraa zul morada cafe"
    accesorios = "cinturon tirantes lentes fedora"
    tamagnio = 3
    print(permutaciones_repeticion(camisas, tamagnio))	