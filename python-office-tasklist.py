office_tasklist = []            # first define a list

def add_task():                 # define add function, ask for user input and set a variable task  
    task = input("Please insert a task you want to add to your office-tasklist: \n")
    if task:
        office_tasklist.append(task)
        print(f"The task {task} was added to your list.")
    else:
        print("Your tasklist is empty.")


def show_tasklist():                        # define show tasklist function 
    if office_tasklist == None:             # check if tasklist is empty
        print("Your tasklist is empty.")
    else:
        for task in office_tasklist:        # enter a for -loop to print the input of the user
            print("Your tasklist:")        
            print(task)


def main():                                 # define main function
    while True:                             # while true do loop 
        print("1. Add a task.")             # define options a user can choose
        print("2. Show the list.")
        print("3. End the programm.")
        choice = input("Please make your choice. \n")   # ask user to make a choice
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            print("Goodbye.")
            break                           # break to end the while - loop
if __name__ == "__main__":                  # control function 
    main()        


   



