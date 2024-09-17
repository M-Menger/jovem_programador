ang1 = float(input('Digite o primeiro angulo do triangulo: '))
ang2 = float(input('Digite o segundo angulo do triangulo: '))
ang3 = float(input('Digite o terceiro angulo do triangulo: '))

if(ang1 == 90 and ang2 != 90 and ang3 != 90 or ang2 == 90 and ang1 != 90 and ang3 != 90 or ang3 == 90 and ang2 != 90 and ang1 != 90):
    print('Triangulo Retângulo!')
elif(ang1 > 90 and ang2 != 90 and ang3 != 90 or ang2 > 90 and ang1 != 90 and ang3 != 90 or ang3 == 90 and ang2 != 90 and ang1 != 90):
    print('Triangulo Obtusângulo!')
elif(ang1 < 90 and ang2 < 90 and ang3 < 90):
    print('Triangulo Acutângulo!')
else:
    print('[Erro]')