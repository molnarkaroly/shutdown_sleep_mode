import customtkinter as ctk
import time
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

font_path = resource_path("digital-7.ttf")



ctk.set_appearance_mode("dark")
theme_mode = "dark"

root = ctk.CTk()
root.title("Időzítő")
root.geometry("170x230")
root.resizable(False, False)

hours_entry = ctk.CTkEntry(root)
hours_entry.insert(0, "0")
minutes_entry = ctk.CTkEntry(root)
minutes_entry.insert(0, "0")
seconds_entry = ctk.CTkEntry(root)
seconds_entry.insert(0, "0")
ora = ctk.CTkLabel(root, text="Óra")
perc = ctk.CTkLabel(root, text="Perc")
másodperc = ctk.CTkLabel(root, text="Másodperc")
nocopy = ctk.CTkLabel(root, text="© molnarkaroly")


hours = 0
minutes = 0
seconds = 0

def start():
    hours = int(hours_entry.get())
    minutes = int(minutes_entry.get())
    seconds = int(seconds_entry.get())

    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds > 0:
        time_label.configure(text=f"{total_seconds // 3600:02d}:{(total_seconds % 3600) // 60:02d}:{total_seconds % 60:02d}")
        root.update()

        time.sleep(1)

        total_seconds -= 1

        if total_seconds <= 0:
            time_label.configure(text="00:00:00")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


            root.destroy()

start_button = ctk.CTkButton(root, text="Start", command=start)

time_label = ctk.CTkLabel(root, text="00:00:00", font=("Digital-7", 30))

def moon():
    global theme_mode
    if theme_mode == "dark":
        ctk.set_appearance_mode("light")
        theme_mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        theme_mode = "dark"

moon_icon = ctk.CTkButton(root, text="🌙", font=("Arial", 12), command=moon, width=12, height=12)
moon_icon.place(relx=1.0, rely=0.0, anchor=ctk.NE)

ora.pack()
hours_entry.pack()
perc.pack()
minutes_entry.pack()
másodperc.pack()

seconds_entry.pack()
start_button.pack()
time_label.pack()
nocopy.pack()

root.mainloop()
