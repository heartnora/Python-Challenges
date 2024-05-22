import tkinter as tk
from tkinter import ttk

def proceed():
    name = name_entry.get()
    surname = surname_entry.get()
    occupation = occupation_combo.get()

    if name and surname and occupation:
        with open("data.txt", "a") as file:
            file.write(f"{name} {surname} - {occupation}\n")
        name_entry.delete(0, tk.END)
        surname_entry.delete(0, tk.END)
        occupation_combo.set('')
        status_label.config(text="Data stored Successfully.", fg="green", font="bold")
    else:
        status_label.config(text="Please fill in all fields.", fg="red", font="bold")

root = tk.Tk()
root.title("Data Entry Application")

# Enlarge the window
root.geometry("400x200")

# Centering the window
root.eval('tk::PlaceWindow . center')

# Name Entry
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Surname Entry
tk.Label(root, text="Surname:").grid(row=1, column=0, padx=5, pady=5)
surname_entry = tk.Entry(root)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

# Gender Dropdown
tk.Label(root, text="Gender:").grid(row=2, column=0, padx=5, pady=5)
occupations = ["Prefer Not to Say", "Male", "Female"]
occupation_combo = ttk.Combobox(root, values=occupations, state="readonly")
occupation_combo.grid(row=2, column=1, padx=5, pady=5)

# Proceed Button
proceed_button = tk.Button(root, text="Enter", command=proceed)
proceed_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Status Label
status_label = tk.Label(root, text="", fg="red")
status_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
