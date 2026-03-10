
def calcular_precio(precio,descuento=10):
    ahorro = precio * descuento / 100
    precio_final = precio - ahorro
    return round(precio_final, 2), round(ahorro, 2)

final, ahorro = calcular_precio(250, 20)
print(f'Precio: {final} Ahorras: {ahorro}')

final, ahorro = calcular_precio(150)
print(f'Precio: {final} Ahorras: {ahorro}')