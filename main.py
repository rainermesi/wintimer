import tkinter as tk
import tkinter.ttk as ttk

window = ttk.Tk()

title_label = ttk.Label(
    text='This is a simple timer',
    )

time_label = ttk.Label(
    text='00:00:00'
)

button_label = ttk.Button(
    text='Start timer',
)

progress = ttk.Progressbar(orient='horizontal', length=500, mode='determinate',value=15)

title_label.pack()
time_label.pack()
progress.pack()
button_label.pack()

window.mainloop()


#reference
#https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter