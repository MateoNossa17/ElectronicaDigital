def decimal_binario(bi):
    potencia=0#Se establece un valor inicial para la potencia, en este caso '0'
    suma=0#Variable para poder ir sumando los resultados 
    for j in range (len(bi),0,-1):# Se recorre la lista al revés para poder ir operando el numero correctamente
        x=(int(bi[j-1]))*2**potencia#Respectiva operación para convertir un numero decimal a binario
        suma+=x#La operación anterior se suma la variable
        potencia+=1#Incrementa el valor de la potencia 
    print(f'El número {bi} en decimal es: {suma}')


num=input(str('Escriba el número en binario para obtener su valor en numeración en decimal (Solo 1 y 0; no mas de 63 bits/dígitos):'))#Se toma como 'str' para analizarlo como una lista de caracteres 

Estado=False #Se establece un estado para posterior comprobación de que el numero solo este compuesto de '1' y '0'
for i in range(0,len(num)):#Se hace uso de la función 'len' para comenzar la comprobación da cada elemento
    if num[i]=='1' or num[i]=='0' :
        Estado=True# Si todos los elementos son '1' o '0' se da por valido para previa operación
    else:
        print('Hay valores distintos de 1 y 0, verifique y vuelca a intentarlo y/o el número es mayor a 63 bits/dígitos')
        Estado=False #Si encuentra algún valor distinto de '1' y '0' se rompe el ciclo (For) y el numero queda invitado para que no se ejecute el resto del programa
        break

if Estado==True and len(num)<=63: #Comprueba el estado y valida la cantidad de dígitos
    decimal_binario(num)#Se invoca la función
else:
    print('El número es mayor a 63 bits/dígitos') #Si no cumple la condición de los dígitos máximos
