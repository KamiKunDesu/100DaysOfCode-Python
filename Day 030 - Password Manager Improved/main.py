'''Day 030 - The purpose of this project is to improve on the password manager from the previous day by adding
JSON format for the storage of the user and passwords, to make the passwords searchable by website name. Also
adding exception handling for potential errors'''

from email import message
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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

    # First lets get the entries and store them in variables, making the website string lower in order to make search work better
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Check the user has the right data inputted
    is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {email} "
                        f"\nPassword: {password} \nIs it ok to save this data?")

    # If the do then go through with process
    if is_ok and (len(password) > 0 and len(website) > 0 and len(email) > 0):
        
        
        # We're going to try and get the json file and update it if it already exists
        try: 
            # Open the file in read to get the Json already in there
            with open("./../../sick_band_names.json", "r") as password_file:
                # First load the json
                data = json.load(password_file)
                # Update it with the new data
                data.update(new_data)
            
            # Re open the file in write mode in order to write the new data
            with open("./../../sick_band_names.json", "w") as password_file:
                # Dump the updated data
                json.dump(data, password_file, indent=4)
        
        # Handle file not found error
        except FileNotFoundError:
            # In this case we need to create the file and write it
            with open("./../../sick_band_names.json", "w") as password_file:
                # Write the entry to the file
                json.dump(new_data, password_file, indent=4)
        
        # These final actions should execute whether or not the file had to be created or was found
        finally:
            # Delete the text in website and password entry to make it clear something has happened
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # Refocus the cursor to the first field
            website_entry.focus()
            # Give a pop up to say the password is added
            messagebox.showinfo(title="Password Added", message="Password Successfully Added!")

    # If they say things are ok however one of the fields is empty show an error
    elif is_ok and not (len(password) > 0 and len(website) > 0 and len(email) > 0):
        messagebox.showerror(title="Validation Error", message=f"The following fields are empty: \n"
                                                               f"{'website, '*(len(website)==0)}{'email, '*(len(email)==0)}{'password'*(len(password)==0)}"
                                                               "\nPlease make sure all fields have something entered")
    
    # Return whether the process was complete or not
    return 

# ------------------------- LOADING PASSWORD -------------------------- #
def load_password():
    '''This function searches the website and loads the password and email associated with the password
    from the JSON store'''

    # We're going to need to handle 2 possible exceptions, a FileNotFound error if the user tries to search
    # a website before the first password is added, and a KeyError if the user searches for a website
    # that doesn't have a password stored
    
    # First let's store the website name for the key in the variable. If there is nothing in the website
    # box then we're going to show a message box to add something
    website = website_entry.get().lower()
    if not website:
        messagebox.showerror(title="Nothing in Search Field", message="There is nothing in the website field\n\nPlease add a website to search the email and password for")
        return
    
    # Next we're going to try and open the Json file and load it, if there is a file not found error we're going to print a message
    # saying that the file doesn't exist and return
    try:
        with open("./../../sick_band_names.json", "r") as password_file:
                # First load the json
                data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="There has been no password file created, likely because this is the first use of the program or the password file has been deleted.\n\nPlease add a new password to use the search function.")

    # Next we try to search for the website and return the email and password
    try:
        email = data[website]["email"]
        password = data[website]["password"]
    except KeyError:
        messagebox.showerror(title="Website Not Found", message="There is no email and password stored for this website.")
        return

    # If these two end with no issues then print the email and password
    messagebox.showinfo(title="Website Login Details", message=f"Email: {email}\nPassword: {password}")
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
website_entry.grid(column=1, row=1, columnspan=1,sticky="EW")
email_entry.grid(column=1, row=2, columnspan=2,sticky="EW")
password_entry.grid(column=1, row=3,sticky="EW")
# Adding a quick line so that the cursor automatically appears in the first entry on program startup
website_entry.focus()
# Also store most common email address as prepopulated in the email entry
email_entry.insert(0, "aarongreenemail@gmail.com")
#Finally we make the buttons, include the relevant commands
generate_button = Button(text="Generate Password",padx=0,command=generate_password)
add_button = Button(text="Add", width=30,padx=0,command=save_password)
search_button = Button(text="Search", command=load_password)
# Then pack them
generate_button.grid(column=2,row=3,sticky="EW")
add_button.grid(column=1,row=5,columnspan=2,sticky="EW")
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()