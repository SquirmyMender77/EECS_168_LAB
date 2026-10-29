soda=int(input("How many sodas do you have? "))

Fridge_Cubes=soda//24
six_packs=(soda%24)//6
Singles=soda%6
print(f"Fridge Cubes: {Fridge_Cubes}")
print(f"Six-Packs: {six_packs}")
print(f"Singles: {Singles}")

print("$$Goodbye$$")
