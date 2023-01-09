# Importing date module to calc current date
from datetime import date
today = date.today()
# Current removes hyphens between the year-months-days to give me an int that I can use
current = (int(today.strftime("%Y%m%d")))

# Functions


def reg_user():
    user_list = []
    with open('user.txt', 'r') as users:
        lines = users.readlines()
        # looping through text file to store usernames in a list
        for line in lines:
            temp = line.strip().split(', ')
            # user_list is used to check if the username that is input is stored in the database
            user_list.append(temp[0])

    while True:
        new_username = input("Please enter a new username: ").lower()
        # Checking whether new user is already registered to the database
        if new_username in user_list:
            # Error message if username is already recognised
            print(
                f"The username {new_username} is already taken, please enter a new one.")
        # Proceed as normal if username is new
        elif new_username not in user_list:
            new_pass = input("Please enter a new password: ").lower()
            # password needs to be double checked before it is added to the DB
            pass_check = input(
                "Please check you have entered the right password: ").lower()

            if new_pass != pass_check:
                print("I'm sorry can you enter the information again please. \n")
            # If password is the same, append it to the user.txt file
            else:
                with open('user.txt', 'a') as users:
                    users.write(str(f"\n{new_username}, {new_pass}"))
                print("New user added to the database. \n")
        break


def add_task():

    user_list = []

    with open('user.txt', 'r') as users:
        lines = users.readlines()

        for line in lines:
            temp = line.strip().split(', ')
            user_list.append(temp[0])

    # User inputs to get information needed to add into the task .txt file
    while True:
        task_user = input(
            "Please enter the username of whom the task is being assigned to: ").lower()

        # Used a conditional statment to check if the username that was entered is stored in the .txt file
        if task_user not in user_list:
            print("This username isn't recognised, please try again.\n")

        else:
            break

    # If the username entered is correct then the program will ask the rest of the questions needed
    task_title = input(
        "Please enter the title of the task being assigned: ").capitalize()
    task_desc = input("Please enter a description of the task: ").capitalize()
    task_date = str(
        input("\nPlease enter the date the task is due in for: (YYYY-MM-DD) "))

    print("Task added to the database.\n")

    # Writing user inputs to the .txt file
    with open('tasks.txt', 'a') as tasks:
        tasks.write(
            str(f"{task_user}, {task_title}, {task_desc}, {today}, {task_date}, No\n"))


def view_all():

    with open('tasks.txt', 'r+') as tasks:
        for lines in tasks:

            va = lines.split(", ")
            # Using \t to indent format the strings into a presentable form
            # Calling on the position of the elements in the list to display the correct outcomes I want
            print("-----------------------------------------------------------------------------------------------------------\n")
            print(f"Task: \t\t\t\t {va[1]}")
            print(f"Assigned to: \t\t\t {va[0]}")
            print(f"Date assigned: \t\t\t {va[3]}")
            print(f"Due date:\t\t\t {va[4]}")
            print(f"Task complete? \t\t\t {va[5]}")
            print(f"Task description:\n {va[2]}\n")
            print("-----------------------------------------------------------------------------------------------------------")


# The view_mine function should receive the username as a parameter
def view_mine(username):
    total_tasks = []
    task_list = []
    num = 1
    with open('tasks.txt', 'r') as tasks_txt:
        for lines in tasks_txt:
            temp = lines.strip().split(', ')
            # One to count total amount of tasks
            if temp[0] == username:
                # The rest of the tasks assigned to the user are placed in the task_list
                task_list.append(temp)

                # Using \t to indent format the strings into a presentable form
                # Calling on the position of the elements in the list to display the correct outcomes I want
                print(
                    "-----------------------------------------------------------------------------------------------------------\n")
                print(f"Task {num}: \t\t\t {temp[1]}")
                print(f"Assigned to: \t\t\t {temp[0]}")
                print(f"Date assigned: \t\t\t {temp[3]}")
                print(f"Due date:\t\t\t {temp[4]}")
                print(f"Task complete? \t\t\t {temp[5]}")
                print(f"Task description:\n {temp[2]}\n")
                print(
                    "-----------------------------------------------------------------------------------------------------------\n")
                # Counter used in f strings when printing out the users tasks
                num += 1
            if temp[0] != username:
                # I start off by appending all other items not assigned with the user to total_tasks
                total_tasks.append(temp)

        # The rest of the tasks assigned to the user are placed in the task_list

        while True:
            choice = input(
                "Would you like to select a task to edit (Yes/No): ").upper()
            if choice == "NO":
                break
            if choice == "YES":
                task_num = int(
                    input("Select which Task you would like to edit: "))
                # creating a variable to refer to the task that the user selects (-1 as the elements start from position 0)
                try:
                    task = task_list[task_num - 1]
                except IndexError:
                    print(
                        "\nSelected task doesn't exist, press -1 to return to the menu\n")
                    task_num == -1
                    pass

                _edit_task = input('''Would you like to:
                                        e - edit task
                                        c - mark as complete
                                        -1 - return to the main menu\n''')

                if _edit_task == 'e':
                    if task[5] == "Yes":
                        print("This task has already been completed")

                    elif task[5] == "No":

                        edit_option = input('''What would you like to edit?:
                                                        u - username
                                                        d - due date\n''')
                        if edit_option == "u":
                            task[0] = input("Please enter the new user here: ")
                            total_task_list = total_tasks + task_list
                            print(total_task_list)

                            with open('tasks.txt', 'w') as f:
                                # Before finally concatenating both lists and overwriting it to the tasks.txt file
                                for line in total_task_list:
                                    f.write(
                                        f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}\n")

                        elif edit_option == "d":
                            task[4] = input(
                                "Please enter the new date here (YYYY-MM-DD): ")
                            total_task_list = total_tasks + task_list
                            print(total_task_list)

                            with open('tasks.txt', 'w') as f:
                                for line in total_task_list:
                                    f.write(
                                        f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}\n")
                        else:
                            print("I did not recognise that!")

                    elif _edit_task == 'c':
                        if task[5] == "Yes":
                            print("This task has already been completed")

                        elif task[5] == 'No':
                            task[5] = "Yes"
                            total_task_list = total_tasks + task_list
                            print(total_task_list)

                            with open('tasks.txt', 'w') as f:
                                for line in total_task_list:
                                    f.write(
                                        f"{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}\n")

                    elif task_num == -1:
                        break

                    else:
                        break


def generate_reports():
    task_overview = open('task_overview.txt', 'w')
    user_overview = open('user_overview.txt', 'w')

    # Counters/Lists i'm using to work out the data that is being generated to task_overview and user_overview
    task_list = []
    tasks_completed = []
    tasks_not_completed = []
    overdue = []
    num = 0

    user_tasks = []
    assigned_to_user = 0
    completed_by_user = 0
    not_completed_by_user = 0
    overdue_by_user = 0

    with open('tasks.txt', 'r') as tasks:
        for lines in tasks:
            # Replacing hyphens with empty spaces so that the dates from the file are reas as a series of numbers
            temp = lines.strip().replace('-', '').split(', ')

            task_list.append(temp[5])

            # appending dates to a list
            overdue.append(temp[4])

            user_tasks.append(temp[0])

            # Calculating amount of completed tasks
            if temp[5] == "Yes":
                tasks_completed.append(temp)
            # Same for uncompleted tasks
            elif temp[5] == "No":
                tasks_not_completed.append(temp)
            # How many tasks the User has completed
            if username == temp[0] and temp[5] == "Yes":
                completed_by_user += 1
            # How many tasks the user hasn't completed
            if username == temp[0] and temp[5] == "No":
                not_completed_by_user += 1
            # How many tasks assigned to the user which are overdue
            # Casting the dates inside the file to an interger so they can be worked on
            if username == temp[0] and temp[5] == "No" and int(temp[4]) < current:
                overdue_by_user += 1

        for values in overdue:
            # if dates in list are less than current date, mark the task as overdue
            if int(values) < current:
                num += 1

        for values in user_tasks:
            if username == values:
                # Calculating how many tasks are assigned to the user who is currently logged in
                assigned_to_user += 1

    user_list = []

    with open('user.txt', 'r') as users:
        for lines in users:
            user_list.append(lines[0])
    # taking out last element of task_list so that it has the correct number assigned to it
    task_list.pop()
    total_tasks = len(task_list) + 1

    # Workings out for task_overview
    count_not_complete = len(tasks_not_completed)
    percent_not_complete = round((count_not_complete / total_tasks) * 100)
    percent_overdue_not_complete = round((num / total_tasks) * 100)

    # Workings out for user_overview
    percent_assigned_to_user = round((assigned_to_user / total_tasks) * 100)
    percentage_completed_by_user = round(
        (completed_by_user / assigned_to_user) * 100)
    percentage_not_completed_by_user = round(
        (not_completed_by_user / assigned_to_user) * 100)
    percentage_overdue_user = round((overdue_by_user / assigned_to_user) * 100)

    # Formatting strings and writing to file so when I call on the contents of file it is displayed in a presentable way

    task_overview.write("Task Overview:\n"
                        f"Total amount of tasks that have been assigned to date is: {total_tasks}\n"
                        f"Total number of completed tasks at the moment is: {len(tasks_completed)}\n"
                        f"Total number of tasks which still need to be completed is: {count_not_complete}\n"
                        f"Percentage of tasks which are currently incomplete is: {percent_not_complete}%\n"
                        f"Number of tasks which are currently overdue is: {num}\n"
                        f"The percentage of tasks that are overdue is: {percent_overdue_not_complete}%"
                        )

    # Formatting strings and writing to file so when I call on the contents of file it is displayed in a presentable way

    user_overview.write("User overview\n"
                        f"The total number of users registered with task_manager.py is {len(user_list)}\n"
                        f"Total amount of tasks that have been assigned to date is: {total_tasks}\n"
                        f"The total amount of tasks assigned to you is: {assigned_to_user}\n"
                        f"The percentage of the total number of tasks assigned to you is : {percent_assigned_to_user}%\n"
                        f"The percentage of tasks you have been assigned which are complete is: {percentage_completed_by_user}%\n"
                        f"The percentage of tasks assigned which you need to complete is: {percentage_not_completed_by_user}%\n"
                        f"The percentage of the tasks assigned which are not completed and are still overdue is: {percentage_overdue_user}%"
                        )

    # Closing both files after I've written data to them to save memory
    task_overview.close()
    user_overview.close()


def stat():
    with open('task_overview.txt', 'r') as t_overview:
        for lines in t_overview:
            print(lines)

    print("\n")

    with open('user_overview.txt', 'r') as r_overview:
        for lines in r_overview:
            print(lines)

    # appending a task on each line of the text file so that I can calculate the length of the list
    # This will allow me to display the number of tasks currently ongoing to the admin.


# Executable

user_list = []
pass_list = []

with open('user.txt', 'r') as users:
    lines = users.readlines()

    for line in lines:
        temp = line.strip().split(', ')

        user_list.append(temp[0])
        pass_list.append(temp[1])

    while True:

        username = input("Please enter your username: ").lower()

        # If username isn't recognised, it resets user back to step 1 and they have to re-enter username
        if username not in user_list:
            print("\nThis username isn't recognised, please try again.\n")

        elif username in user_list:
            password = input("\nPlease enter your password: ").lower()
            # If password isn't recognised resets user back to step 1
            if password not in pass_list:
                print("The password wasn't recognised, please try again. \n")
            
            elif (user_list[i] == username and pass_list[i] == password for i in range(len(user_list))):
                break


while True:
    if username != "admin":

        menu = input('''Select one of the following Options below:
                    a - Adding a task
                    va - View all tasks
                    vm - View my task
                    gr- generate reports
                    e - Exit
                    : ''').lower()
    # two different menu's for 2 types of registered user, Admin and registered users
    elif username == "admin":

        menu = input('''Select one of the following Options below:
                    r - Registering a user
                    a - Adding a task
                    va - View all tasks
                    vm - View my task
                    gr - Generate reports
                    s - Display stats
                    e - Exit
                    : ''').lower()

    while True:

        if menu == 'r' and username == "admin":
            reg_user()
            print("\n")
            break

        elif menu == 'a':
            add_task()
            print("\n")
            break

        elif menu == 'va':
            view_all()
            print("\n")
            break

        elif menu == 'vm':
            view_mine(username)
            break

        elif menu == 'gr':
            generate_reports()
            break

        elif menu == 's' and username == "admin":
            stat()
            print("\n")
            break

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
            break
