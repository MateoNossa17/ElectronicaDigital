def Decimal_binario(x):
    residuo=[]
    while int(x)!=0:
        r=int(x)%2
        residuo.append(r)
        x=int(x)//2
    resultado=''
    for j in range(len(residuo),0,-1):
        resultado+=f'{residuo[j-1]}'
    print(f'El binario de su número {resultado}')

num=input(str('Escriba una número decimal entero para obtener su equivalente en binario:'))
Estado=False
base10=['0','1','2','3','4','5','6','7','8','9']
for i in range (0,len(num)):
    if num[i] in base10:
        Estado=True
    else:
        print('El número contiene caracteres distintos a los números del 0 a el 9')
        Estado=False
        break
if Estado==True:
    Decimal_binario(num)


