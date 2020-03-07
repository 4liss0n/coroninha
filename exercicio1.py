
nome = input(print("qual o seu nome? "))
idade = int(input(print("qual a sua idade? ")))
if idade <= 15:
    print("tu tem chance de pegar corona")
elif idade >= 60:
    print("tu tem chance de pegar corona")
else:
    print("tá suave, mas toma cuidado")
risco = input(print("você tem algum outro tipo de doença? s/n")).upper()
if risco == "S":
    print("então fudeu muito")
elif risco == "N":
    print("tá tranquilo, mas se cuida")
else:
    print("não vou poder te ajudar, sinto muito")