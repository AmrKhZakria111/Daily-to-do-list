from tkinter import *
import subprocess
from database import register_user

def open_signin():
    root.destroy()
    subprocess.run(['python', 'python.py'])

def register():
    username = user.get()
    password = user2.get()
    confirm_password = user3.get()
    if not username or not password or not confirm_password:
        Label(frame, text="Please enter both username and password", fg='red', bg='white', font=("Microsoft YaHei UI Light", 8)).place(x=120, y=200)
        return
    elif  password == confirm_password:
        success = register_user(username, password)
        if success:
            Label(frame, text="Registration Successful", fg='green', bg='white', font=("Microsoft YaHei UI Light", 10)).place(x=120, y=300)
        else:
            Label(frame, text="Username Already Exists", fg='red', bg='white', font=("Microsoft YaHei UI Light", 10)).place(x=120, y=300)
    else:
        Label(frame, text="Passwords Do Not Match", fg='red', bg='white', font=("Microsoft YaHei UI Light", 10)).place(x=120, y=300)

root = Tk()
root.title("Register Page")
root.geometry("925x500")
root.resizable(False, False)
root.configure(bg="white")

# Frame 2
img = PhotoImage(file='Webp.net-resizeimage (1).png')
lb1 = Label(root, image=img, bg='white')
lb1.place(x=50, y=50)
frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)
heading = Label(frame, text="Sign Up", bg="white", fg='#57a1f8', font=("Microsoft YaHei", 25, "bold"))
heading.place(x=100, y=-5)

lb1 = Label(frame, text="Username : ", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
user = Entry(frame, width=25, fg='black', bg='white', font=("Microsoft YaHei UI Light", 12), border=0)
lb1.place(x=0, y=70)
user.place(x=75, y=72)
Frame(frame, width=310, height=2, bg='black').place(x=5, y=102)

lb2 = Label(frame, text="Password : ", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
user2 = Entry(frame, width=25, fg='black', bg='white', font=("Microsoft YaHei UI Light", 12), border=0, show='*')
lb2.place(x=0, y=140)
user2.place(x=72, y=142)
Frame(frame, width=310, height=2, bg='black').place(x=5, y=172)

lb3 = Label(frame, text="Confirm Password : ", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
user3 = Entry(frame, width=25, fg='black', bg='white', font=("Microsoft YaHei UI Light", 12), border=0, show='*')
lb3.place(x=0, y=210)
user3.place(x=122, y=212)
Frame(frame, width=310, height=2, bg='black').place(x=5, y=242)

bu1 = Button(frame, width=39, pady=8, text='Sign Up', bg='#57a1f8', fg='white', border=0, cursor="hand2", command=register)
bu1.place(x=35, y=274)
lb3 = Label(frame, text="I Have An Account?", fg='black', bg='white', font=("Microsoft YaHei UI Light", 10))
lb3.place(x=70, y=320)

sign_in = Button(frame, width=6, text='Sign In', border=0, bg='white', fg='#57a1f8', font=10, cursor="hand2", command=open_signin)
sign_in.place(x=200, y=318)

root.mainloop()
