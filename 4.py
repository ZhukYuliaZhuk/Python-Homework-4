#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
#многочлена и записать в файл многочлен степени k
#k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
#Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

#Пример:
#k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
#k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint
max_val=100
k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# Поиск и замены:
poly=poly.replace('x^1+', 'x+')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print(poly)
