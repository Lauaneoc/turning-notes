
def CalculaNotaFinal(a):
    if a > 9:
        nota=  'A'
    elif a > 7 <= 9:
        nota= 'B'
    elif a >= 6 <= 7:
        nota = 'C'
    elif a < 6:
        nota = 'R'
    return nota

a = int(input('Digite sua nota:'))

nota = CalculaNotaFinal(a)

print('A nota final é:', nota)

#01
a= 3 
nota = CalculaNotaFinal(a)
print('Quando o valor da nota for 3, o resultado final será:', nota)

#02
a= 10
nota = CalculaNotaFinal(a)
print('Quando o valor da nota for 10, o resultado final será:', nota)

#03
a= 7
nota = CalculaNotaFinal(a)
print('Quando o valor da nota for 7, o resultado final será:', nota)

#04
a= 1
nota = CalculaNotaFinal(a)
print('Quando o valor da nota for 1, o resultado final será:', nota)

#05
a= 6
nota = CalculaNotaFinal(a)
print('Quando o valor da nota for 6, o resultado final será:', nota)






    
        
 