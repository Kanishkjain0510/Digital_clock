import datetime
import pytz
import tkinter as tk
from tkinter import ttk

class Clock:
    def __init__(self, name, timezone):
        self.name = name
        self.timezone = timezone
        self.label = ttk.Label(font=('Helvetica', 12))
    
    def update_time(self):
        now = datetime.datetime.now(pytz.timezone(self.timezone))
        time_str = now.strftime("%H:%M:%S")
        self.label.config(text=f"{self.name}\n{time_str}")
        self.label.after(1000, self.update_time)

def display_world_clock():
    window = tk.Tk()
    window.title("World Clock")
    window.geometry("800x600")
    
    clock_style = ttk.Style()
    clock_style.configure('TLabel', font=('Helvetica', 12))
    
    clocks = [
        ("Honolulu", "Pacific/Honolulu"),
        ("Anchorage", "America/Anchorage"),
        ("Los Angeles", "America/Los_Angeles"),
        ("Denver", "America/Denver"),
        ("Chicago", "America/Chicago"),
        ("New York", "America/New_York"),
        ("Sao Paulo", "America/Sao_Paulo"),
        ("London", "Europe/London"),
        ("Berlin", "Europe/Berlin"),
        ("Cairo", "Africa/Cairo"),
        ("Moscow", "Europe/Moscow"),
        ("Dubai", "Asia/Dubai"),
        ("New Delhi", "Asia/Kolkata"),
        ("Hong Kong", "Asia/Hong_Kong"),
        ("Tokyo", "Asia/Tokyo"),
        ("Sydney", "Australia/Sydney"),
        ("Auckland", "Pacific/Auckland"),
        ("Adelaide", "Australia/Adelaide"),
        ("Wellington", "Pacific/Auckland"),
        ("Jeddah", "Asia/Riyadh"),
        ("Toronto", "America/Toronto"),
        ("Mexico City", "America/Mexico_City"),
        ("Paris", "Europe/Paris"),
        ("Barcelona", "Europe/Madrid"),
        ("Oslo", "Europe/Oslo"),
        ("Singapore", "Asia/Singapore"),
        ("Mumbai", "Asia/Kolkata")
    ]
    
    for i, (city, timezone) in enumerate(clocks):
        clock = Clock(city, timezone)
        clock.label.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X)
        clock.update_time()
    
    window.mainloop()

if __name__ == "__main__":
    display_world_clock()
