# Task_Manager

This code is a script for managing tasks and users on a command-line interface. The script has several functions including:

"reg_user()" which allows a new user to register by entering a new username and password, which are then checked for availability and confirmed before being added to the "user.txt" file.


"add_task()" which allows a registered user to add a task by inputting the task's title, description, due date, and completion status, along with the current date. These inputs are then added to the "tasks.txt" file with the assigned user's name.

"view_all()" which displays all tasks stored in the "tasks.txt" file.

"view_mine(curr_user)" which displays all tasks assigned to the current user.
It also uses the "datetime" library to get the current date.

"generate_report" which will generate two .txt files called user_overview and task_overview. task overview will include; Total tasks, completed tasks, not completed tasks, not completed adn overdue and overdue %.

User overview will include; Num of users, total num of tasks, how many tasks are assigned to them/ % that has been completed/ % that need to be completed/ % that are not completed and overdue.

"display_stats()" which displays all statistics of the file from the user_overview and task_overview reports
