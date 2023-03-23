from tkinter import *
from tkinter import messagebox
from random import choice,randint, shuffle
import json
import pyperclip

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = pseudo_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {
          website: {
            "email":email,
            "password":password,
        }
    }
    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Ooops", message="Please don t leave any fields empty ! ")
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data , data_file , indent=4)
        except:
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(new_data , data_file , indent=4)
        website_entry.delete(0,END)
        password_entry.delete(0,END)
# ---------------------------- SEARCH BUTTON ------------------------------- #
def search():
    try:
        website_name = website_entry.get()
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            email = data[website_name]["email"]
            password = data[website_name]["password"]
        messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title=website_name, message="there are no names stored yet ! Please enter some websites ")
    except KeyError:
        messagebox.showinfo(title=website_name, message="website not found Sorry :( ")











# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8,10))]
    password_list += [choice(symbols) for _ in range (randint(2,4))]
    password_list += [choice(numbers) for _ in range(randint(2,4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")
#image
logo_img = PhotoImage(file="logo.png")
#canvas
canvas = Canvas(width=200, height=200, )
canvas.create_image(100, 100,image=logo_img)
canvas.grid(row=0,column=1)
#Labels
website= Label(text="Website:")
website.grid(row=1,column=0)
pseudo = Label(text="Email/Username:     ")
pseudo.grid(row=2,column=0)
password=Label(text="Password:")
password.grid(row=3,column=0)
#Entries
website_entry=Entry(width=33)
website_entry.grid(row=1,column=1)
website_entry.focus()
pseudo_entry = Entry(width=51)
pseudo_entry.insert(END, "aminelakbachi@gmail.com")
pseudo_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)
#buttons
generate_button = Button(text="GeneratePassword", width=14, command = generate_password)
generate_button.grid(row=3,column=2)
add_button = Button( text="Add" ,width=43, command=save)
add_button.grid( row=4,column=1,columnspan=2)
Search_button = Button(text="Search", width=14, command = search)
Search_button.grid(row=1,column=2)
window.mainloop()