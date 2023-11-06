import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

# Establish a connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="todolist"
)

# Create a cursor
mycursor = mydb.cursor()

# Create a table if it doesn't exist
mycursor.execute("CREATE TABLE IF NOT EXISTS tasks (srno INT AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), date_and_time DATETIME)")

# Function to show tasks in the treeview
def show_tasks():
    mycursor.execute("SELECT * FROM tasks ORDER BY date_and_time")
    records = mycursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for i, (srno, task_name, date_and_time) in enumerate(records, start=1):
        tree.insert("", "end", values=(srno, task_name, date_and_time))

# Function to add tasks to the database
def add_task():
    task_name = task_entry.get()
    date_and_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO tasks (task_name, date_and_time) VALUES (%s, %s)"
    val = (task_name, date_and_time)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Task Added", "Task has been added successfully")
    show_tasks()

# Function to delete a selected task
def delete_task():
    selected_task = tree.focus()
    if selected_task:
        task_id = tree.item(selected_task)['values'][0]
        mycursor.execute("DELETE FROM tasks WHERE srno=%s", (task_id,))
        mydb.commit()
        messagebox.showinfo("Task Deleted", "Task has been deleted successfully")
        show_tasks()

# Function to edit tasks
def edit_tasks():
    selected_task = tree.focus()
    if selected_task:
        task_id = tree.item(selected_task)['values'][0]
        new_task_name = task_entry.get()
        date_and_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mycursor.execute("UPDATE tasks SET task_name = %s, date_and_time = %s WHERE srno = %s", (new_task_name, date_and_time, task_id))
        mydb.commit()
        messagebox.showinfo("Task Updated", "Task has been updated successfully")
        show_tasks()
        task_entry.delete(0, 'end')

# Create the main application window
root = tk.Tk()
root.title("ToDo List Application by Omkar Shelke")
root.configure(bg='green')


# Create a treeview
tree = ttk.Treeview(root, columns=("srno", "task_name", "date_and_time"), show="headings")
tree.heading("srno", text="Sr. No.")
tree.heading("task_name", text="Task Name")
tree.heading("date_and_time", text="Date and Time")
tree.pack(padx=20, pady=20)

# Add some sample data to the treeview
show_tasks()

# Add Task section
task_label = ttk.Label(root, text="Task Name")
task_label.pack(pady=5)
task_entry = ttk.Entry(root, width=30)
task_entry.pack(pady=5)
add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Delete Task section
delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Edit Task section
edit_button = ttk.Button(root, text="Edit Task", command=edit_tasks)
edit_button.pack(pady=5)

# Exit section
exit_button = ttk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

# Run the main event loop
root.mainloop()
