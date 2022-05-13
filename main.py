import tkinter
import customtkinter
import time
from datetime import datetime

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("400x240")

start_time = datetime.now().strftime("%H:%M:%S")

def button_function():
    print('Button press')

# Label
label = customtkinter.CTkLabel(master=root_tk, text=f"{start_time}")
label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, text="Button", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()