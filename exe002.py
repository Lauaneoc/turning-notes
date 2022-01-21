def calculaRentabilidade(a):
    if a <= 20000:
        taxa = 7
    elif a > 20000 <= 50000:
        taxa = 10
    elif a > 50000:
        taxa = 12
    resultado = a * taxa //100
    resultado_final = resultado + a
    return resultado_final

valorDoDeposito= float(input('Digite o valor do deposito:'))

rentabilidade = calculaRentabilidade(valorDoDeposito)

print('O valor da rentalidade é:', rentabilidade)

#01
Valor1Investido = 19000
rentabilidade1= calculaRentabilidade(Valor1Investido)
print('O valor do montante 1:',rentabilidade1)

#02
Valor2Investido = 30000
rentabilidade2= calculaRentabilidade(Valor2Investido)
print('O valor do montante 1:',rentabilidade2)

#03
Valor3Investido = 50000
rentabilidade3= calculaRentabilidade(Valor3Investido)
print('O valor do montante 1:',rentabilidade3)

#04
Valor4Investido = 52000
rentabilidade4= calculaRentabilidade(Valor4Investido)
print('O valor do montante 1:',rentabilidade4)



