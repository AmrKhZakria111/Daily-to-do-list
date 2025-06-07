import sqlite3
import sys
from tkinter import *
from tkinter import ttk
from database import get_tasks, delete_task
import subprocess

# Get user ID from command-line arguments
user_id = int(sys.argv[1])

def refresh_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()
    tasks = get_tasks(user_id)
    row = 0
    column = 0
    for task in tasks:
        task_id, day, category, time, details = task
        add_task(task_id, day, category, time, details, row, column)
        column += 1
        if column >= columns:
            column = 0
            row += 1

def clear_task(task_id):
    delete_task(task_id)
    refresh_tasks()

# Create the main window
root = Tk()
root.title("Daily Tasks")
root.geometry("925x500")  # Adjust the size as needed
root.configure(bg="white")
root.resizable(False, False)

# Define styles
style = ttk.Style()
style.configure("TButton", font=('Arial', 12), padding=10)
style.configure("TLabel", font=('Arial', 14))

# Create a frame for the canvas and scrollbar
frame = Frame(root, bg="white")
frame.pack(fill=BOTH, expand=True, pady=10)

# Create a canvas with a scrollbar
canvas = Canvas(frame, bg="white")
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Load the background image
background_image = PhotoImage(file='Webp.net-resizeimage (6).png')
background_label = Label(root , image=background_image , border=0)
background_label.place(x=0 , y=0)
# Create a canvas background
# canvas.create_image(0, 0, image=background_image ,anchor="nw")

# Create a frame within the canvas to hold the tasks
tasks_frame = Frame(root, bg="white")
tasks_frame.place(x=0 , y=0)

# canvas.create_window((0, 0), window=tasks_frame, anchor="nw")

# Ensure the grid columns and rows expand evenly
columns = 4
for i in range(columns):  # Adjust the range for the number of columns
    tasks_frame.columnconfigure(i, weight=1, uniform="col")
for i in range(10):  # Adjust the range for a reasonable number of rows initially
    tasks_frame.rowconfigure(i, weight=1, uniform="row")

# Function to add a new task
def add_task(task_id, day, category, time, task, row, column, color="#57a1f8"):
    task_frame = Frame(tasks_frame, bg="white", pady=5, padx=10, bd=1, relief=SOLID, height=500, width=500)  # Adjust height and width here
    task_frame.grid(row=row, column=column, padx=20, pady=20, sticky="nsew")  # Increase padding here
    
    Label(task_frame, text=category, bg=color, font=('Arial', 12, 'bold')).pack(fill=X)
    Label(task_frame, text=day, bg=color, font=('Arial', 12)).pack(fill=X)
    Label(task_frame, text=time, bg="white", font=('Arial', 12)).pack(fill=X)
    Label(task_frame, text=task, bg="white", font=('Arial', 12), wraplength=180, justify=LEFT).pack(fill=BOTH, expand=True)
    Button(task_frame, text="Clear", bg="red", fg="white", command=lambda: clear_task(task_id)).pack(fill=X)
    tasks_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Fetch tasks from the database and display them
refresh_tasks()

# External frame for adding tasks (example placeholder)
# Replace this with your actual frame and functionality
external_frame = Frame(root, bg="white", pady=10)
external_frame.pack(fill=X)

# Example function to simulate adding a task from an external frame
def simulate_add_task():
    subprocess.run(['python', 'frame3.py', str(user_id)])
    refresh_tasks()

Button(external_frame, text="Add Task", command=simulate_add_task, bg="#57a1f8", fg="white", font=('Arial', 12)).pack()

# Update scrollregion after adding tasks
tasks_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Run the application
root.mainloop()
