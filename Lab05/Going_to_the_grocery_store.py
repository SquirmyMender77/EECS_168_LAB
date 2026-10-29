shopping_list=[]
def cross_out(item):
    if len(item) <=2:
        return item
    return item[0] + '-' * (len(item)- 2) +item[-1]
while True:
    print(f"Welcome to the shopping list!\n1) Add item\n2) Check off item\n3) Print list\n4) Exit")
    choice=int(input("Choose an option: "))
    if choice==1:
        item=input("What are you putting on the list?: ")
        shopping_list.append(item)
        print(f"'{item}' added to the list")
            
    elif choice==2:
        if not shopping_list:
            print("The list is empty")
            continue
        print("\nWhich item did you get?: ")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}) {item}")
        try:
            index = int(input("Enter the number of item: ")) - 1
            if 0<= index<len(shopping_list):
                shopping_list[index] = cross_out(shopping_list[index])
        except ValueError:
            print("Please enter a valid number")
    elif choice==3:
        if not shopping_list:
            print("The list is empty")
        else:
            print("\nCurrent list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}) {item}")
    else:
        break
    
            
            
            
