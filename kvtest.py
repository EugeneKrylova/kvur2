# kvur 2
from math import sqrt
baddata = True
while baddata == True:
    try:
        a = int(input('Введите a: '))
        b = int(input('Введите b: '))
        c = int(input('Введите c: '))
        baddata = False
    except:
        print('Не удалось получить данные')

D = (b*b)-(4*a*c)

if D > 0:

    d = sqrt(D)
    Х1 =((-b)+d)/(2*a)
    Х2 =((-b)-d)/(2*a)
    print(f'Уравнение имеет два корня X1 ={X1}, X2 ={Х2}')
elif D == 0:
    Х1 =(-b)/(2*a)
    print(f'Уравнение имеет один корень X1 ={X1}')
else:
    print('Уравнение не имеет корней')