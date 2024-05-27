import tkinter as tk
from tkinter import messagebox

expenses = []
file_name = "expenses.txt"

def read_file():
    try:
        with open(file_name, "r") as file:
            for line in file:
                expenses.append(line.strip())
    except FileNotFoundError:
        pass

def write_file():
    with open(file_name, "w") as file:
        for expense in expenses:
            file.write(expense + "\n")

def add_expense():
    date = date_entry.get()
    item = item_entry.get()
    cost = cost_entry.get()
    expenses.append(f"{date},{item},{cost}")
    write_file()
    date_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    cost_entry.delete(0, tk.END)
    messagebox.showinfo("Info", "Kulutus lisatud.")
    

def display_expenses()
    display_text = "Kuupäev\tKirje\tKirje\tKulu\n"
    for expense in expenses:
        display_text += expense.replace(",", "\t") + "\n"
    messagebox.showinfo("Kulude kokkuvõte", display_text)
    
read_file()







