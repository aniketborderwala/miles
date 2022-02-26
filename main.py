from tkinter import *
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)


def button_clicked():
    new_text = int(input.get())
    km = float(new_text*1.609)
    label_4.config(text=f"{km}")


#label

my_label = Label(text="Miles", font=("Detective", 10))
my_label.grid(column=10, row=2)
my_label.config(padx=5, pady=5)

label_2 = Label(text="is equal to", font=("Detective", 10))
label_2.grid(column=2, row=4)
label_2.config(padx=5, pady=5)

label_3 = Label(text="km", font=("Detective", 10))
label_3.grid(column=10, row=4)
label_3.config(padx=5, pady=5)

label_4 = Label(text="0", font=("Detective", 10))
label_4.grid(column=8, row=4)
label_4.config(padx=5, pady=5)

#button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=8, row=20)



#Entryy
input = Entry(width=15)
input.grid(column=8, row=2)
input.get()



















window.mainloop()
