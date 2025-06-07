from tkinter import *
import subprocess
from database import validate_login,get_id
def open_signup():
    root.destroy()
    subprocess.run(['python', 'frame2.py'])

def open_tasks(user_id):
    root.destroy()
    subprocess.run(['python', 'frame4.py', str(user_id)])

def login():
    username = user.get()
    password = user2.get()
    if not username or not password:
        Label(frame, text="Please enter both username and password", fg='red', bg='white', font=("Microsoft YaHei UI Light", 8)).place(x=120, y=200)
        return
    elif validate_login(username, password):
        Label(frame, text="Login Successful", fg='green', bg='white', font=("Microsoft YaHei UI Light", 10)).place(x=120, y=200)
        user_id = get_id(username)
        open_tasks(user_id)
    else:
        Label(frame, text="Invalid Credentials", fg='red', bg='white', font=("Microsoft YaHei UI Light", 10)).place(x=120, y=200)

root = Tk()
root.title("Login Page")
root.geometry("925x500")
root.resizable(False, False)
root.configure(bg="white")

# Frame 1
img = PhotoImage(file='Webp.net-resizeimage (2).png')
lb1 = Label(root, image=img, bg='white')
lb1.place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading = Label(frame, text="Sign In", bg="white", fg='#57a1f8', font=("Microsoft YaHei", 25, "bold"))
heading.place(x=100, y=5)

lb1 = Label(frame, text="Username : ", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
user = Entry(frame, width=25, fg='black', bg='white', font=("Microsoft YaHei UI Light", 12), border=0)
lb1.place(x=0, y=100)
user.place(x=75, y=102)
Frame(frame, width=310, height=2, bg='black').place(x=5, y=132)

lb2 = Label(frame, text="Password : ", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
user2 = Entry(frame, width=25, fg='black', bg='white', font=("Microsoft YaHei UI Light", 12), border=0, show='*')
lb2.place(x=0, y=160)
user2.place(x=72, y=162)
Frame(frame, width=310, height=2, bg='black').place(x=5, y=190)

bu1 = Button(frame, width=39, pady=8, text='Sign In', bg='#57a1f8', fg='white', border=0, cursor="hand2", command=login)
bu1.place(x=35, y=234)
lb3 = Label(frame, text="Don't Have An Account?", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
lb3.place(x=70, y=300)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white', fg='#57a1f8', font=10, cursor="hand2", command=open_signup)
sign_up.place(x=228, y=298)

root.mainloop()
