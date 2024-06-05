import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Building Project Estimate")

# Bold Title
title_label = tk.Label(root, text="Building Project Estimate", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))

# List of Variables
material_cost = tk.DoubleVar()
miles_travelled = tk.DoubleVar()
rate_per_mile = tk.DoubleVar()
project_duration = tk.IntVar()
num_workers = tk.IntVar()
rate_per_worker = tk.DoubleVar()
discount = tk.StringVar()
discount.set("0%")

# Validation function to allow only numbers
def validate_float(P):
    if P == "" or P.replace(".", "", 1).isdigit():
        return True
    return False

def validate_int(P):
    if P == "" or P.isdigit():
        return True
    return False

vcmd_float = (root.register(validate_float), '%P')
vcmd_int = (root.register(validate_int), '%P')

# All Entry Boxes and Fields
tk.Label(root, text="Material Cost:").grid(row=1, column=0, pady=5, padx=5, sticky=tk.E)
tk.Entry(root, textvariable=material_cost, validate="key", validatecommand=vcmd_float).grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Miles Travelled:").grid(row=2, column=0, pady=5, padx=5, sticky=tk.E)
tk.Entry(root, textvariable=miles_travelled, validate="key", validatecommand=vcmd_float).grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Rate per Mile:").grid(row=3, column=0, pady=5, padx=5, sticky=tk.E)
tk.Entry(root, textvariable=rate_per_mile, validate="key", validatecommand=vcmd_float).grid(row=3, column=1, pady=5, padx=5)

tk.Label(root, text="Project Duration (days):").grid(row=4, column=0, pady=5, padx=5, sticky=tk.E)
tk.Entry(root, textvariable=project_duration, validate="key", validatecommand=vcmd_int).grid(row=4, column=1, pady=5, padx=5)

tk.Label(root, text="Number of Workers:").grid(row=5, column=0, pady=5, padx=5, sticky=tk.E)
tk.Entry(root, textvariable=num_workers, validate="key", validatecommand=vcmd_int).grid(row=5, column=1, pady=5, padx=5)

tk.Label(root, text="Rate per Worker per Day:").grid(row=6, column=0, pady=5, padx=5, sticky=tk.E)
tk.Entry(root, textvariable=rate_per_worker, validate="key", validatecommand=vcmd_float).grid(row=6, column=1, pady=5, padx=5)

tk.Label(root, text="Discount:").grid(row=7, column=0, pady=5, padx=5, sticky=tk.E)
tk.OptionMenu(root, discount, "0%", "5%", "10%", "20%").grid(row=7, column=1, pady=5, padx=5)

output = tk.Text(root, height=10, width=50)
output.grid(row=10, column=0, columnspan=2, pady=10, padx=10)

# Estimate Calculator
def calculate_estimate():
    material_cost_val = material_cost.get()
    miles_travelled_val = miles_travelled.get()
    rate_per_mile_val = rate_per_mile.get()
    project_duration_val = project_duration.get()
    num_workers_val = num_workers.get()
    rate_per_worker_val = rate_per_worker.get()
    discount_val = int(discount.get().strip('%'))

    travel_cost = miles_travelled_val * rate_per_mile_val * project_duration_val
    labor_cost = project_duration_val * num_workers_val * rate_per_worker_val
    total_cost = material_cost_val + travel_cost + labor_cost
    discount_amount = (discount_val / 100) * total_cost
    final_cost = total_cost - discount_amount

    breakdown = (
        f"Material Cost: ${material_cost_val:.2f}\n"
        f"Travel Cost: ${travel_cost:.2f}\n"
        f"Labor Cost: ${labor_cost:.2f}\n"
        f"Total Cost before Discount: ${total_cost:.2f}\n"
        f"Discount: {discount_val}% (${discount_amount:.2f})\n"
        f"Final Cost: ${final_cost:.2f}\n"
    )

    output.delete("1.0", tk.END)
    output.insert(tk.END, breakdown)

# Larger and user-friendly buttons
tk.Button(root, text="Calculate Estimate", command=calculate_estimate, font=("Helvetica", 12), width=20).grid(row=8, column=0, columnspan=2, pady=10)

def save_estimate():
    estimate = output.get("1.0", tk.END)
    if estimate.strip():
        with open("estimate.txt", "w") as file:
            file.write(estimate)
        messagebox.showinfo("Save Estimate", "Estimate saved to estimate.txt")
    else:
        messagebox.showwarning("Save Estimate", "No estimate to save.")

tk.Button(root, text="Save Estimate", command=save_estimate, font=("Helvetica", 12), width=20).grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()

