from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("600x200")
root.config(bg="Skyblue")
root.title("Malaysia Trip")

amount_label=Label(root, text="Enter funds available for the trip: ", bg="skyblue")
amount_label.place(x=20, y=50)
amount = Entry(root,)
amount.place(x=350, y=50)

def qual():
    funds =  amount.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror("not enough funds", "Please deposit more funds.")
        else:
            messagebox.showinfo("Congratulations", "You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("Error","Please insert a valid number.")

qualification=Button(root, text="check qualification", command=qual)
qualification.place(x=200,y=100)


root.mainloop()