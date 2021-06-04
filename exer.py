from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x200")
root.title("Log in")

# Create Labels and entries

user_label=Label(root, text= "please enter Username: ")
user_label.place(x=50, y=50)
user_entry=Entry(root)
user_entry.place(x=250, y=50, width=100)

pass_label=Label(root, text="please enter Password: ")
pass_label.place(x=50,y=90)
pass_entry=Entry(root)
pass_entry.place(x=250, y=90, width=100)

# create function

def login():
    usernames = ["Aisaacs", "Jsmith", "Bblack", "Karnold", "Lmorgan"]
    password = ["12548", 85296, 14725, 96385, 78945]
    found=False
    for x in range(len(usernames)):
        if user_entry.get()==usernames[x] and pass_entry.get()==password[x]:
            found=True
    if found==True:
        messagebox.showinfo("STATUS", "Access Granted")
        root.destroy()
        import next
    else:
        messagebox.showinfo("STATUS","Access not granted")

# create button

submit_button=Button(root,text="Submit", command=login)
submit_button.place(x=250, y=150)

root.mainloop()
