'''Day 27 of 100 days of code python challenge - The purpose of todays project is to make a pomodoro timer, which is 
a type of program to help manage time blocks for the pomodoro productivity technique which is documented further here:
https://en.wikipedia.org/wiki/Pomodoro_Technique

I was quite excited about making this program because this is a technique I use myself to help with my productivity, it
gave me a good chance to get to grips with GUIs and also I tried my hand at designing my own buttons in adobe
illustrator so that was fun, even if they do look a bit amateur.
'''


from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Setting up global variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    '''This function will reset the timer back to the it's default state'''
    # Stop the timer
    window.after_cancel(timer)
    # Reset all text
    canvas.itemconfig(timer_text, text="00:00")
    time_stage.config(text="")
    tickmark.config(text="")
    # Reset reps
    global REPS
    REPS = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    '''This function is linked to the start button so that when the start button is pressed this function
    calls the count_down function'''
    # Bring in Global Reps
    global REPS

    # Configure and grid the label
    time_stage.config(text="Work Period")
    time_stage.grid(column=2, row=1)

    # Check if we're at the beginning of a cycle or at the end of a cycle
    if REPS == 0 or REPS == 8:
            REPS = 1
    # Add one onto the reps if we're not at the beginning or end of a cycle
    else:
        REPS += 1
    # If we're on a work cycle then call with work time
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        worktime = int(work_time_spinbox.get())
        count_down(worktime*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    '''This is a recursive function that starts with a number and counts down to 0'''
    # Bring in global REPS
    global REPS
    
    # Get the minutes and seconds
    count_min = count // 60
    count_sec = count % 60

    # Update the text on the canvas, there is a clever f string which uses boolean logic and string arithmetic to keep it in a good format
    canvas.itemconfig(timer_text, text=f'{"0"*(len(str(count_min))<2)}{count_min}:{"0"*(len(str(count_sec))<2)}{count_sec}')

    # Allows the timer to become an object which can be killed with the reset button
    global timer

    if count > 0:
        # If count not at 0 then call 
        timer = window.after(1000, count_down, count - 1)
    if count == 0 and (REPS == 1 or REPS == 3 or REPS == 5):
        # Call the short break immediately
        shorttime = int(short_time_spinbox.get())
        # Increase REPS by 1
        REPS += 1
        # Configure Label
        time_stage.config(text="Short Break")
        # Add necessary tickmarks
        tickmark.config(text="✔"*int(((REPS+1)/2)))
        # Call Count with short break time
        timer = window.after(1000, count_down, shorttime*60)
    elif count == 0 and REPS == 7:
        # Call the long break counter immediately if it turns out that there have been a certain amount of reps
        longtime = int(long_time_spinbox.get())
        REPS += 1
        # Configure Label
        time_stage.config(text="Long Break")
        # Add necessary tickmarks
        tickmark.config(text="✔"*int(((REPS+1)/2)))
        # Call count with long break time
        timer = window.after(1000, count_down, longtime*60)
    elif count == 0:
        time_stage.config(text="")

# ---------------------------- UI SETUP ------------------------------- #
# Set up a window
window = Tk()
# Set the title
window.title("Pomodoro")
# Add some padding to the window so the image doesn't take up the whole screen
window.config(padx=100, pady=50, bg=YELLOW)

# Make a canvas to overlay images on top of each other in the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Read the necessary image in as a photo image class
tomato_image = PhotoImage(file="tomato.png")
# Add image to the canvas
canvas.create_image(100, 112, image=tomato_image)
# Add text onto the canvas, also store it in a variable
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
# Pack the canvas into the screen
canvas.grid(column=1,row=1)

# Make a Label for the UI
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Comic Sans MS", 25, "bold"))
# Pack it onto the screen
timer_label.grid(column=1, row=0)

# Make a photo image out of both the start and reset buttons
start_button_img = PhotoImage(file="start_button.png")
reset_button_img = PhotoImage(file="reset_button.png")

# Make a start button
start_button = Button(image=start_button_img, borderwidth=0, bg=YELLOW, command=start_timer)
# Add it onto the window
start_button.grid(column=0, row=2)
# Make a reset button
reset_button = Button(image=reset_button_img, borderwidth=0, bg=YELLOW, command=reset_timer)
# Add it onto the window
reset_button.grid(column=2, row=2)

# Make some spinbox and labels to help decide the amount of time for each section, add them into a frame and then add that onto a window
# Explain the process once in comments and then repeat again twice because it's the same thing

# First make a frame to store the label and spinbox in
work_time_frame = Frame(window, borderwidth=0, bg=YELLOW, relief="flat")
# Create the label and the spinbox, make sure their parent is the frame
work_time_label = Label(work_time_frame, text="Work Time: ", bg=YELLOW, borderwidth=2)
work_time_label.pack(side="left")
# Pack them into the frame
work_time_spinbox = Spinbox(work_time_frame, from_=0, to=60, borderwidth=2, width=5)
work_time_spinbox.pack(side="right")
# Finally add the frame to the main window using the grid method
work_time_frame.grid(column=0, row=4)

# Repeat for short break, and long break
short_time_frame = Frame(window, borderwidth=0, bg=YELLOW, relief="flat")
short_time_label = Label(short_time_frame, text="Short Break Time: ", bg=YELLOW, borderwidth=2)
short_time_label.pack(side="left")
short_time_spinbox = Spinbox(short_time_frame, from_=0, to=60, borderwidth=2, width=5)
short_time_spinbox.pack(side="right")
short_time_frame.grid(column=1, row=4)

long_time_frame = Frame(window, borderwidth=0, bg=YELLOW, relief="flat")
long_time_label = Label(long_time_frame, text="Long Break Time: ", bg=YELLOW, borderwidth=2)
long_time_label.pack(side="left")
long_time_spinbox = Spinbox(long_time_frame, from_=0, to=60, borderwidth=2, width=5)
long_time_spinbox.pack(side="right")
long_time_frame.grid(column=2, row=4)


# Make the checkmark label and add it onto the window
tickmark = Label(text="", bg=YELLOW, fg=GREEN, font=("Comic Sans MS", 10, "bold"))
tickmark.grid(column=1, row=3)

# Add a label to let you know which stage of the timer it's on
time_stage = Label(text="Work Period", bg=YELLOW, fg=GREEN, font=("Comic Sans MS", 25, "bold"))

# Make sure the window continues to run
window.mainloop()