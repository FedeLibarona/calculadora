number1=float(input("ingresa un numero:"))
number2=float(input("ingresar otro numero:"))

eleccion = 0

while eleccion != 8:
    print("""
    Indique la opearacion:
    
    1) suma
    2) resta
    3) multiplicacion
    4) divicion
    5) cambio de valores 
    6) seguir operando
    7) salir
    """)  

    eleccion = int(input())
    
    if eleccion == 1:
        print(" ")
    
        print("resultado: ", number1,"+" , number2,"=",number1+number2)
        numeroanterior = number1+number2
        
    if eleccion == 2:
        print(" ")
        print("resultado: ",number1,"-", number2,"=",number1-number2)
        numeroanterior = number1-number2
    
    if eleccion == 3:
        print(" ")
        print("resultado: ", number1,"*", number2,"=",number1*number2)
        numeroanterior = number1*number2
        
    if eleccion == 4:
        print(" ")
        print("resultado: ", number1,"/", number2,"=",number1/number2)
        numeroanterior = number1/number2
        
        
    if eleccion == 5:
        
       number1 = float(input("cambio de valores"))
       number2 = float(input("cambio de valores"))  
    
    if eleccion == 6:
        
        number1 = numeroanterior
        number2 = float(input("ingresar otro numero"))     
        
    if eleccion == 7:
        
         print ("gracias por usar esta calculadora") 
     
        
        
      
        
         
        
        
        
                
        

    
    
    
        
        
    
        
         
           
        
    
