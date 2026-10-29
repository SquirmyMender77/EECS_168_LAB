interface=print(f"1) Select a specific number\n2) Display Visible ASC|| values (33 to 126)\n3) Exit")
while True:
    choice=int(input("Choice: "))
    if choice==1:
        value=int(input("Enter value: "))
        print(f"{value} = {chr(value)}")
    for i in range(33,127):
        if choice==2:
            print(i, "=", chr(i))
    else:
        print("And stay out!")
        break
                  
            
        
            
            
    
