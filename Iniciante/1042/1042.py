x,y,z = map(int,input().split())
xCopia, yCopia, zCopia = x, y, z

if x > y:
    aux = x
    x = y
    y = aux

if x > z:
    aux = x
    x = z
    z = aux

if y > z:
    aux = y
    y = z
    z = aux

print(f'{x}\n{y}\n{z}\n\n{xCopia}\n{yCopia}\n{zCopia}')