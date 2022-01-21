def calculaValor(a,b,c,):
    orçamento = a * b 
    orçamento_final = c * orçamento /100 + orçamento 
    return orçamento_final

a= int(input('Digite o tamanho da construção em metros quadrados:'))
b= int(input('Digite o valor da construção em metros quadrados:'))
c= int(input('Digite a margem de lucro da construtora'))

valor= calculaValor(a,b,c,)

print('O valor do orçamento é:', valor )

# 01
a= 150
b= 1500
c= 15

valor_do_orçamento1 = calculaValor(a,b,c)
print('O valor do orçamento é:', valor_do_orçamento1)

#02
a= 300
b= 2000
c= 12

valor_do_orçamento2 = calculaValor(a,b,c)
print('O valor do orçamento é:', valor_do_orçamento2)

#03
a= 380
b= 2100
c= 10

valor_do_orçamento3 = calculaValor(a,b,c)
print('O valor do orçamento é:', valor_do_orçamento3)