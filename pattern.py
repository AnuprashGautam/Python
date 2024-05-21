lines = int(input("Enter the number of lines: "))
print("Enter -1 for exit.")
print("Enter 1 for window pattern.")
print("Enter 2 for upright star pattern.")
print("Enter 3 for downward star pattern.")

while True:
    choice = int(input("Enter your choice: "))

    if choice == -1:
        break
    elif choice == 1:
        for i in range(1, lines + 1):
            for j in range(1, lines + 1):
                if i == 1 or i == lines or j == 1 or j == lines:
                    print("*",end=" ")
                else:
                    print(" ", end=" ")
            print()
                
    elif choice == 2:
        for i in range(1, lines + 1):
            print("*" * i)
            print()
    elif choice == 3:
        for i in range(lines, 0, -1):
            print("*" * i)
            print()
    else:
        print("Invalid choice.")
