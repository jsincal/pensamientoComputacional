def main():
    nombre1 = input("""Usuario 1
    Ingresa tu nombre: """)
    edad1 = int(input(f'Hola {nombre1} cual es tu edad: '))
    nombre2 = input("""Usuario 2
    Ingresa tu nombre: """)
    edad2 = int(input(f'Hola {nombre1} cual es tu edad: '))

    if edad1 > edad2:
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad2 > edad1:
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} y {nombre2} tienen la misma edad.')

if __name__ == '__main__':
    main()
