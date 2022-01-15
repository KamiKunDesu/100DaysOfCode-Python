from tkinter import *

def button_clicked():
    '''A function that alerts you to when a window button is clicked, and changes some text in the window to match
    some input'''
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title('My second GUI program')
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=('Arial', 24, 'bold'))
my_label.config(text='New Text')
my_label.grid(column=0,row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Second Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)

window.mainloop()