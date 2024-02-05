import tkinter as tk
import form_data
from tkinter import ttk
from tinydb import TinyDB, Query

db = TinyDB('form_database.json')
User = Query()


def error_terms_window():
    error_terms = tk.Tk()
    error_terms.geometry('300x50')
    error_terms.config(background='#faf0e6')
    error_terms.resizable(False, False)
    error_terms.title('Error')
    error_terms_label = tk.Label(error_terms, text='Please read and accept Terms & Conditions', background='#faf0e6')
    error_terms_label.pack()
    error_terms_close_button = tk.Button(error_terms, text='Close', command=error_terms.destroy)
    error_terms_close_button.pack()


def open_terms():
    terms_window = tk.Tk()
    terms_window.geometry('600x620')
    terms_window.resizable(False, False)
    terms_window.config(background='#faf0e6')
    terms_window.title('Terms & Conditions')
    terms_window_text = tk.Label(terms_window, background='#faf0e6')
    terms_window_text['text'] = form_data.terms_text_data
    terms_window_text.pack()
    terms_window_close_button = tk.Button(terms_window, text='Close', command=terms_window.destroy)
    terms_window_close_button.pack()


def fill_error_window():
    fill_error = tk.Tk()
    fill_error.geometry('300x50')
    fill_error.config(background='#faf0e6')
    fill_error.resizable(False, False)
    fill_error.title('Error')
    fill_error_label = tk.Label(fill_error, text='Please fill the required fields', background='#faf0e6')
    fill_error_label.pack()
    fill_error_close_button = tk.Button(fill_error, text='Close', command=fill_error.destroy)
    fill_error_close_button.pack()


def user_error_window():
    user_error = tk.Tk()
    user_error.geometry('300x50')
    user_error.config(background='#faf0e6')
    user_error.resizable(False, False)
    user_error.title('Error')
    user_error_label = tk.Label(user_error, text='Email and/or phone number registered', background='#faf0e6')
    user_error_label.pack()
    user_error_close_button = tk.Button(user_error, text='Close', command=user_error.destroy)
    user_error_close_button.pack()


def user_registered_window():
    user_registered = tk.Tk()
    user_registered.geometry('300x50')
    user_registered.config(background='#faf0e6')
    user_registered.resizable(False, False)
    user_registered.title('You have successfully registered')
    user_registered_label = tk.Label(user_registered, text='You have successfully registered', background='#faf0e6')
    user_registered_label.pack()
    user_registered_label = tk.Button(user_registered, text='OK', command=user_registered.destroy)
    user_registered_label.pack()


def validation():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    occupation = occupation_combo.get()
    prefix = prefix_combo.get()
    phone_number = phone_number_entry.get()
    email = email_address_entry.get()
    age = age_spinbox.get()
    check_mail = db.search(User.Email == email)
    check_phone = db.search(User.Number == (prefix + phone_number))
    if consent.get() == 0:
        print('Please read and accept Terms & Conditions')
        error_terms_window()
    elif consent.get() == 1:
        if first_name and last_name and occupation and prefix and phone_number and email and age:
            if check_mail or check_phone:
                print('Email and/or phone number registered')
                user_error_window()
            else:
                db.insert({
                    'First name': first_name,
                    'Last Name': last_name,
                    'Occupation': occupation,
                    'Number': prefix + phone_number,
                    'Email': email,
                    'Age': age
                })
                print('You have successfully registered')
                user_registered_window()
        else:
            print('Please fill the required fields')
            fill_error_window()


root = tk.Tk()
root.title('Form')
root.geometry('650x350')
root.resizable(False, False)
root.config(background='#faf0e6')

frame = tk.Frame(root, background='#faf0e6')
frame.pack()

user_data_frame = tk.LabelFrame(frame, text='User Information', background='#faf0e6')
user_data_frame.grid(row=0, column=0, pady=(10, 0))

first_name_label = tk.Label(user_data_frame, text='First name', background='#faf0e6')
first_name_label.grid(row=0, column=0, padx=15, pady=15)

last_name_label = tk.Label(user_data_frame, text='Last name', background='#faf0e6')
last_name_label.grid(row=0, column=1)

occupation_label = tk.Label(user_data_frame, text='Occupation', background='#faf0e6')
occupation_label.grid(row=0, column=2)

first_name_entry = tk.Entry(user_data_frame, width=30)
first_name_entry.grid(row=1, column=0, padx=(10, 0), pady=(0, 10))
last_name_entry = tk.Entry(user_data_frame, width=30)
last_name_entry.grid(row=1, column=1, padx=10, pady=(0, 10))
occupation_combo = ttk.Combobox(user_data_frame, width=30, state='readonly')
occupation_combo['values'] = form_data.occupation_data
occupation_combo.grid(row=1, column=2, padx=(0, 10), pady=(0, 10))

phone_number_label = tk.Label(user_data_frame, text='Phone number', background='#faf0e6')
phone_number_label.grid(row=2, column=0, padx=15, pady=15)

email_address_label = tk.Label(user_data_frame, text='E-mail address', background='#faf0e6')
email_address_label.grid(row=2, column=1)

something_label = tk.Label(user_data_frame, text='Age', background='#faf0e6')
something_label.grid(row=2, column=2)

prefix_combo = ttk.Combobox(user_data_frame, width=8, state='readonly')
prefix_combo['values'] = form_data.phone_prefix_data

prefix_combo.grid(row=3, column=0, padx=(10, 0), pady=(0, 10), sticky='w')
phone_number_entry = tk.Entry(user_data_frame, width=18)
phone_number_entry.grid(row=3, column=0, pady=(0, 10), sticky='e')
email_address_entry = tk.Entry(user_data_frame, width=30)
email_address_entry.grid(row=3, column=1, padx=10, pady=(0, 10))
age_spinbox = tk.Spinbox(user_data_frame, width=30, from_=18, to=999)
age_spinbox.grid(row=3, column=2, padx=10, pady=(0, 10))

terms_label = tk.LabelFrame(frame, text='Terms & Conditions', background='#faf0e6')
terms_label.grid(row=1, column=0, pady=(10, 0), sticky='news')
open_terms_label = tk.Label(terms_label, text='Read Terms & Conditions', background='#faf0e6')
open_terms_label.grid(row=0, column=0)
open_terms_button = tk.Button(terms_label, text='Read', command=open_terms)
open_terms_button.grid(row=0, column=1)
consent = tk.IntVar()
terms_checkbox = tk.Checkbutton(terms_label, variable=consent, onvalue=1, offvalue=0,
                                text='I agree to Terms & Conditions', background='#faf0e6')
terms_checkbox.grid(row=1, column=0, padx=(35, 0))

register_button = tk.Button(frame, width=20, text='Register', command=validation)
register_button.grid(row=2, column=0, pady=10)

root.mainloop()
