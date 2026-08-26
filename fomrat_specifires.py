# format specifiries = {value:flags} format a value based on what flags are inserted

# .(number) f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces 
# :< = left justify 
# :> = rigth justify
# :^ = center align 
# :+ = use a plus sign to indicate positive values
# := = place sign to leftmost position 
# :  = insert a space before positive numbers
# :, = comma separator 


price1 = 30000000.14159
price2 = -987.65
price3 = 200000.34

# print(f"price 1 is ${price1:.2f}")
# print(f"price 2 is ${price2:.2f}")
# print(f"price 3 is ${price3:.2f}")

# print(f"price 1 is ${price1:10}")
# print(f"price 2 is ${price2:10}")
# print(f"price 3 is ${price3:10}")

# print(f"price 1 is ${price1:010}")
# print(f"price 2 is ${price2:010}")
# print(f"price 3 is ${price3:010}")

# print(f"price 1 is ${price1:<10}")
# print(f"price 2 is ${price2:<10}")
# print(f"price 3 is ${price3:<10}")

# print(f"price 1 is ${price1:>10}")
# print(f"price 2 is ${price2:>10}")
# print(f"price 3 is ${price3:>10}")

# print(f"price 1 is ${price1:^10}")
# print(f"price 2 is ${price2:^10}")
# print(f"price 3 is ${price3:^10}")

# print(f"price 1 is ${price1:+}")
# print(f"price 2 is ${price2:+}")
# print(f"price 3 is ${price3:+}")

# print(f"price 1 is ${price1: }")
# print(f"price 2 is ${price2: }")
# print(f"price 3 is ${price3: }")

# print(f"price 1 is ${price1:,}")
# print(f"price 2 is ${price2:,}")
# print(f"price 3 is ${price3:,}")

print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")