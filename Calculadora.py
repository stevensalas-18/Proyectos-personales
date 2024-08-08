print('Bienvenido a la calculadora')
usuario= int(input("Digite la opcion que desea realizar. \n1 Suma: \n2 Resta: \n3 Multplicacion: \n4 Divison: \n5 Salir: " ))
if usuario == 1:
    n1=int(input('Digite el primer numero que desea sumar: '))
    n2=int(input('Digite el segundo numero que desea sumar: '))
    re=n1+n2
    print('El resulatado de la suma es', re)
if usuario == 2:
    n1=int(input('Digite el primer numero que desea restar: ' ))
    n2=int(input('Digite el segundo numero que desea restar: ' ))
    re=n1-n2
    print('El resultado de la de la resta es', re )
if usuario == 3:
    n1 = int(input('Digite el primer numero que desea multiplicar: ' ))
    n2 = int(input('Digite el segundo numero que desea multiplicar: ' ))
    re = n1 * n2
    print('El resultado de la de la multiplicacion es', re )
if usuario == 4:
    try:
        n1 = int(input('Digite el primer número que desea dividir: '))
        n2 = int(input('Digite el segundo número que desea dividir: '))
        re = n1 / n2  
        print('El resultado de la división es:', re)
    except ZeroDivisionError:
        print('Error: No se puede dividir por cero.')
if usuario == 5:
    print("Gracias por usar la calculadora")

    
   

    
    