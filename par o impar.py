#determinar en parametro de n y m cual es par o impar

n=int(input('escoge un número cualquiera positivo: '))
while n<=0:
    n=int(input('error, escoge un número cualquiera positivo: '))
m=int(input('escoge un número cualquiera positivo mayor que el anterior: '))
while m<=n:
    m=int(input('error, escoge un número cualquiera positivo mayor que el anterior: '))
    
for i in range (m,n,-1):
    if i%2==0:
        print(i,'es par')
    else:
        print(i,'es impar')
