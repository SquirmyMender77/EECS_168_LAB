storage = []
while True:
    current_planet=input("Enter Planet name(all lowercase letters please): ")
    mission=input("Is the mission over? (y/n): ").strip().lower()
    storage.append(current_planet)
    if mission=="y":
        enumerated_list = list(enumerate(storage))
        print(enumerated_list)
        neighbors=int(input("Which planet do you want the neighbors for?(Enter the corresponding number): "))
        for index in range(1):
            if neighbors==0:
                    print(f"No planet was reached before {storage[neighbors]}.")
                    print(storage[neighbors+1])
            elif neighbors>0:
                try:
                    print(storage[neighbors-1])
                    print(storage[neighbors+1])
                except IndexError:
                    if index<neighbors:
                        print(f"No planet was reached after {storage[neighbors]}.")

        print("Program ending...")
        break
