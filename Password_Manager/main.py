from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list+=[random.choice(symbols) for _ in range(nr_symbols)]
    password_list+=[random.choice(numbers) for _ in range(nr_numbers)]
    password = "".join(password_list)
    password_entry.insert(END,password)
    pyperclip.copy(password) 
# ---------------------------- SAVE_ PASSWORD ------------------------------- #

def save_():
    web=website_entry.get()
    mail=email_entry.get()
    pas= password_entry.get()
    new_data={
        web: {
            "email": mail,
            "password": pas
        }
    }

    if web=="" or pas=="":
        messagebox.askokcancel(title=web,message=f"Hey, dont leave anything empty")
    else:
        flag=messagebox.askokcancel(title=web,message=f"Your details: \nEmail: {mail}\nPassword: {pas}\nSure you wanna save_ it?")
        if flag:
            try:
                with open ("output.json","r") as data_file:
                    data=json.load(data_file)
            except FileNotFoundError:
                data_file=open("output.json","w")
                json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open ("output.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END) 



def find_pas():
    web=website_entry.get()

    try:
        data_file=open("output.json","r")
        data=json.load(data_file)

    except FileNotFoundError:
        messagebox.askokcancel(title="Error",message=f"NO Data File Found")

    else:
        if web in data:
            mail=data[web]["email"]
            pas=data[web]["password"]
            messagebox.askokcancel(title=web,message=f"Email: {mail}\nPassword: {pas}")
        else:
            messagebox.askokcancel(title="Error",message=f"No details for {web} exists")


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(END,"example@gmail.com")
email_entry.grid(row=2, column=1,columnspan=2, sticky="EW")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1,sticky="w ")

# Buttons
generate_password_button = Button(text="Generate Password",width=15,command=gen_pass)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35,command=save_)
add_button.grid(row=4, column=1,columnspan=2, sticky="EW")
search=Button(text="Search",width=15,command=find_pas)
search.grid(row=1,column=2)







window.mainloop()