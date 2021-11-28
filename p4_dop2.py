def fibb(n):
  print(1)
  num1 = 1
  num2 = 1
  for i in range(n):
      num2 += num1
      num1, num2 = num2, num1
      print(num2)

fibb(10)