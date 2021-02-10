from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters=[random.choice(letters) for letter in range(random.randint(8, 10))]
    password_symbols=[random.choice(symbols) for symbol in range(random.randint(2, 4))]
    password_numbers=[random.choice(numbers) for number in range(random.randint(2, 4))]

    password_list = password_numbers+password_symbols+password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_get=website_entry.get()
    try:
        with open("data.json","r") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="No Data File Found.")
    else:
        if website_get in data:
            email = data[website_get]["email"]
            password=data[website_get]["password"]
            messagebox.showinfo(title=website_get, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Result", message=f"No details for {website_get} exists.")


        # try:
        #     website=data[website_get]
        # except:
        #     messagebox.showinfo(title="Result", message=f"No details for {website_get} exists.")
        # else:
        #     email=website["email"]
        #     password=website["password"]
        #     messagebox.showinfo(title=website_get, message=f"Email:{email}\nPassword:{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get()
    email=email_username_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="OOPs!!",message="Please don't leave any fields empty!")
    else:
        isOk=messagebox.askokcancel(title=website,message=f"These are the details entered:\n"
                                                     f"Website:{website}\nEmail/Username:{email}\nPassword:{password}"
                                                     f"\nIs it ok to save data?")
        data=website+"  |  "+email+"  |  "+password+"\n"
        if isOk:
            try:
                with open("data.json","r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file2:
                    json.dump(data,file2,indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=55,pady=55)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
email_username_label=Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry=Entry(width=33)
website_entry.focus()
website_entry.grid(column=1,row=1)
email_username_entry=Entry(width=52)
email_username_entry.insert(0,"roysohag95@gmail.com")
email_username_entry.grid(column=1,row=2,columnspan=2)
password_entry=Entry(width=33)
password_entry.grid(column=1,row=3)

generate_button=Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=44,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)
search_button=Button(text="Search",width=15,command=find_password)
search_button.grid(column=2,row=1)

window.mainloop()