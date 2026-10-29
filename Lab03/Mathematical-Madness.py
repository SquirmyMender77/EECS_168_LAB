import math
while True:
    print(f"1) Summation\n2) Product\n3) Odd Count\n4) Even Count\n5) Exit")
    choice=int(input("Choice: "))
    if choice==1:
        lower_bound=int(input("Enter Lower Bound: "))
        upper_bound=int(input("Enter Upper Bound: "))
        summation=print(sum(range(lower_bound,upper_bound+1)))
    elif choice==2:
        lower_bound2=int(input("Enter Lower Bound: "))
        upper_bound2=int(input("Enter Upper Bound: "))
        product=print(math.prod(range(lower_bound2,upper_bound2+1)))
    elif choice==3:
        lower_bound3=int(input("Enter Lower Bound: "))
        upper_bound3=int(input("Enter Upper Bound: "))
        for num in range(lower_bound3,upper_bound3+1, 2):
            print(num)
    elif choice==4:
       lower_bound4=int(input("Enter Lower Bound: "))
       upper_bound4=int(input("Enter Upper Bound: "))
       for num2 in range(lower_bound4+1,upper_bound4+1,2):
           print(num2)
    else:
        print("Goodbye!")
        break
