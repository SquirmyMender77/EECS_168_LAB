favored_points=float(input("How many points is your team favored by? "))
home_game_identifier=input("Is it a home game? (enter h or H, anything else is an away game) ").lower()
bengals_checker=input("Is it the bengals? (y or Y for yes, anything else is no) ").lower()

if bengals_checker==('y'):
    print("No! No! No!")


elif favored_points>=7.5:
    print("SLAM IT!")

elif 3<=favored_points<7.5 and home_game_identifier==('h'):
    print("Good Bet")
elif 3<=favored_points<7.5:
    print("Okay Bet")
elif 3>favored_points>0 and home_game_identifier==('h'):
    print("Highly Risky")
elif 3>favored_points>0:
    print("Don't Bet!")
elif favored_points<0 and home_game_identifier==('h'):
    print("Don't Bet!")
else:
    print("Impossible")
