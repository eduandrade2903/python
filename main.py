import math
import random

def calculaMedia():
    print("Digite a primeira nota: ")
    n1 = int(input())
    print("Digite a segunda nota: ")
    n2 = int(input())
    resultado = n1 + n2 / 2 
    if resultado < 6: 
        print("Você reprovou")
    else:
        print("Voce está aprovado")
    return resultado
    
def converterUnidade():
    grau = float(input("Digite um valor para fazer a conversao para Fahrenheit: "))
    calculoConversao = (grau * 1.8) + 32
    print("a conversão do grau", grau,"°", " para F. é igual a", calculoConversao, "°")
    return calculoConversao
    
def geradorDeLista():
    lista_Numeros = []
    numeroMinimo = int(input("Digite um numero minimo de intervalo"))
    numeroMaximo = int(input("Digite um numero maximo de intervalo"))
    for x in range(0,6):
        lista_Numeros.append(random.randint(numeroMinimo, numeroMaximo))
    print(lista_Numeros)
    return lista_Numeros
    
def contadorPalavras():
    texto = str(input("Digite um texto para saber quantas palavras ela tem: "))
    print("O texto escolhido tem ",len(texto), "letras")


while True:
    print("Escolha uma das opcões\n1 - calcular média \n2 - Conversor de Unidades \n3 - gerador de lista \n4 - contador de palavras \n5 - encerrar programa")
    escolha  = int(input())
    match escolha:
        case 1:
            print("Calculando média")
            calculaMedia()
        case 2:
            print("Conversor de Unidades")
            converterUnidade()
        case 3:
            print("Gerador de lista ")
            geradorDeLista()
            
        case 4:
            print("Contador de letras")
            contadorPalavras()
        case 5:
            print("Encerrando.....")
            break
        case _:
            print("Opção inválida")
            break