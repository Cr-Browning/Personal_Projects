from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
"""
This program opens a GUI that allows the user to do unit conversions between metric and customary units.
    If the conversion is not valid the user will be prompted with an error. They'll have to restart the GUI to convert
    compatable units. The text box is autamatically selected with the cursur and upon pressing enter the user will be 
    given the correct conversion. 
"""

root = tk.Tk()
root.title("Unit Converter")
root.geometry('400x400')
root.configure(bg='black')

options_1 = [
    "km", "mi", "kg", "lbs", "°F", "°C","mph","kph", "cm", "in"
]

options_2 = [
    "km", "mi", "kg", "lbs", "°F", "°C","mph","kph", "cm", "in"
]

clicked1 = StringVar()
clicked1.set(options_1[1])

clicked2 = StringVar()
clicked2.set(options_2[0])

drop_one = OptionMenu(root, clicked1, *options_1)
drop_two = OptionMenu(root, clicked2, *options_2)

drop_one.place(x=150,y=50)
drop_two.place(x=245,y=50)

num_unit = Entry(root, width=8, bg='black', fg="white")
num_unit.focus()
num_unit.place(x=55, y=47)
txt = tk.Label(root, text="to",bg='black', fg='white',font=("Ariel",20))
txt.place(x=205,y=46)


def convert(event = None):
    """
    :param event: set to none so the <Return> key can press the button
    :return: the unit conversion
    """
    if clicked1.get() == 'km' and clicked2.get() == 'mi':
        ans = float(num_unit.get()) * .621
        return tk.Label(root, text=str(ans)+' mi',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'mi' and clicked2.get() == 'km':
        ans = float(num_unit.get()) * 1.609
        return tk.Label(root, text=str(ans)+' km',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'kg' and clicked2.get() == 'lbs':
        ans = float(num_unit.get()) * 2.20462
        return tk.Label(root, text=str(ans)+' lbs',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'lbs' and clicked2.get() == 'kg':
        ans = float(num_unit.get()) * .45359
        return tk.Label(root, text=str(ans)+' kg',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == '°C' and clicked2.get() == '°F':
        ans = float(num_unit.get()) * 1.8 + 32
        return tk.Label(root, text=str(ans)+' °F',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == '°F' and clicked2.get() == '°C':
        ans = (float(num_unit.get()) - 32) * .625
        return tk.Label(root, text=str(ans)+' °C',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'mph' and clicked2.get() == 'kph':
        ans = (float(num_unit.get()) * 1.609344)
        return tk.Label(root, text=str(ans)+' kph',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'kph' and clicked2.get() == 'mph':
        ans = (float(num_unit.get()) * .62137119)
        return tk.Label(root, text=str(ans)+' mph',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'cm' and clicked2.get() == 'in':
        ans = (float(num_unit.get()) * 0.39370079)
        return tk.Label(root, text=str(ans)+' in',bg='black',fg='white',font=("Arial",18)).place(x=175,y=180)
    elif clicked1.get() == 'in' and clicked2.get() == 'cm':
        ans = (float(num_unit.get()) * 2.54)
        return tk.Label(root, text=str(ans) + ' cm', bg='black', fg='white', font=("Arial", 18)).place(x=175, y=180)

    else:
        return tk.Label(root,text="Error, Please select compatible conversions",bg='black',fg='white',
                        font=("Arial",14)).place(x=80,y=180)


btn = Button(root, text="run", command=convert)
btn.place(x=190, y=106)
root.bind("<Return>", lambda e: convert())
root.mainloop()
