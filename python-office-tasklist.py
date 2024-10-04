office_tasklist = []            # first define a list

def add_task():                 # define add function, ask for user input and set a variable task  
    task = input("Please insert a task you want to add to your office-tasklist: \n")
    if task:
        office_tasklist.append(task)
        print(f"The task {task} was added to your list.")
    else:
        print("Your tasklist is empty.")
add_task()

def show_tasklist():
    if office_tasklist == None:
        print("Your tasklist is empty.")
    else:
        for task in office_tasklist:
            print("Your tasklist:")        
            print(task)
show_tasklist()             
   



