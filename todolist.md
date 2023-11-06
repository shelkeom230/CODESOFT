# ToDo List Application using Tkinter and MySQL

This is a simple ToDo list application created using Tkinter for the GUI and MySQL for the database. It allows users to add, delete, edit, and sort tasks based on date and time.

## Installation

To run this application, you need to have Python and MySQL installed on your system. Additionally, you need to install the `mysql-connector-python` package. You can install it using the following command:

run this command to install connector for python mysql :
pip install mysql-connector-python

Instructions for setup: 


## Setup

1. Create a MySQL database named `todolist`.
2. Create a table named `tasks` in the `todolist` database with the following attributes:
    - `srno` (INT, AUTO_INCREMENT, PRIMARY KEY)
    - `task_name` (VARCHAR(255))
    - `date_time` (DATETIME)

3. Update the `yourusername` and `yourpassword` in the code with your MySQL username and password.

## Usage

Run the `todo_list_app.py` file to launch the application. You can add tasks using the "Add Task" button, delete tasks using the "Delete Task" button, and edit tasks using the "Edit Task" button.

Screenshots: 
![image](https://github.com/shelkeom230/CODESOFT/assets/104075298/55ec6143-31db-42e0-9fad-1156e9716587)
![image](https://github.com/shelkeom230/CODESOFT/assets/104075298/ef29c960-4337-4dce-83fa-c530e3317a64)


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
