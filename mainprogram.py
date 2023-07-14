from tkinter import *

#Main Window
root = Tk()
root.title("Summing Series")
root.geometry("500x400")

#Text specification
my_text = Text(root, font=('arial', 14))

#Calculate Arithmetic and Geometric Series
def calculate_sum():
    try:
        first_term = float(first_term_entry.get())
        common_difference = float(common_difference_entry.get())
        num_terms = int(num_terms_entry.get())

        if var.get() == 1: 
            #arithmetic series calculations
            sum_series = (num_terms/2) * (2 * first_term + (num_terms - 1) * common_difference)
        else:
            #geometric series calculations
            sum_series = (first_term*(1-common_difference**num_terms) / (1-common_difference))
    
        sum_label.config(text="Sum: " + str(sum_series))

    except ValueError:
        show_error("Invalid input! Please enter a valid number")

#Calculating an error message if an invalid input is entered
def show_error(message=""):
    error_label.config(text=message)

    if message:
        root.after(3000, show_error)

#Clear All Text in Entry Fields
def clear():
    first_term_entry.delete(0,END)
    common_difference_entry.delete(0,END)
    num_terms_entry.delete(0,END)
    sum_label.config(text="Sum: ")

#Original Theme, turning off night mode
def night_off():
    main_colour = '#f0f0f0'
    second_colour = 'White'
    text_colour = 'Black'

    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="black")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="black")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="black")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor='White')
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor='White')

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Turn On Night Mode
def night_on():
    main_colour = 'Black'
    second_colour = 'Grey'
    text_colour = 'White'

    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour )

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor='Black')
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor='Black')

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Defining other themes
#Beige theme
def beige(): 
    main_colour = "#F5F5DC"
    second_colour = "#D5BA99"
    text_colour = "#8B4411"
    
    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Retro Beige Theme
def retro_beige(): 
    main_colour = "#eeebe2"
    second_colour = "#d0c9ae"
    text_colour = "#9b9994"
    
    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Aether Theme (Purple-like theme)
def aether():
    main_colour = "#101820"
    second_colour = "#452e54"
    text_colour = "#cf6bdd"
    
    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Blueberry Light Theme
def blueberry_light():
    main_colour = "#dae0f5"
    second_colour = "#8fa4b8"
    text_colour = "#a5a2b0"
    
    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)


def lavender():
    main_colour = "#ada6c2"
    second_colour = "#423b5c"
    text_colour = "#d0cddb"

    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor="#F5F5DC")

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

    
#Labels and Entry Widgets
first_term_label = Label(root, text="First Term: ")
first_term_label.place(x=150, y=75)
first_term_entry = Entry(root)
first_term_entry.place(x=220, y=75, width=150, height=20)

error_label = Label(root, text="")
error_label.place(x=200, y=250)

common_difference_label = Label(root, text="Common Difference/Ratio:")
common_difference_label.place(x=65, y=100) 
common_difference_entry = Entry(root)
common_difference_entry.place(x=220, y=100, width=150, height=20)

num_terms_label = Label(root, text="Number of Terms:")
num_terms_label.place(x=110, y=125)
num_terms_entry = Entry(root)
num_terms_entry.place(x=220, y=125, width=150, height=20)

#Radio Buttons
var = IntVar()
arithmetic_button = Radiobutton(root, variable=var, value=1, text="Arithmetic Series")
arithmetic_button.place(x=100, y=170)

geometric_button = Radiobutton(root, variable=var, value=2, text="Geometric Series")
geometric_button.place(x=100, y=190)

#Output Widgets
sum_label = Label(root, text = "Sum: ")
sum_label.place(x=230, y=200)

#Calculate and Clear Buttons
calculate_button = Button(root, text="Calculate", command=calculate_sum)
calculate_button.place(x=275, y=160)

clear_button = Button(root, text="Clear", command=clear)
clear_button.place(x=230, y=160)

#File buttons
my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.destroy)

#Options buttons
options_menu = Menu(my_menu)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label='Original Theme',command = night_off)
options_menu.add_command(label='Night Mode', command = night_on)
options_menu.add_command(label="Beige", command = beige)
options_menu.add_command(label="Retro Beige", command = retro_beige)
options_menu.add_command(label="Aether", command=aether)
options_menu.add_command(label="Blueberry Light", command=blueberry_light)
options_menu.add_command(label="Lavender", command=lavender)

#Loops the program
root.mainloop()