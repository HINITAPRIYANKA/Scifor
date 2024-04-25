import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("300x200")

        self.hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                      '08', '09', '10', '11', '12', '13', '14', '15',
                      '16', '17', '18', '19', '20', '21', '22', '23', '24')

        self.minutes = tuple(f"{i:02d}" for i in range(60))
        self.seconds = tuple(f"{i:02d}" for i in range(60))

        self.selected_hour = tk.StringVar(value='00')
        self.selected_minute = tk.StringVar(value='00')
        self.selected_second = tk.StringVar(value='00')

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Select Alarm Time").pack(pady=10)

        hour_label = ttk.Label(self.root, text="Hour:")
        hour_label.pack()
        hour_combobox = ttk.Combobox(self.root, values=self.hours, textvariable=self.selected_hour)
        hour_combobox.pack()

        minute_label = ttk.Label(self.root, text="Minute:")
        minute_label.pack()
        minute_combobox = ttk.Combobox(self.root, values=self.minutes, textvariable=self.selected_minute)
        minute_combobox.pack()

        second_label = ttk.Label(self.root, text="Second:")
        second_label.pack()
        second_combobox = ttk.Combobox(self.root, values=self.seconds, textvariable=self.selected_second)
        second_combobox.pack()

        set_alarm_button = ttk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        set_alarm_button.pack(pady=20)

    def set_alarm(self):
        selected_time = f"{self.selected_hour.get()}:{self.selected_minute.get()}:{self.selected_second.get()}"
        try:
            alarm_time = datetime.strptime(selected_time, '%H:%M:%S')
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format")
            return

        current_time = datetime.now()
        delta_time = alarm_time - current_time

        if delta_time.total_seconds() <= 0:
            tk.messagebox.showwarning("Warning", "Please select a future time")
            return

        tk.messagebox.showinfo("Alarm Set", f"Alarm set for {selected_time}")

        # Schedule the alarm callback after the calculated delay
        self.root.after(int(delta_time.total_seconds()) * 1000, self.alarm_callback)

    def alarm_callback(self):
        tk.messagebox.showinfo("Alarm", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()

