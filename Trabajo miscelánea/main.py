while(True):
    print("")
    print("Bienvenido a mi programa")
    print("")
    print("[a]: Operadores")
    print("[b]: Condicionales")
    print("[c]: Ciclos")
    print("[d]: Arreglos")
    print("")
    print("[99] Finalizar programa")
    print("")
    
    choice=input("Ingresar letra o numero de la seccion a la cual desea ingresar: ") 
    
    import os
    import random
    os.system("clear")
    if choice=="a":
      print("[OPERADORES]")
      print("")
      print("[1]: Area y altura de un triangulo ")
      print("[2]: Sumas")
      print("[3]: Numero al cuadrado ")
      print("[4]: Convertir dolares a euros ")
      print("[5]: Obtener area y perimeto de un cuadrado")
      print("[6]: Obtener el area y perimetro de un cilindro")
      print("[7]: Obtener el area y longitud de un circulo")
      print("[8]: Calcular el promedio de 3 numeros")
      print("")
      choice=input("ingrese numero a la seccion a la cual quiere ingresar: ")
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
  
  
    if choice=="b":    
      print("[CONDICIONALES]")
      print("")
      print("[1]: Numeros positivos o negativos ")
      print("[2]: Numeros mayores o menores")
      print("[3]: calcular entre tres numero cual es mayor y menor ")
      print("[4]: si A es mayor restarlo, en cambio si A es menor sumarlo ")
      print("[5]: Obtener el cociente de una division")
      print("[6]: Da dos numeros, si alguno de ellos son negativos se suman en lo contrario se multiplican")
      print("[7]: Conocer que años son bisiestos")
      print("")
      choice=input("ingrese numero de la seccion a la cual desea ingresar: ")
      if choice=="1":
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
   
   
      
      if choice=="2":
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
  
  
      if choice=="3":
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
  
  
  
      if choice=="4":
        print("                                                     ")
        print("si A es mayor se resta por lo contrario se suman")
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
  
  
  
  
  
  
  
      if choice=="5":
        print("                                                     ")
        print("ingrese el dividiendo y un divisor para obtener el cociente") 
        print("dividiendo")
        a = int(input())
        print("divisor")
        b = int(input())
        if b == 0:
          print("El divisor no puede ser 0")
        
        else:
         print("El cociente de la división es",str(a/b))
        print("")
        n4 = input("Enter para continuar")
        os.system("clear") 
  
  
  
  
  
  
  
  
  
  
  
      if choice=="6":
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
  
    
      if choice=="7":
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


    if choice=="c":
      print("[CICLOS]")
      print("")
      print("[1]: Imprimir todos los multiplos de 3 hasta 100 ")
      print("[2]: Imprimir todos los numeros impares hasta el numero deseado")
      print("[3]: Imprimir todos los numeros pares hasta el numero deseado ")
      print("[4]: Todos los numeros cuadrados del 1 al 30 ")
      print("[5]: La suma de los numeros cuadrados del 1 al 100")
      print("[6]: 2 numeros naturales")
      print("[7]: Sumar numeros de forma infinita hasta el 0")
      print("")
      choice=input("ingrese numero a la seccion a la cual quiere ingresar: ")    
      
      if choice=="1":
        print("                                                     ")
        print("Todos los multiplos de 3")
        num = 100
        odd_numbers = [i for i in range(num) if i % 2 != 0]
        print("Los multiplos de 3 hasta el 100:")
        print(odd_numbers)
        print("")
        n4 = input("ENTER para continuar")
        os.system("clear")
  
  
      if choice=="2":
        print("                                         ")
        print("digete un numero para mostrar todos los impares hasta ese numero")
        num = int(input())
        odd_numbers = [i for i in range(num) if i % 2 != 0]
        print(f"Todos los numeros impares hasta {num}:")
        print(odd_numbers)
        print("")
        n4 = input("ENTER para continuar")
        os.system("clear")
  
  
      if choice=="3":  
        print("")
        print("digete un numero para mostrar todos los pares hasta ese numero")
        num = int(input())
        odd_numbers = [i for i in range(num) if i % 2 != 1]
        print(f"Todos los numeros pares hasta {num} son:")
        print(odd_numbers)
        print("")
        n4 = input("ENTER para continuar")
        os.system("clear")
  
  
      if choice=="4":
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
      if choice=="5":
        print("")
        print("La suma de los 100 primeros numeros cuadrados")
        print("Resultado: 338350")
        print("")
        n4 = input("ENTER para continuar")
        os.system("clear") 
    
  

    
      if choice=="6":
          print("Digite dos numeros")
          n1=int(input('Digite el número inicial de la secuencia \n'))
          n2=int(input('Digite el número final de la secuencia \n'))  
          nums=[]
          for i in range(n1, n2 + 1):
            nums.append(i)
          print('\n La secuencia ascendente de los números es:', nums)
          n4 = input("ENTER para continuar")
          os.system("clear") 
      if choice=="7":
          print("digite digites para sumar infinitamente hasta el cero")
          nums=[]
          while True:
              n=float(input('Digite el número a sumar, para concluir la suma por favor digite 0:'))
              if n!=0:
                  nums.append(n)
              else:
                  break
          print('Los números digitados fueron:', nums)
          print('La suma de los números fue:', sum(nums))
          n4 = input("Enter para continuar")
          os.system("clear")
    if choice=="d":    
      print("[ARREGLOS]")
      print("")
      print("[1]: Numeros aleatorios") 
      print("[2]: Organizacion de elementos en inversa")
      print("[3]: Organizacion de numero de menor a mayor, mayor a menor y de menor a mayor ")
      print("[4]: En arreglo decir cual es mayor y cual es menor")
      print("[5]: Convertir numeros ingresados en *")
      print("[6]: Identificar cantidad de veces que aparece un número en un arreglo")
      print("[7]: Identificar si un número es impar y par")
      print("")
      choice=input("Ingrese el numero de la seccion la cual desea ingresar: ")
      if choice=="1":
            nums=[]
            aux=None
            while True:
                cant=int(input('Ingrese la cantidad de números que desea ver\n'))
                for i in range(cant):
                    n=random.randint(-100,100)
                    nums.append(n)
                print(nums)
                for i in range(len(nums)-1):
                  for i in range(len(nums)-1):
                    if nums[i]>=nums[i+1]:
                      aux=nums[i+1]
                      nums[i+1]=nums[i]
                      nums[i]=aux
                print(nums)
                break
            n4 = input("ENTER para continuar")
            os.system("clear")
  
    
      if choice=="2":
        print("")
        lista = []
        print("introducir 10 elementos")
        print("elemento 1:")
        n1 = int(input())
        print("elemento 2:")
        n2 = int(input())
        print("elemento 3:")
        n3 = int(input())
        print("elemento 4:")
        n4 = int(input())
        print("elemento 5:")
        n5 = int(input())
        print("elemento 6:")
        n6 = int(input())
        print("elemento 7:")
        n7 = int(input())
        print("elemento 8:")
        n8 = int(input())
        print("elemento 9:")
        n9 = int(input())
        print("elemento 10:")
        n10 = int(input())
        lista.append(n1)
        lista.append(n2)
        lista.append(n3)
        lista.append(n4)
        lista.append(n5)
        lista.append(n6)
        lista.append(n7)
        lista.append(n8)
        lista.append(n9)
        lista.append(n10)
        lista.reverse()
        print(lista)
        n98 = input("ENTER para continuar")
        os.system("clear")
        
               
      if choice=="3":
        print("")
        n = 10
        print("Ingresar 10 numeros:")  
        lista=[]
        for x in range(n):
            valor=float(input("Ingrese un numero: ")) 
            lista.append(valor)
        
        RecorrerLista = False 
        while RecorrerLista == False: 
            RecorrerLista = True
    
            for i in range(len(lista)-1):
                if lista[i] > lista[i + 1]:
                    VariableAuxiliar = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = VariableAuxiliar
                    RecorrerLista = False

        print("Orden ASCENDENTE (de menor a mayor): ")
        for i in range(0,n,1):
            print(lista[i])

        print("Orden DESCENDENTE (de mayor a menor): ")
        longitud_lista=len(lista)
        for i in range(longitud_lista//2):
            lista[i], lista[longitud_lista-i-1] = lista[longitud_lista-i-1], lista[i]
        print(lista)
        print("Orden ASCENDENTE (de menor a mayor): ")
        lista.reverse()
        for a in range(0,n,1):
            print(lista[a])
        n4 = input("ENTER para continuar")
        os.system("clear")
      if choice=="4":
        print("")
        print("ingrese la cantidad de elementos que desea en su arreglo")
        n = int(input())
        print(f"Ingresar {n} numeros:")  
        lista=[]
        for x in range(n):
          valor=float(input("Ingrese un numero: ")) 
          lista.append(valor)



        def mayor_de_arreglo(lista):
    
            mayor = lista[0]

            for elemento in lista:
              if elemento > mayor:
                mayor = elemento
            return mayor


        def menor_de_arreglo(lista):
            menor = lista[0]
            for elemento in lista:
              if elemento < menor:
                menor = elemento
            return menor

        mayor = mayor_de_arreglo(lista)
        menor = menor_de_arreglo(lista)
        print(f"Del arreglo {lista} el mayor es {mayor} y el menor es {menor}")

        n4 = input("Enter para continuar")
        os.system("clear")
      if choice=="5":
        nums=[]
        n1 = int(input("Ingresar la cantidad de numeros de desea ingresar: "))
        for i in range(n1):
          n=int(input('Digite un numero: '))
          nums.append(n)
        for i in nums:
          print(i,'->',i*'*')
        n4 = input("Enter para continuar")
        os.system("clear")
      if choice=="6":
          counts=dict()
          nums=[]
          n3 = int(input("Ingrese el rango de numeros que desea tener en el buscador"))
          for i in range(n3):
              n=int(input('Digite un numero: '))
              nums.append(n)
          for num in nums :
              counts [num] = counts.get (num, 0) + 1
          x=int(input('Ingrese el número que desea buscar: \n'))
          try:
            print('el número {} está {} veces'.format(x, counts[x]))
          except:
            print('no se encontró el número {} en la lista'.format(x))
          n4 = input("Enter para continuar")
          os.system("clear")
      if choice=="7":
        print("Digite Sus 8 Numeros")
        valores = 8
        valor1 = 0
        impar = []
        par = []
        lista = []
        while valor1 < valores:
          print("Llevas Digitado", (valor1 + 1), "Numeros")
          enteros = int(input())
          lista.append(enteros)
          valor1 += 1
        for i in range(valores):
          if lista[i] % 2 == 0:
            par.append(lista[i])
          else:
            impar.append(lista[i])
        impar.sort()
        par.sort()
        print("El Arreglo Que Diste Fue: \n"+ str(lista),"\n""Los Numeros Impares Del Arreglo Son: \n"+ str(impar),"\n""Los Numeros Pares Del Arreglo Son: \n"+ str(par))
        n4 = input("ENTER para continuar")
        os.system("clear")
    if choice=="99":
        print("")
        print("Gracias por participar")
        print("Creado por: Santiago Polanco Buitrago ")
        break
  
  
  
  
