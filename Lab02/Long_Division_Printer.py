numerator=int(input("Enter a numerator: "))
denominator=int(input("Enter a denominator: "))
while True:
    if denominator==0:
        print("You know you can't do that, try again")
        

    else:
        remainder=(numerator%denominator)
        value=(numerator//denominator)
        print(f"{numerator} / {denominator} = {value} Remainder {remainder}")
        break
print("Shutting Down...")
