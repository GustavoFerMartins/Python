lados = [float(x) for x in input().split()]

a = lados[0]
b = lados[1]
c = lados[2]
perimetro = a + b + c
area = ((a + b) * c) / 2

if a + b > c and a + c > b and b + c > a:
    print(f"Perimetro = {perimetro:.1f}")
else:
    print(f"Area = {area:.1f}")