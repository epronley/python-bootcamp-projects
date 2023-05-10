# _______________________________PASSWORD MANAGER_____________________________#
# Allows users to generate and save passwords for their online accounts.
# Copies newly generated password to clipboard for easy use.
# Allows users to search for their passwords in a JSON file.
# If JSON file doesn't exist, program creates one after user saves first password.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# _______________________________GENERATE PASSWORD FUNCTION_____________________________#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    copy_message()
    pyperclip.copy(password)


# _______________________________ADD PASSWORD TO JSON FILE_____________________________#
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you haven't left any fields empty.")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# _______________________________DISPLAY COPY MESSAGE_____________________________#
def copy_message():
    copied = Label(text="Password Copied\n To Clipboard", font=("Arial", 12))
    copied.grid(column=0, row=0)
    window.after(2000, copied.destroy)


# _______________________________SEARCH PASSWORD FUNCTION_____________________________#
def search_password():
    search = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="No data found!\n\nCreate new file by adding password")
    else:
        if search in data:
            email = data[search]["email"]
            password = data[search]["password"]
            messagebox.showinfo(message=f"Site: {search}\n\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(message=f"No data for '{search}' exists")


# _______________________________CREATE UI_____________________________#
# Create Window
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# Create Canvas for Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Create and place Labels
website_label = Label(text="Website Name:")
website_label.grid(column=0, row=1)
email_label = Label(text="Username/Email:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create and place Entries
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "epronley@gmail.com")
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Create and place Buttons
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=6, command=search_password)
search_button.grid(column=2, row=1)

window.mainloop()
