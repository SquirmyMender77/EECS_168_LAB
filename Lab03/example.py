i = 0
while i < 5:
    print(i)
    if i == 2:  # Restart condition
        print("Restarting loop...")
        i = 0  # Reset the loop variable
        continue
    i += 1
    
