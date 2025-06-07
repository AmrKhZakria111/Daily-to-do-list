import sqlite3
import sys
from tkinter import *
from tkinter import messagebox
from database import add_task
 

# Get user ID and callback function from command-line arguments
user_id = int(sys.argv[1])

def add_subjects():
    subject_name = nameofsubject_txt.get()
    start_date = startdate_txt.get()
    start_time = starttime_txt.get()
    details = details_txt.get()
    
    if not subject_name or not start_date or not start_time or not details:
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    # Add task to the database
    if add_task(user_id, start_date, subject_name, start_time, details):
        messagebox.showinfo("Success", "Task added successfully")
        reset()
        # Call the callback function to refresh tasks in frame 4
        root.destroy()
    else:
        messagebox.showerror("Error", "Failed to add task")

def reset():
    nameofsubject_txt.delete(0, 'end')
    startdate_txt.delete(0, 'end')
    starttime_txt.delete(0, 'end')
    details_txt.delete(0, 'end')

root = Tk()
photo_frame = Frame(root, width=338, height=338, bg='#57a1f8')
middle_frame = Frame(root, width=350, height=350)
last_frame = Frame(root, width=320, height=150)
root.title('Add Tasks')
root.geometry("925x500")
root.configure(bg='#fff')
middle_frame.configure(bg='white')
last_frame.configure(bg='white')
root.resizable(False, False)

task_completed = PhotoImage(file="Webp.net-resizeimage (3).png")
lbl = Label(root, image=task_completed, border=0, bg='white')

subject_lbl = Label(root, text='TASKS', background='white', foreground='#57a1f8', font=("Microsoft YaHei UI Light", 25, "bold"))

nameofsubject_lbl = Label(middle_frame, text='Name Of Subject : ', background='#fff', fg='black', font=("Microsoft YaHei UI Light", 10))
nameofsubject_txt = Entry(middle_frame, background='#fff', width=25, fg='black', font=("Microsoft YaHei UI Light", 12), border=0)
Frame(middle_frame, width=310, height=2, bg='black').place(x=0, y=82)

startdate_lbl = Label(middle_frame, text='Start Date : ', background='#fff', fg='black', font=("Microsoft YaHei UI Light", 10))
startdate_txt = Entry(middle_frame, width=25, background='white', fg='black', font=("Microsoft YaHei UI Light", 12), border=0)
Frame(middle_frame, width=310, height=2, bg='black').place(x=0, y=152)

starttime_lbl = Label(middle_frame, text='Start Time: ', background='#fff', fg='black', font=("Microsoft YaHei UI Light", 10))
starttime_txt = Entry(middle_frame, width=25, background='white', fg='black', font=("Microsoft YaHei UI Light", 12), border=0)
Frame(middle_frame, width=310, height=2, bg='black').place(x=0, y=222)

details_lbl = Label(middle_frame, text='Details: ', background='#fff', fg='black', font=("Microsoft YaHei UI Light", 10))
details_txt = Entry(middle_frame, width=25, background='white', fg='black', font=("Microsoft YaHei UI Light", 12), border=0)
Frame(middle_frame, width=310, height=2, bg='black').place(x=0, y=292)

add_btn = Button(last_frame, text='ADD', width=18, fg="white", pady=8, cursor="hand2", border=0, bg='#57a1f8', command=add_subjects)
reset_btn = Button(last_frame, text='RESET', width=18, fg="white", border=0, cursor="hand2", pady=8, bg='#57a1f8', command=reset)

lbl.place(x=20, y=30)
subject_lbl.place(x=600, y=15)
middle_frame.place(x=480, y=70)
nameofsubject_lbl.place(x=0, y=50)
nameofsubject_txt.place(x=122, y=51)
startdate_lbl.place(x=0, y=120)
startdate_txt.place(x=80, y=121)
starttime_lbl.place(x=0, y=190)
starttime_txt.place(x=90, y=191)
details_lbl.place(x=0, y=260)
details_txt.place(x=70, y=261)
last_frame.place(x=480, y=400)
add_btn.place(x=0, y=30)
reset_btn.place(x=180, y=30)

root.mainloop()
