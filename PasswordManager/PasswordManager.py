from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# Password generator

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list= [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)


# GUI
window = Tk()
window.title("Password Manager")
window.minsize(width=400,height=400)
window.config(pady=20,padx=20)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=2,row=2)

website_label=Label(text="Website:",font=("Cursor",12,"bold"))
website_label.grid(column=1,row=4)

website_entry=Entry(width=35)
website_entry.grid(column=2,row=4,columnspan=2)
website_entry.focus()

email_label=Label(text="Email/Username:",font=("Cursor",12,"bold"))
email_label.grid(column=1,row=6)

email_entry=Entry(width=35)
email_entry.grid(column=2,row=6,columnspan=2)

pass_label=Label(text="Password:",font=("Cursor",12,"bold"))
pass_label.grid(column=1,row=8)

pass_entry=Entry(width=21)
pass_entry.grid(column=2,row=8)

Gen_pass=Button(text="Generate Password",command=generate_pass)
Gen_pass.grid(column=4,row=8)

def find_password():
    try:
        with open("data.json",mode="r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Data file not found",message="No data storage file found")
    else:
        try:
            website=website_entry.get()
            messagebox.showinfo(title="Website details", message=f"{data[website]['email']} password: {data[website]['password']}")
        except KeyError:
            messagebox.showinfo(title="Website details", message=f"No website {website_entry.get()} found")


Search=Button(text="Search",command=find_password)
Search.grid(column=3,row=4,columnspan=2)

def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    pass_data=pass_entry.get()
    new_data={
        website_data: {
            "email":email_data,
            "password":pass_data
        }
    }

    if website_data=="" or email_data=="" or pass_data=="":
        is_empty=messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website_data,message=f"These are the details entered: \nEmail: {email_data}"
                           f"\nPassword: {pass_data} \n Is it ok to save?")
        if is_ok:
            try:
                with open("data.json",mode="r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("data.json",mode="w") as file:
                    json.dump(new_data,file,indent=4)
            else:
                new_data.update(data)
                with open("data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                pass_entry.delete(0,END)
                messagebox.showinfo(title="Save password",message="Password saved")

Add=Button(text="Add",width=40,command=save)
Add.grid(column=2,row=10,columnspan=6)

window.mainloop()