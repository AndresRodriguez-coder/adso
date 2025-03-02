operacion = input (" selecciones operacion a realizar 1 para Suma , 2 para Resta, 3 Multiplicación, 4 División, 5 Potencia, 6 para Raiz, 7 para Suma de potencias, 8 para Promedio 9 Comparación entre A y B igualdad y número mayor :")

A = int (input("ingrese valor  ")) 
B = int(input("ingrese valor ")) 

match operacion:
    case "1":
       res = A+B 
       print ("la suma de los numeros es: ",res)
    case "2":
       res = A-B 
       print ("la resta de los numeros es: ",res) 
    case "3":
       res = A*B 
       print ("la multiplicacion de los numeros es: ",res)  
    case "4":
      res = A/B 
      print ("la divicion de los numeros es: ",res) 
    case "5":
       res = A**B 
       print ("la potencia es: ",res) 
    case "6":
       res = A**(1/B) 
       print ("la raiz es: ",res) 
    case "7":
      res = (A**B) +(A**B) 
      print ("la suma de potencias es: ",res) 
    case "8":
       res = (A+B)/2 
       print ("el promedio de los dos numeros es : ",res) 
    case "9":
        if A==B:
           print ("el numero es igual", A) 
        elif A>B:
             print ("el numero mayor es : ",A) 
        else:
            print("el numero mayor es: ", B) 
