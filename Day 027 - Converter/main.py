'''Day 27 of 100 days of code python challenge - The purpose of todays project is to make a program which is a GUI that
converts from miles to kilometers which will help to demonstrate knowledge of GUIs and the Tkinter module
'''
from tkinter import *

# First make a window
window = Tk()
# Set the title
window.title("Miles to Kilometers Converter")
# Set the size
window.minsize()
# Add some padding to the window
window.config(padx=20, pady=20)

# Make an input to get the miles in and set it's position
miles_input = Entry()
miles_input.grid(column=1, row=0)

# Make all the labels necessary and set their position
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Make the function which calculates the km from the miles and then changes the label
def calculate_km():
    '''This function converts miles to kilometers and then adjusts the appropriate widget to display the result'''
    # Get miles from the entry widget
    miles = float   (miles_input.get())
    # Convert them to km
    km = round(miles*1.609, 2)
    # Update the label to the result
    kilometer_result_label.config(text=km)

# Make a button for the final calculate and set its position
calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2)

# Keep the program running
window.mainloop()