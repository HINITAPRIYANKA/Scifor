import tkinter as tk
from tkinter import ttk
from datetime import datetime

class BMIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("BMI Calculator")

        self.height_unit = tk.StringVar(value="cm")
        self.weight_unit = tk.StringVar(value="kg")

        self.height_label = ttk.Label(self.master, text="Height:")
        self.height_label.grid(row=0, column=0, padx=10, pady=10)

        self.height_scale = ttk.Scale(self.master, from_=100, to=250, length=200, orient="horizontal")
        self.height_scale.set(170)
        self.height_scale.grid(row=0, column=1, padx=10, pady=10)

        self.height_unit_menu = ttk.Combobox(self.master, values=["cm", "in"], textvariable=self.height_unit)
        self.height_unit_menu.grid(row=0, column=2, padx=10, pady=10)

        self.weight_label = ttk.Label(self.master, text="Weight:")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)

        self.weight_scale = ttk.Scale(self.master, from_=40, to=200, length=200, orient="horizontal")
        self.weight_scale.set(70)
        self.weight_scale.grid(row=1, column=1, padx=10, pady=10)

        self.weight_unit_menu = ttk.Combobox(self.master, values=["kg", "lb"], textvariable=self.weight_unit)
        self.weight_unit_menu.grid(row=1, column=2, padx=10, pady=10)

        self.calculate_button = ttk.Button(self.master, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.bmi_scale = ttk.Scale(self.master, from_=10, to=40, length=200, orient="horizontal", state="disabled")
        self.bmi_scale.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=4, column=0, columnspan=3, pady=10)

    def calculate_bmi(self):
        height = self.height_scale.get()
        weight = self.weight_scale.get()

        if self.height_unit.get() == "in":
            height *= 0.0254  # Convert inches to meters

        if self.weight_unit.get() == "lb":
            weight *= 0.453592  # Convert pounds to kilograms

        bmi = weight / (height ** 2)
        self.bmi_scale.set(bmi)

        bmi_category = self.get_bmi_category(bmi)
        self.display_result(bmi_category)

        self.save_to_file(height, weight, bmi)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        else:
            return "Overweight"

    def display_result(self, bmi_category):
        color = "green" if bmi_category == "Normal" else "red"
        self.result_label.config(text=f"Result: {bmi_category}", foreground=color)

    def save_to_file(self, height, weight, bmi):
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d %H:%M:%S")

        with open("bmi_records.txt", "a") as file:
            file.write(f"Date: {date_str}, Height: {height:.2f} {self.height_unit.get()}, "
                       f"Weight: {weight:.2f} {self.weight_unit.get()}, BMI: {bmi:.2f}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
