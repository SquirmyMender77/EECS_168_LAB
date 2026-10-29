def display_board(N, rook_row, rook_col):
    for row in range(N):
        line=""
        for col in range(N):
            if rook_row==row and rook_col==col:
                print("R", end="")
            elif row==rook_row:
                print("-", end="")
            elif col==rook_col:
                print("|", end="")
            else:
                print("*", end="")
        print(line)
        
def main():
    N = int(input("Enter board size(N): "))
    rook_row= int(input("Enter rook row(1-N): ")) -1
    rook_col = int(input("Enter rook column (1-N): ")) -1

    display_board(N, rook_row, rook_col)

if __name__=="__main__":
    main()
