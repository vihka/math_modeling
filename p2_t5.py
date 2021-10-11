a = int(input())
b = int(input())
if b != 0 and a % b == 0:
  print(f'Число {a} делится на число {b} без остатка. Ответ: {a/b}')
elif b != 0 and a % b != 0:
  print(f'Число {a} делится на число {b} с остатком {a % b}. Частное: {a // b}')
else:
  print('На нуль делить нельзя')