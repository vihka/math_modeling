#Создать функцию, строящую графики кривых второго порядка, заданных явно: Парабола Гипербола на вход, функции подаются: пределы изменения переменной (xa, xb), количество точек N, на которое разбиваются соответствующие пределы, необходимые параметры a, b, c, … и название графика.
import matplotlib.pyplot as plt
import numpy


Xa = int(input("Отрицательное пжпжпжпжп:"))
Xb = int(input())
N = int(input())
a = int(input()) 
b = int(input())
c = int(input())
k = int(input('Неравное нулю:'))

def parabola(a, b, c, k, Xa, Xb, N,  title = 'Парабола и Гипербола'):
  x = numpy.linspace(Xa, Xb, N)
  y = a * x ** 2 + b * x + c

  plt.plot(x, y, label = 'Парабола, Finally!')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(title)
  plt.legend()
  plt.show()

#parabola(a, b, c, k, Xa, Xb, N)

def hyperbola(k, Xa, Xb, title = 'Гипербола'):
  x1 = numpy.linspace(Xa,Xb, N)
  y1 = k / x1
  
  x2 = x1[y1 == 0]
  y2 = y1[y1 == 0]
  
  y3 = numpy.ma.masked_where(abs(y1) <= 0.0001, y1)
  x3 = numpy.ma.masked_where(abs(x1) <= 0.0001, x1)

  plt.plot(x3, y3, label = 'Гипербола, Ура!')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title(title)
  plt.legend()
  plt.show()

hyperbola(k, Xa, Xb) 
#разкомментируй чтоб увидеть Гиперболу и закоментируй параболу
