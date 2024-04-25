import tkinter as tk
import random

class RandomNamePicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Name Picker")
        self.root.geometry("400x300")

        self.students = ["Student1", "Student2", "Student3", "Student4", "Student5"]
        self.selected_name = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        # Frame for random name display
        random_name_frame = tk.Frame(self.root)
        random_name_frame.pack(pady=20)

        random_name_label = tk.Label(random_name_frame, text="Random Name Selector:")
        random_name_label.pack()

        selected_name_display = tk.Label(random_name_frame, textvariable=self.selected_name, font=("Helvetica", 16, "bold"))
        selected_name_display.pack()

        # Frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()


        pick_name_button = tk.Button(button_frame, text="Selected name", command=self.pick_random_name)
        pick_name_button.pack(side=tk.LEFT, padx=10)


        reset_button = tk.Button(button_frame, text="Already Selected", command=self.reset_list)
        reset_button.pack(side=tk.RIGHT, padx=10)

        pick_name_button = tk.Button(button_frame, text="Shuffle", command=self.pick_random_name)
        pick_name_button.pack(side=tk.LEFT, padx=10)

    def pick_random_name(self):
        if self.students:
            random_name = random.choice(self.students)
            self.selected_name.set(random_name)
            self.students.remove(random_name)
        else:
            self.selected_name.set("List is empty!")

    def reset_list(self):
        self.students = ["Student1", "Student2", "Student3", "Student4", "Student5"]
        self.selected_name.set("")

if __name__ == "__main__":
    root = tk.Tk()
    random_name_picker = RandomNamePicker(root)
    root.mainloop()

