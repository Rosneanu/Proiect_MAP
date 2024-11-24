#program for password check, if it's strong enough
#criteria: at least 8 characters long, one uppercase letter, one lowercase letter, one digit, one special character

import re

import tkinter as tk
from tkinter import *
from tkinter import messagebox

# routine for checking if it is strong enough
def is_strong_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return "Parola e prea scurta, trebuie sa contina macar 8 caractere!"
    # Check if password has any space
    if re.search(r'[ ]', password):
        return "Parola nu trebuie sa contina spatiu."
    # Check if password has at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Parola trebuie sa contina macar o litera mare."
    
    # Check if password has at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Parola trebuie sa contina macar o litera mica."
    
    # Check if password has at least one digit
    if not re.search(r'[0-9]', password):
        return "Parola trebuie sa contina macar o cifra."
    
    # Check if password has at least one special character
    if not re.search(r'[!@#$%^&+=]', password):
        return "Parola trebuie sa contina macar un caracter special (exemplu: !, @, #, $, %, ^, &, +, =)."
    
    return "Parola este puternica!."
# routine called when the user press the check button ("Verifica")
def check_password():
    password = password_entry.get()  #get the password from the text field
    result = is_strong_password(password)  #check the password
    messagebox.showinfo("Rezultatul verificarii este:  ", result)  #show result in a message box


afisaj = tk.Tk()
afisaj.title("Password checker")
afisaj.geometry("400x200")

# Lable  for instruction
label = tk.Label(afisaj, text="Introdu o parolă pentru a o verifica:")
label.pack(pady=10)

# Box for input
password_entry = tk.Entry(afisaj, show="*", width=30)
password_entry.pack(pady=5)

# Button for checking
check_button = tk.Button(afisaj, text="Verifică Parola", command=check_password)
check_button.pack(pady=10)


mainloop()