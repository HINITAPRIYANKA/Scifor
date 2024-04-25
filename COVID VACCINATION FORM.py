import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    address = address_text.get("1.0", tk.END)
    email = email_entry.get()
    contact_no = contact_entry.get()
    country = country_entry.get()
    state = state_entry.get()
    diseases = [disease.get() for disease in disease_vars]

    # You can do further processing with the collected data
    # For now, displaying the information in a messagebox
    info_message = f"Name: {name}\nAge: {age}\nGender: {gender}\nAddress: {address}\nEmail: {email}\nContact No: {contact_no}\nCountry: {country}\nState: {state}\nDiseases: {', '.join(diseases)}"
    messagebox.showinfo("Registration Details", info_message)

# Create the main window
root = tk.Tk()
root.title("COVID Vaccine Registration")

# Labels and Entries
tk.Label(root, text="Name of the visitor").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter your Age").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Gender").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=1, padx=10, pady=5, sticky=tk.E)

tk.Label(root, text="Address").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
address_text = tk.Text(root, height=4, width=30)
address_text.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Email Id").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Contact No").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
contact_entry = tk.Entry(root)
contact_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Country").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
country_entry = tk.Entry(root)
country_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="State").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
state_entry = tk.Entry(root)
state_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Select diseases if you are having any following disease").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
diseases = ["Cold", "Cough", "Fever", "Headache"]
disease_vars = [tk.IntVar() for _ in range(len(diseases))]
for i, disease in enumerate(diseases):
    tk.Checkbutton(root, text=disease, variable=disease_vars[i]).grid(row=8+i, column=1, sticky=tk.W, padx=10, pady=2)

# Submit button
submit_button = tk.Button(root, text="REGISTER HERE", command=submit_form)
submit_button.grid(row=9+len(diseases), column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
