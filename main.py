from tkinter import *


def mile_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    Km_result_label.config(text=f"{km}")


window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=2)

Km_result_label = Label(text="0")
Km_result_label.grid(column=2, row=2)

Km_label = Label(text="KM")
Km_label.grid(column=3, row=2)

Calculate_button = Button(text="Calculate",command=mile_to_km)
Calculate_button.grid(column=2, row=3)

window.mainloop()
