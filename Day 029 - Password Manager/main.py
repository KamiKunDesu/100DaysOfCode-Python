'''Day 029 - The purpose of this project is to make a password manager which can generate passwords for websites
and store them on a local machine. It will be developed using the Tkinter GUI'''

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    '''This function generates a random password for the user'''

    # First we need to store all our letters and numbers and symbol
    letters = sorted([chr(num) for num in range(97,123)] + [chr(num) for num in range(65,91)])
    numbers = [str(num) for num in range(0,10)]
    symbols = ['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|','\\',':',';','"',"'",'<',',','>','.','?','/']

    # Then randomly generate the number of letters, numbers and symbols
    nr_letters = random.randint(8,10)
    nr_numbers = random.randint(2,4)
    nr_symbols = random.randint(2,4)

    # Clear whatever is already in the password entry
    password_entry.delete(0, END)
    
    # Make a list to store the different password items in
    password_list = []
    # Append the correct number of letters, numbers and symbols to the password list choosing from each list randomly
    password_list += [random.choice(letters) for i in range(nr_letters)] + [random.choice(numbers) for i in range(nr_numbers)] + [random.choice(symbols) for i in range(nr_symbols)]
    # Give one more shuffle to make sure numbers, letters and symbols are mixed together in a random order
    random.shuffle(password_list)
    # Finally produce password
    password = ''.join(password_list)
    # Put the password in the field
    password_entry.insert(0, password)
    # Copy the password to the clipboard
    pyperclip.copy(password)
    #Return from the function
    return 

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    '''This function will take the data from the input fields in the program and then store them
    in a file location in a specified format, it will serve as a command for the add button'''

    # First lets get the entries and store them in variables
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check the user has the right data inputted
    is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \n Email: {email} "
                        f"\nPassword: {password} \nIs it ok to save this data?")

    # If the do then go through with process
    if is_ok and (len(password) > 0 and len(website) > 0 and len(email) > 0):
        # Lets open a file to store the passwords in
        with open("./../../sick_band_names.txt", "a") as password_file:
            # Compile the entry variables into a formatted string
            string_final = f'{website} | {email} | {password}\n'
            # Write the entry to the file
            password_file.write(string_final)
            # Finally delete the text in website and password entry to make it clear something has happened
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # Refocus the cursor to the first field
            website_entry.focus()
            # Give a pop up to say the password is added
            messagebox.showinfo(title="Password Added", message="Password Successfully Added!")
        # Close context
    # If they say things are ok however one of the fields is empty show an error
    elif is_ok and not (len(password) > 0 and len(website) > 0 and len(email) > 0):
        messagebox.showerror(title="Validation Error", message=f"The following fields are empty: \n"
                                                               f"{'website, '*(len(website)==0)}{'email, '*(len(email)==0)}{'password'*(len(password)==0)}"
                                                               "\nPlease make sure all fields have something entered")
    # Return whether the process was complete or not
    return 

# ---------------------------- UI SETUP ------------------------------- #

# Set up a window
window = Tk()
# Set the title
window.title("Password Manager")
# Add some padding to the window so the image doesn't take up the whole screen
window.config(padx=50, pady=50, bg="#ffffff")

# NB: For all the following where Stick="EW" is seen in grid this is to fix the alignment
# issues that were being caused by using widths. This essentially just sticks the widget
# to the east and west of the grid cell which it is in removing any margins

# Make a canvas to overlay images on top of each other in the window, this is for the main image
canvas = Canvas(width=200, height=200, bg="#ffffff", highlightthickness=0)
# Read the necessary image in as a photo image class
lock_image = PhotoImage(file="logo.png")
# Add image to the canvas
canvas.create_image(100, 100, image=lock_image)
# Pack the canvas into the screen
canvas.grid(column=1,row=0,sticky="EW")

# Now let's make the labels
website_label = Label(text="Website:", bg="#fff", padx=0)
email_label = Label(text="Email/Username:", bg="#fff", padx=0)
password_label = Label(text="Password:", bg="#fff",padx=0)
# Then we pack these into the window
website_label.grid(column=0, row=1,sticky="EW")
email_label.grid(column=0, row=2,sticky="EW")
password_label.grid(column=0, row=3,sticky="EW")

# Next let's make the 3 entries, they have different widths and column spans so need to include that
website_entry = Entry(width=35, bg='#fff')
email_entry = Entry(width=35, bg='#fff')
password_entry = Entry(width=21, bg='#fff')
# Then pack them
website_entry.grid(column=1, row=1, columnspan=2,sticky="EW")
email_entry.grid(column=1, row=2, columnspan=2,sticky="EW")
password_entry.grid(column=1, row=3,sticky="EW")
# Adding a quick line so that the cursor automatically appears in the first entry on program startup
website_entry.focus()
# Also store most common email address as prepopulated in the email entry
email_entry.insert(0, "aarongreenemail@gmail.com")
#Finally we make the buttons, include the relevant commands
generate_button = Button(text="Generate Password",padx=0,command=generate_password)
add_button = Button(text="Add", width=30,padx=0,command=save_password)
# Then pack them
generate_button.grid(column=2,row=3,sticky="EW")
add_button.grid(column=1,row=5,columnspan=2,sticky="EW")

window.mainloop()
