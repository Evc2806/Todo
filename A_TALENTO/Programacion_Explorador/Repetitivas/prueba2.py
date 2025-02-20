sumaTotal = 0
salir = False
while not salir:
    menu = int(input('''
                     1.Pasta precio = 1000
                     2.Bandeja Paisa precio = 2000
                     3.Pescado precio = 4000
                     4.Salir 
                     
                     '''))
    if menu == 1:
        pasta = 1000
        print(f'El usuario ordeno Pasta = ¨{pasta}')
        sumaTotal=sumaTotal+pasta
    elif menu ==2:
        bandejaPaisa = 2000
        print(f'El usuario ordeno Bandeja Paisa = ''{bandejaPaisa}')
        sumaTotal += bandejaPaisa
    elif menu == 3:
        pescado = 4000
        print(f'El usuario ordeno Pescado = ¨{pescado}')
        sumaTotal += pescado
    elif menu == 4:
        print(f'El valor total= {sumaTotal}')
        salir = True
        break
    