while(True):
    print("                                                      ")

    print("Bienvenido a mi programa de prueba")
    print("                                                      ")
    print("                                                      ")
    print("Operadores")
    print("1: Area del triangulo")  
    print("2: Sumas")
    print("3: Numero elevado al cuadrado")
    print("4: Convertidor de euros a dolares")
    print("5: Area y perimetro de un cuadrado")
    print("6: Area y volumen de un cilindro")
    print("7: Area y longitud de un circulo")
    print("8: Calcular el promedio de 3 numeros")
    print("                                                      ")
    print("Condicionales                                                  ")
    print("9: Numeros positivos o negativos")
    print("10: Numero mayor y numero menor")
    print("11: Calcular entre 3 numeros cual es mayor y cual es menor  ")
    print("12: si A es mayor restarlo, en cambio si A es menor sumarlo  ")
    print("13: Obtener el cociente de una division")
    print("14: Da dos numeros, si alguno de ellos son negativos se suman en lo contrario se multiplican")
    print("15: Conocer que años son bisiestos")
    print("                                                     ")
    print("Ciclos                                                  ")
    print("16: Imprimir todos los multiplos de 3 hasta 100 ")
    print("17: Imprimir todos los numeros impares hasta el numero deseado")
    print("18: Imprimir todos los numeros pares hasta el numero deseado")
    print("19: Todos los numeros cuadrados del 1 al 30")
    print("20: La suma de los numeros cuadrados del 1 al 100")
    print("21: 2 numeros naturales")
    print("22: Sumar numeros de forma infinita hasta el 0")
    print("99: Finalizar programa")
    print("                                                     ")
    print("                                                     ")
    print("Escoger el numero de la seccion a la cual desea ingresar")

  
    choice=input("ingresar numero:") 

    import os


    if choice=="1":
      print("                                                    ")
      print("Digite los datos de la base y altura del triangulo")
      print("base:")
      n1 = int(input())
      print("altura:")
      n2 = int(input())
      result1 = n1 * n2
      result = result1 / 2
      print("el area del triangulo es:" + str(result))
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")

  
    if choice=="2":
      print("                                                   ")
      print("Digite dos numeros que se sumaran:")
      n1 = int(input())
      n2 = int(input())
      result = n1 + n2
      print("la suma es de:" + str(result))
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")

  
    if choice=="3":
      print("                                                  ")
      print("ingreso el numero y exponente")
      print("numero:")
      n1 = int(input())
      print("exponente:")
      n2 = int(input())
      result = n1 ** n2
      print("resultado:" + str(result))
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")

  
    if choice=="4":
      print("                                                  ")
      print("euros convertidos a dolares")
      print("euros")
      n1 = int(input())
      result = 1.05 * n1
      print("dolar:" + str(result))
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")

  
    if choice=="5":
      print("                                                   ")
      print("digete la medida de un lado de un cuadrado para")
      print("obtener su Area y Perimetro")
      n1 = int(input())
      medidaarea = n1 * n1
      medidaperimetro = n1 + n1 + n1 + n1
      print("Area")
      print(medidaarea)
      print("Perimetro")
      print(medidaperimetro)
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")


    if choice=="6":
      print("                                                  ")
      print("calcular el area y perimetro de un cilindro")
      print("ingresar radio y altura del cilindro")
      print("radio:")
      n1 = int(input())
      print("altura:")
      n2 = int(input())
      Volumen = (3.1416 * (n1 * n1)) * (n2)
      Area = (2 * 3.1416 * (n1 * n1)) + (2 * 3.1416 * (n1 * n2))
      print("Area")
      print(Area)
      print("Volumen")
      print(Volumen)
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")
  
    if choice=="7":
      print("                                                    ")
      print("calcular el area y longitud de un circulo")
      print("ingresar el radio del circulo:")
      n1 = int(input())
      print("longitud del circulo es:")
      longitud = (2 * n1) * (3.1416)
      print(longitud)
      print("la area es:")
      n8 = (3.1416 * n1) ** 2
      print(n8)
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")

    if choice=="8":
      print("                                                  ")
      print("calcular el promedio de tres numeros")
      print("ingresa los numeros:")
      n1 = int(input())
      n2 = int(input())
      n3 = int(input())
      Promedio = (n1 + n2 + n3) /3
      print("El promedio es:")
      print(Promedio)
      print("")
      n4 = input("Enter para continuar")
      os.system("clear") 


    if choice=="9":
      print("                                                     ")
      print("Ingresa un numero para saber si el numero es negativo o positivo")
      print("Numero:")
      a = int(input())     
      if 0 > a:
        print("El numero es negativo")
      if a > 1:
        print("El numero es positivo")
      if a == 0:
        print("el numero es neutro") 
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear") 
 
 
    
    if choice=="10":
      print("                                                     ")
      print("conocer cual numero es mayor y cual numero es menor")
      print("ingresar el primer numero:")
      n1 = int(input())     
      print("ingresar el segundo numero")
      n2 = int(input())
      if n1==n2:
        print("los dos numeros son iguales")
      elif n1>n2:
        print(f"El numero {n1} es mayor que {n2}")
      elif n2>n1:
        print(f"El numero {n2} es mayor que {n1}")
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear") 


    if choice=="11":
      print("                                                     ")
      print("Calcular entre tres numeros cual es mayor y cual es menor")
      n1 = int(input("ingrese el primer numero:"))
      n2 = int(input("ingrese el segundo numero:"))
      n3 = int(input("ingrese el tercer numero:"))

      if n2 < n1 > n3:
        print(f"el numero mayor es: {n1}")     
      if n1 < n2 > n3:
        print(f"el numero mayor es: {n2}")     
      if n1 < n3 > n2:
        print(f"el numero mayor es: {n3}")     
      
      if n1 > n2 < n3:
        print(f"el numero menor es: {n2}")     
      if n2 > n1 < n3:
        print(f"el numero menor es: {n1}")    
      if n1 > n3 < n2:
        print(f"el numero menor es: {n3}")    
      if n1 == n2:
        print(f"el numero {n1} y {n2} son iguales")    
      if n1 == n3:
        print(f"el numero {n1} y {n3} son iguales")     
      if n2 == n3:
        print(f"el numero {n2} y {n3} son iguales")
      print("")
      n4 = input("Enter para continuar")
      os.system("clear")



    if choice=="12":
      print("                                                     ")
      print("Calcular entre tres numeros cual es mayor y cual es menor")
      n1 = int(input("ingrese el primer numero:"))
      n2 = int(input("ingrese el segundo numero:"))
    
      
      if n1 < n2:
        print(f"el numero mayor es: {n2}")
        result = n1 + n2
        print("Resultado de la suma")
        print(result)
      
      if n2 < n1:
        print(f"el numero menor es:{n1}")
        result = n1 - n2
        print("Resultado de la resta:")
        print(result)
      print("")
      n4 = input("Enter para continuar")
      os.system("clear") 







    if choice=="13":
      print("                                                     ")
      print("ingrese el dividiendo y un divisor para obtener el cociente") 
      print("dividiendo")
      a = int(input())
      print("divisor")
      b = int(input())
      if b == 0:
        print("El divisor no puede ser 0")
      

      print("El cociente de la división es",str(a/b))
      print("")
      n4 = input("Enter para continuar")
      os.system("clear") 











    if choice=="14":
      print("                                                     ")
      print("Ingresar primer numero:")
      n1 = int(input())
      print("Ingresar segundo numero:")
      n2 = int(input())
      
      if n1 < 0 and n2 > 0:
        print(f"El numero {n1} es negativo")
        result1 = n1 + n2
        print("El resultado es:")
        print(result1)
      
      
      if n2 < 0 and n1 >0:
        print(f"el numero {n2} es negativo")
        result1 = n1 + n2
        print("El resultado es:")
        print(result1)
      
      
      if n1 > 0 and n2 > 0:
        print("Los dos son positivos")
        result2 = n1 * n2
        print("El resultado es:")
        print(result2)
      
      if n2 < 0 and n1 <0:
        print(f"el numero {n2} y {n1} es negativo")
        result1 = n1 + n2
        print("El resultado es:")
        print(result1)
      print("")
      n4 = input("Enter para continuar")
      os.system("clear") 

  
    if choice=="15":
      print("                                                     ")
      año = int(input('Introduce un año para saber si es bisiesto: '))
      
      if año % 4 == 0:
          if año % 100 == 0:
              if año % 400 == 0:
                  print('El año es bisiesto')
              else:
                  print('El año no es bisiesto')
          else:
              print('El año es bisiesto.')
      else:
          print('El año no es bisiesto.')
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear") 

    if choice=="16":
      print("                                                     ")
      print("Todos los multiplos de 3")
      num = 100
      odd_numbers = [i for i in range(num) if i % 2 != 0]
      print("Los multiplos de 3 hasta el 100:")
      print(odd_numbers)
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")


    if choice=="17":
      print("                                         ")
      print("digete un numero para mostrar todos los impares hasta ese numero")
      num = int(input())
      odd_numbers = [i for i in range(num) if i % 2 != 0]
      print(f"Todos los numeros impares hasta {num}:")
      print(odd_numbers)
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")


    if choice=="18":  
      print("")
      print("digete un numero para mostrar todos los pares hasta ese numero")
      num = int(input())
      odd_numbers = [i for i in range(num) if i % 2 != 1]
      print(f"Todos los numeros pares hasta {num} son:")
      print(odd_numbers)
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")


    if choice=="19":
      def generar_cuadrados(n):
        if 2 * n <= 30:
          cuadrados = [i ** 2 for i in range(1, 31)]
          return cuadrados
        else:
            raise ValueError("n no debe ser mayor a 2*n")

      resultados = generar_cuadrados(10)  
      print(resultados)
        
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear")   
    if choice=="20":
      print("")
      print("La suma de los 100 primeros numeros cuadrados")
      print("Resultado: 338350")
      print("")
      n4 = input("ENTER para continuar")
      os.system("clear") 
    if choice=="99":
      print("")
      print("Gracias por participar")
      print("Creado por: Santiago Polanco Buitrago ")
      break




