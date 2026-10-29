while True:
    print(f"1) Chceckboard\n2) Twin Islands\n3) Running Total\n4) Upper Left Triangle\n5) Upper Right Triangle\n6) Exit")
    choice=int(input("Choice: "))
    if choice==1:
        grid_size=int(input("Enter size of Grid(>=5): "))
        for i in range(grid_size):
            for j in range(grid_size):
                print("*", end="")
            print()
    elif choice==2:
        N=5
        for row in range(N):
            line = ""
            for column in range(N):
                if column == (N-1) -row:
                    line +="*"
                elif row<N//2 and column<N//2:
                    line +="!"
                elif row>N//2 and column>N//2:
                    line +="?"
                else:
                    line +="~"
            print(line)
                

    elif choice==3:
        def print_grid(rows=5,cols=5):
            for row in range(1,rows+1):
                current_row = [(row-1) * cols+col for col in range(1,cols+1)]
                print(",".join(map(str,current_row)))
        print_grid()

    elif choice==4:
        N=5
        for i in range(N):
            print("" * i, end="")
            print("*" * (N-i))
    elif choice==5:
        N=5
        for i in range(N):
            print(" " * i, end="")
            print("*" * (N-i))
    elif choice==6:
        print("Goodbye!")
        break
    else:
        print("Let's try this again.")
            
         
