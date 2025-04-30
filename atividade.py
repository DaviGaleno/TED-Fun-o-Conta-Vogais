
def conta_vogais (texto):
    vogais = 'AEIOUaeiou'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador +=1
    return contador

texto = (input("Digite uma palavra: "))
result = conta_vogais(texto)
print(f'O numero de vogais é result')