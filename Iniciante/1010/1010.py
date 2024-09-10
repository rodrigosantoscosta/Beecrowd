first_product = input().split()
code_1 = int(first_product[0])
unit_1 = int(first_product[1])   
price_1 = float(first_product[2])
#print(first_product)
#print(unit_1

#print("VALOR A PAGAR: R$%0.2f " %(unit_1 * price_1))
second_product = input().split()
code_2 = int(second_product[0])
unit_2 = int(second_product[1])
price_2 = float(second_product[2])
print("VALOR A PAGAR: R$ %0.2f" %((unit_1 * price_1) + (unit_2 * price_2)))