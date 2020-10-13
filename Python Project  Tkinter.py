from tkinter import *

# cel = IntVar()
# fahren = IntVar()


def convert_function():
    if feh_entry:
        fahren = float(feh_entry.get())
        celsius = (fahren - 32) * (5/9)
        result_lbl.configure(text=round(celsius, 2))

def convert_function1():
    if celcius_entry:
        cel = float(celcius_entry.get())
        fahrenheit = (cel - 9 / 5) + 32
        result_lbl.configure(text=round(fahrenheit, 2))







mywindow = Tk()
mywindow.title("Temperature Convertor")
mywindow.geometry("800x400")
mywindow.configure(background="navy")


def activate():
    celcius_entry.configure(state="normal")
    feh_entry.configure(state="disable")
    calculate_button1.configure(state="disable")
    calculate_button.configure(state="normal")

def activate_two():
    feh_entry.configure(state="normal")
    celcius_entry.configure(state="disable")
    calculate_button.configure(state="disable")
    calculate_button1.configure(state="normal")


def clear():
    celcius_entry.delete(0,END)
    feh_entry.delete(0,END)
    result_lbl.configure(text="")


group = LabelFrame(mywindow, text="Celcius To Fehrenheit", padx=50, pady=50,bg="orange")
group.grid(row=1, column= 1)


celcius_entry= Entry(group,state="disable")
celcius_entry.grid(row=1, column=2)


group = LabelFrame(mywindow, text="Fehrenheit To Celcius", padx=50, pady=50,bg="orange")
group.grid(row=1, column=7)

feh_entry = Entry(group,state="disable")
feh_entry.grid(row=1, column=8)


active_button = Button (mywindow, text = "ActivateCel", command=activate,bg="pink")
active_button.grid(row = 4, column = 1, pady = 5, padx = 5)

activate_button = Button (mywindow, text = "ActivateFeh",command=activate_two,bg="pink")
activate_button.grid(row = 4, column = 7, pady = 5, padx = 5)


calculate_button = Button (mywindow, text = "CalculateCel",bg="orange" ,command=convert_function1)
calculate_button.grid(row = 6, column = 1, pady = 5, padx = 5)

calculate_button1 = Button (mywindow, text = "CalculateFeh",bg="orange" ,command=convert_function)
calculate_button1.grid(row = 6, column = 7, pady = 5, padx = 5)


result_Label = Label(mywindow, text="", relief="solid",font=("Arial", 18 ,"bold"))
result_lbl=Label(mywindow, height=2, width= 20,bg="green")
result_Label.grid(row=6, column=3)
result_lbl.grid(row=6, column=3)

clear_button = Button (mywindow, text = "Clear", command=clear,bg="white")
clear_button.grid(row = 8, column = 1, pady = 5, padx = 5)

exit_button = Button (mywindow, text = "Exit Program",command=mywindow.destroy,bg="red")
exit_button.grid(row = 8, column = 7, pady = 5, padx = 5)

mywindow.mainloop()
