import math

x1, y1 = map(float, (input().split()))
x2, y2 = map(float, (input().split()))
distancia = math.sqrt((x1 * x1) - (2 * x1 * x2) + (x2 * x2) + (y1 * y1) - (2 * y1 * y2) + (y2 * y2))
                   
print("%0.4f" %distancia)