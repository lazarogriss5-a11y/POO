#Calculadora de IMC
peso = 50 #kg
altura = 1.60 #metros

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:2f}")

if imc < 19.5:
    print("Bajo de peso")

elif imc < 25:
    print("Peso normal")

else: imc < 30
print("Obesidad")