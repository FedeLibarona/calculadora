number1=int(input("ingresa un numero:"))
number2=int(input("ingresar otro numero:"))

eleccion = 0

while eleccion != 4:
    print("""
    Indique la opearacion:
    
    1) suma
    2) resta 
    3) cambio de valores 
    4) salir
    """)  

    eleccion = int(input())
    
    if eleccion -- 1:
        print(" ")
    
        print("resultado: ", number1,"+" , number2,"-",number1+number2)
        
    if eleccion -- 2:
        print(" ")
        print("resultado: ",number1,"-", number2,"-",number1-number2)
        
    
