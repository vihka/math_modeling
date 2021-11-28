import math
import p3_t1 as pc
h = 100
alpha = math.pi/3
betha = 30
g = pc.g
betha_rad = math.radians(betha)
skobka = 1 - math.tan(betha_rad)*math.tan(alpha)
v_up = g*h*(math.tan(betha_rad)**2)
v_dn = 2*((math.cod(alpha))**2)*skobka
v = math.sqrt(v_up/v_dn)
print(v)
T = 200
epsylon = 300
k = pc.k
hp = pc.h
N1 = 2/math.sqrt(math.pi)
N2 = hp/(k*T)**(3/2)
N3 = math.exp(-epsylon/(k*T))
N4 = math.exp(T/2)
N = N1 * N2 * N3 * N4
print(N)