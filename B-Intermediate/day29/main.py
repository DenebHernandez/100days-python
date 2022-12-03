import os
import tkinter as tk

main_folder = os.getcwd()
cwd = f"{main_folder}\B-Intermediate\day29"
# cwd = f"{main_folder}"

#Functions
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    website_entry.focus()

    with open(file=f"{cwd}\data.txt", mode="a") as fh:
        fh.write(f"{website} | {email} | {password}\n")


window = tk.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
logo_img = tk.PhotoImage(file=f"{cwd}\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website")
email_label = tk.Label(text="Email/Username")
password_label = tk.Label(text="Password")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = tk.Entry(width=40)
email_entry = tk.Entry(width=40)
password_entry = tk.Entry(width=22)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "deneb@test.com")
password_entry.grid(column=1, row=3, columnspan=1)

gen_password_button = tk.Button(text="Generate Password")
add_button = tk. Button(text="Add", width=34, command=save)
gen_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
