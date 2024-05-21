lines = int(input("Enter the number of lines: "))
print("Enter -1 for exit.")
print("Enter 1 for combined diamond pattern.")
print("Enter 2 for upright diamond pattern.")
print("Enter 3 for downward diamond pattern.")

while True:
    choice = int(input("Enter your choice: "))

    if choice == -1:
        break

    elif (choice==1):

        if(lines%2==0):                #even number of lines
            hlines=int(lines/2)
            for i in range(hlines,-1,-1):    
                print(" "*i,end="")        #for printing the space
                print("* "*(hlines-i))       #for printing the asterisk
            for i in range(hlines,0,-1):   
                print(" "*(hlines-i),end="")        #for printing the space
                print("* "*i)                      #for printing the asterisk

        else:                          #odd number of lines
            hlines=int(lines/2)
            for i in range(hlines,-1,-1):    
                print(" "*(i+1),end="")        #for printing the space
                print("* "*(hlines-i))     #for printing the asterisk
            
            print("* "*(int(lines/2)+1))    #for midline

            for i in range(hlines,0,-1):   
                print(" "*(hlines-i+1),end="")        #for printing the space
                print("* "*i)                      #for printing the asterisk



    elif (choice==2):
        for i in range(lines,-1,-1):    
            print(" "*i,end="")        #for printing the space
            print("* "*(lines-i))       #for printing the asterisk
        
    elif (choice==3):
        for i in range(lines,0,-1):   
            print(" "*(lines-i),end="")        #for printing the space
            print("* "*i)                      #for printing the asterisk
                   

    else:
        print("Invalid Choice")
            