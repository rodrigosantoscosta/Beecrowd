pi = 3.14159
A, B, C = input().split()
#print(A, B, C
A = float(A)
B = float(B)
C = float(C)

print("TRIANGULO: %0.3f" %((A * C)/2))
print("CIRCULO: %0.3f" %(pi * (C * C)))
print("TRAPEZIO: %0.3f" %( ((A + B) * (C)) / (2) ))
print("QUADRADO: %0.3f" %(B * B))
print("RETANGULO: %0.3f" %(A * B))