n = int(input())
a, b, c = 0, 1, 1
s = str()
for i in range(n + 1):
    s += str(c) + " "
    c = a + b
    a = b
    b = c
print(s)