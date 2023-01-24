# For start date
import datetime as date
import datetime

# Function for new user
def reg_user():
    # User inputs new username and password
    reg_user_name = input("Enter your new username: ")
    reg_password = input("Enter your new password: ")
    # Request input of password confirmation
    confirm_password = input("Confirm Password: ")
    # Check if username and password already exist
    if reg_user_name == usernames:
        print("This username already exists")
    elif reg_password == passwords:
        print("This password already exists")
    # Check both new passwords are the same that they entered
    elif reg_password == confirm_password:
        print("New user added")
        # Open file to write to credentials inside
        with open("user.txt", "a") as out_file:
            # Variable with new user credentials
            new_user_data = (f"{reg_user_name};{reg_password}")
            # Write on a new line the stored credentials in the list
            out_file.write(f"\n{new_user_data}")


# Function for tasks
# user, title, description, start date, due date, status
###TO DO: validations for user inputs
def add_task():
    # So we can read which users exist
    with open("user.txt", "r") as read_task:
        # Declaring variables to booleans
        valid_username = False
        completed = False
        # While true loop
        while not valid_username:
            task_username = input("Name of person assigned to task: ")
            # If the user name entered is not in user.txt
            if task_username not in usernames:
                print("User does not exist. Please enter a valid username")
            else:
                valid_username = True
        # Only executes if true
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            task_compl = input("Is the task completed YES/NO: ").strip().capitalize()
            break
        # Current date using date
        curr_date = date.date.today()
        print(curr_date)
        # Opens task.txt and will append on new line
        with open("tasks.txt", "a") as task_file:
            # New variable with user inputs
            task_list_to_write = (f"{task_username};{task_title};{task_description};"
                                  f"{curr_date};{task_due_date};{task_compl}")
            # Writes inside tasks.txt
            task_file.write(f"\n{task_list_to_write}")
        print("Task successfully added.")


# Function to view all tasks from task.txt
def view_all():
    # Open tasks.txt read only
    with open("tasks.txt", "r") as read_task:
        for line in read_task:
            # Split line by ';' character to get task details
            task_list = line.strip().split(';')
            # Make new variables that uses indexing to get right order and info
            task_str = f"Task: \t\t\t\t {task_list[1]}\n"
            task_str += f"Assigned to: \t\t {task_list[0]}\n"
            task_str += f"Date Assigned: \t\t {task_list[4]}\n"
            task_str += f"Due Date: \t\t\t {task_list[3]}\n"
            task_str += f"Task Description: \n {task_list[2]}\n"
            task_str += f"Task Completed: \t\t\t {task_list[5]}\n"
            # Print task string
            print(task_str)


# Function to show tasks for that user
def view_mine(curr_user):
    # Lists
    tasks_found = []
    row_list = []
    counter = 0
    # Open tasks.txt read only
    with open("tasks.txt", "r") as read_task:
        # Variable to read lines
        t = read_task.readlines()
        for row in t:
            # Split line by ';' character to get task details
            task_list = row.strip().split(';')
            # Append to a list
            row_list.append(task_list)
            # Check if current user has a task
            if curr_user == task_list[0]:

                counter += 1
                print(f"{counter}")

                # Make new variables that uses indexing to get right order and info
                task_str = f"Task: \t\t\t\t {task_list[1]}\n"
                task_str += f"Assigned to: \t\t {task_list[0]}\n"
                task_str += f"Date Assigned: \t\t {task_list[4]}\n"
                task_str += f"Due Date: \t\t\t {task_list[3]}\n"
                task_str += f"Task Description: \n {task_list[2]}\n"
                task_str += f"Task Completed: \t\t\t {task_list[5]}\n"

                print(task_str)
                # Add task to list of tasks found for current user
                tasks_found.append(task_list)
        # Keep asking for a specific task until the user enters a valid task number or "-1"
        while True:
            specific_task = int(input("Enter which number task you want or -1 for main menu: "))
            if specific_task == -1:
                return menu
                break
            # If they call a task that is within the range
            elif specific_task > 0 and specific_task <= len(tasks_found):
                # After the user selects a specific task
                while True:
                    action = input("Enter 'complete' to mark the task as complete or 'edit' to edit the task: ")
                    # If they input complete
                    if action == "complete":
                        # Get the task details from the tasks_found list this will only
                        # change the specific task they want
                        task_list = tasks_found[specific_task - 1]
                        # Update to yes
                        task_list[5] = "yes"
                        # Write the updated task to the tasks.txt file
                        with open("tasks.txt", "w") as write_task:
                            for row in row_list:
                                # If row equals the required task then write and join
                                if row == tasks_found[specific_task - 1]:
                                    write_task.write(";".join(task_list) + "\n")
                                # Else write and join the rest of the list
                                else:
                                    write_task.write(";".join(row) + "\n")
                        print("Task marked as complete.")
                        return menu
                    # If user picks edit
                    elif action == "edit":
                        # Get the task details from the tasks_found list
                        task_list = tasks_found[specific_task - 1]
                        # Ask what the user wants to edit
                        while True:
                            field = input(
                                "Enter 'username' to edit the assigned user or 'duedate' to edit the due date: ")
                            if field == "username":
                                # User inputs new user
                                new_username = input("Enter the new username: ")
                                # Change username
                                task_list[0] = new_username
                                # Write the updated task to the tasks.txt file
                                with open("tasks.txt", "w") as write_task:
                                    for row in row_list:
                                        # If row equals the required task then write and join
                                        if row == tasks_found[specific_task - 1]:
                                            write_task.write(";".join(task_list) + "\n")
                                        # Else write and join the rest of the list
                                        else:
                                            write_task.write(";".join(row) + "\n")
                                print("Username updated.")
                                return menu
                            elif field == "duedate":
                                # User inputs new due date
                                new_duedate = input("Enter the new due date: ")
                                # Update the date
                                task_list[3] = new_duedate
                                # Write the updated task to the tasks.txt file
                                with open("tasks.txt", "w") as write_task:
                                    for row in row_list:
                                        # If row equals the required task then write and join
                                        if row == tasks_found[specific_task - 1]:
                                            write_task.write(";".join(task_list) + "\n")
                                        # Else write and join the rest of the list
                                        else:
                                            write_task.write(";".join(row) + "\n")
                                print("Due date updated.")
                                return menu
                            else:
                                print("Invalid input. Please try again.")
                        else:
                            print("Invalid input. Please try again.")
                    else:
                        print("Invalid task number. Please try again.")
            else:
                print("Invalid task number. Please try again.")


# Function to generate reports
def generate_report():
    # Initialize task overview variables
    total_tasks = 0
    completed_tasks = 0
    overdue_not_complete_tasks = 0
    not_completed_tasks = 0
    overdue = 0
    task_per_user = 0

    # Open tasks.txt file in read mode
    with open("tasks.txt", "r") as f:
        for line in f:
            # Split line by ';' character to get task details
            task_list = line.strip().split(';')
            # Increment total tasks count
            total_tasks += 1
            # Check how many tasks user has
            if task_list[0] == curr_user:
                    task_per_user += 1
            # Check if task is completed
            if task_list[5] == "yes":
                completed_tasks += 1
            # Check if task is not completed
            else:
                not_completed_tasks += 1

            # Check if task is overdue and not complete
            task_due_date = datetime.datetime.strptime(task_list[3], "%Y-%m-%d")
            # If date is overdue
            if task_due_date < datetime.datetime.now():
                # Increment overdue
                overdue += 1
            # Overdue and not complete
            if task_list[5] == "no" and overdue:
                overdue_not_complete_tasks += 1

    # Calculate percentage of tasks not completed and overdue
    not_completed_percent = not_completed_tasks / total_tasks * 100
    overdue_percent = overdue / total_tasks * 100

    # Open task_overview file in write mode
    with open("task_overview.txt", "w") as write_task_overview:

        # Write task overview data to file
        write_task_overview.write(f"Total tasks: {total_tasks}\n")
        write_task_overview.write(f"Completed tasks: {completed_tasks}\n")
        write_task_overview.write(f"Not completed tasks: {not_completed_tasks}\n")
        write_task_overview.write(f"Not completed and Overdue tasks: {overdue_not_complete_tasks}\n")
        write_task_overview.write(f"Not completed task percentage: {not_completed_percent:.2f}%\n")
        write_task_overview.write(f"Overdue task percentage: {overdue_percent:.2f}%\n")

        # Calculate percentage of tasks assigned/ been completed/ must be completed/ not complete and overdue
        task_user_percentage = task_per_user / total_tasks * 100
        tasks_completed = completed_tasks / task_per_user * 100
        tasks_to_be_completed = 100 - tasks_completed
        overdue_user_tasks = overdue / task_per_user * 100

    # Open user_overview file in write mode
    with open("user_overview.txt", "w") as write_user_overview:
        write_user_overview.write(f"Numbers of users: {total_tasks}\n")
        write_user_overview.write(f"Total number of tasks: {total_tasks}\n")
        write_user_overview.write(f"Number of tasks assigned to {curr_user}: {task_per_user}\n")
        write_user_overview.write(f"Percentage of tasks assigned to {curr_user}: {task_user_percentage:.2f}%\n")
        write_user_overview.write(f"Percentage of tasks assigned to {curr_user} "
                                    f"that have been completed: {tasks_completed:.2f}%\n")
        write_user_overview.write(f"Percentage of tasks assigned to {curr_user} "
                                    f"that need to be completed: {tasks_to_be_completed:.2f}%\n")
        write_user_overview.write(f"Percentage of tasks assigned to {curr_user} that have not "
                                    f"been completed and are overdue: {overdue_user_tasks:.2f}%\n")


# Create function do display stats
def display_stats():

    # Open both files so we can print all info for the report
    with open("task_overview.txt", "r") as task_overview_file, open("user_overview.txt", "r") as user_overview_file:
        print("--------------------- Report ---------------------")
        print("------user_overview.txt------")

        for line, content in enumerate(task_overview_file):
            print(content[:-1])
        print("------user_overview.txt------")

        for line, content in enumerate(user_overview_file):
            print(content[:-1])

# Function for exit
def exit():
    if menu == 'e':
        print('Goodbye!!!')


# Lists for log in
usernames = []
passwords = []
#====Log in section====
with open('user.txt', 'r') as file:

    for lines in file:
        # Strip line by ';'
        logged_data = lines.strip().split(';')

        usernames.append(logged_data[0])
        passwords.append(logged_data[1])

# Ask user for username and password
logged_in = False
# While logged = True loop
while not logged_in:
    # Ask user for credentials
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    # If invalid user name and password
    if curr_user not in usernames:
        print("This is a invalid username")
    elif curr_pass not in passwords:
        print("This is a invalid password")
    else:
        print("Login Successful!")
        logged_in = True

while True:
    # presenting the menu to the user if the condition is true and
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    # If statement for functions
    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(curr_user)
    elif menu == 'gr':
        generate_report()
    elif menu == 'ds':
        display_stats()
    else:
        exit()




# GENERATE REPORT
# Need to generate files task_overview and user_overview

