from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def saving_password():

    website = website_text.get()
    email = username_text.get()
    password = password_text.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                              f"Password: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as passwords:
                passwords.write(f"{website} | {email} | {password}\n")

            website_text.delete(0, END)
            password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Entries
website_text = Entry(width=38)
website_text.focus()
website_text.grid(row=1, column=1, columnspan=2)
username_text = Entry(width=38)
username_text.insert(0, "username@email.com")
username_text.grid(row=2, column=1, columnspan=2)
password_text = Entry(width=21)
password_text.grid(row=3, column=1)


# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=saving_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
