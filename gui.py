from tkinter import *
import customtkinter


window = Tk()
window.geometry("420x420")
window.title("Tip Calculator")
customtkinter.set_appearance_mode("dark")

def tip():
    a=int(amount_entry.get())
    b=(tip_entry.get())
    if b.endswith("%"):
        b=int(b[:-1])
    else:
        b=int(b)
    t=(b/100)*a
    print(f"The tip is {t}")



Label(window, text="Enter amount:").pack()
amount_entry = Entry(window)
amount_entry.pack()

Label(window, text="Enter tip percentage:").pack()
tip_entry = Entry(window)
tip_entry.pack()

Button(window, text="Calculate", command=tip).pack()

result_label = Label(window, text="")
result_label.pack()
window.mainloop()
