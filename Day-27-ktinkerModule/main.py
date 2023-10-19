# from tkinter import *
# window=Tk()
# window.title("Day 27")
# window.minsize(width=500, height=300)
# window.config(padx=100,pady=200)
#
# my_label=Label(text="Good Morning",font=("Arial",30))
# my_label.grid(row=0,column=0)
#
#
# #button
# def button_click():
#     my_label.config(text=input.get())
#
#
# button=Button(command=button_click,text="Click Me")
# button.grid(row=1,column=1)
#
# button2=Button(command=button_click,text="Click me")
# button2.grid(row=0,column=2)
# #ENtry
# input=Entry(width=10)
# input.grid(row=2,column=3)
# window.mainloop()

#MILE TO KM PROJECT
from tkinter import *
window=Tk()
window.minsize(width=500,height=300)
window.config(padx=50,pady=100)

#function to convert mile to km
def mile_to_km_function():
    # mile=float(mile_input.get())
    # km=mile*1.6
    # after_calculation_km.config(text=km)
    after_calculation_km.config(text=float(mile_input.get())*1.6)

mile_input=Entry(width=10)
mile_input.grid(row=0,column=1)

mile_label=Label(text="Miles")
mile_label.grid(row=0,column=2)

is_equal_to_label=Label(text="is equal to")
is_equal_to_label.grid(row=1,column=0)

after_calculation_km=Label(text="0")
after_calculation_km.grid(row=1,column=1)

km_label=Label(text="km")
km_label.grid(row=1,column=2)

button=Button(text="Calculate",command=mile_to_km_function)
button.grid(row=2,column=1)



window.mainloop()
