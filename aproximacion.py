def run():
    objetivo = int(input('Escoge un entero:'))
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta**2 - objetivo)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


if __name__ == '__main__':
    run()
