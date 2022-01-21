def calculamenorvalor(a,b,c,d):
    if a < b and a < c and a < d:
        menor = a
    elif b < c and b < a and b < d:
        menor = b
    elif c < b and c < a and c < d:
        menor = c
    elif d < a and d < b and d < c:
        menor = d
    return menor

m1 = int(input('Digite o primeiro número'))
m2 = int(input('Digite o segundo número'))
m3 = int(input('Digite o terceiro número'))
m4 = int(input('Digite o quarto número'))

menor_valor = calculamenorvalor(m1, m2, m3, m4)

print('O menor valor é:', menor_valor)

#01
a1= 1
b1= 2
c1= 3
d1= 4
menor_valor1 = calculamenorvalor(a1,b1,c1,d1)
print('O menor valor é:', menor_valor1)

#02
a2= 40
b2= 30
c2= 20
d2= 10
menor_valor2 = calculamenorvalor(a2,b2,c2,d2)
print('O menor valor é:', menor_valor2)

#03
a3= 10
b3= 2
c3= -1
d3= 0
menor_valor3 = calculamenorvalor(a3,b3,c3,d3)
print('O menor valor é:', menor_valor3)