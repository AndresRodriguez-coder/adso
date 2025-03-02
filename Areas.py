figura = input ("selecciones la figura a calcular, 1 para Rombo: 2 para Rectángulo: 3 para Cuadrado: 4 para Trapecio: ")
pi =  3.1416
var1 = int (input("ingrese valor  ")) 
var2 = int(input("ingrese valor ")) 
var3 =int (2)

match figura:
    case "1":
       res = ((var1 * var2)/2) 
       print ("el Area del Rombo es: ",res) 
    case "2":
       res = (var1 * var2)
       print ("el Area del Rectángulo es:",res) 
    case "3":
       res = var1 * var2
       print (" el Area del cuadroda es:", res) 
    case "4":
       res = var1 * var2
       print ("el area del Trapecio es :",res) 
   
    case " ":
        
       res = var1 * pi
       print (res) 