def convertem(md,d):
    if d == 'cm':
        converte = md * 100
    elif d == 'mm':
        converte = md * 1000
    elif d == 'km':
        converte = md // 1000
    return converte

medida_m = 100

print(medida_m, 'm -', convertem(medida_m, 'cm'), 'cm')
print(medida_m, 'm -', convertem(medida_m, 'mm'), 'mm')
print(medida_m, 'm -', convertem(medida_m, 'km'), 'km')
