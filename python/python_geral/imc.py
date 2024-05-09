def IMC(peso, altura):
    return peso/altura**2

def IMC_categoria(imc):
    if imc < 17:
        return "Muito abaixo do peso"
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Acima do peso"
    if imc < 35:
        return "Obesidade grau I"
    if imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    while True:
        try:
            peso_usuario = float(input("Digite seu peso: "))
            break
        except ValueError:
            print("Digite um valor numérico.")
    
    while True:
        try:
            altura_usuario = float(input("Digite sua altura: "))
            break
        except ValueError:
            print("Digite um valor numérico.")

    if peso_usuario > 0 and altura_usuario > 0:
        imc_usuario = IMC(peso_usuario, altura_usuario)
        print(IMC_categoria(imc_usuario))
    else:
        print("Utilize somente valores POSITIVOS")
    
main()