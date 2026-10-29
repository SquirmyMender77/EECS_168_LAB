def print_menu():
    print(f"1) Last digit\n2) Remove Last Digit\n3) Add Digit\n4) Count Digits\n5) Sum Digits\n6) Palindrome\n7) Reverse\n8) Exit")
def last_digit(user_num):
    print(user_num%10)
def remove_last_digit(user_num):
    print(user_num//10)  
def add_digit(user_num, new_digit):
    added_digit=(f'{user_num}{new_digit}')
    print(added_digit)
def count_digits(user_num):
    print(len(str(user_num)))
def sum_digits(n: int) -> int:
    total = sum(int(user_num) for user_num in str(n)) if n>0 else 0
    print(total)      
def is_palindrome(user_num):
   num_str = str(user_num)
   return num_str == num_str[::-1]
def reverse(user_num: int) -> int:
    return int(str(user_num)[::-1])
def main():
    while True:
        print_menu()
        choice=int(input("Pick a choice: "))
        if choice ==1:
            user_num=int(input("Pick a positive number: "))
            last_digit(user_num)
        elif choice ==2:
            user_num=int(input("Pick a positive number: "))
            remove_last_digit(user_num)
        elif choice ==3:
            user_num=int(input("Pick a positive number: "))
            new_digit=int(input("Pick a number to add onto the OG num: "))
            add_digit(user_num, new_digit)
        elif choice ==4:
            user_num=int(input("Pick a positive number: "))
            count_digits(user_num)
        elif choice ==5:
            user_num=int(input("Pick a positive number: "))
            sum_digits(user_num)
        elif choice ==6:
            user_num=int(input("Pick a positive number: "))
            print(is_palindrome(user_num))
        elif choice ==7:
            user_num=int(input("Pick a positive number: ").strip())
            number =int(user_num)
            reversed_number=reverse(number)
            print(reversed_number)
        else:
            break
if __name__ == "__main__":
    main()
