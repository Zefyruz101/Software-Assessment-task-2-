from tkinter import *

#Main Window
root = Tk()
root.title("Summing Series")

default_font_name = "Arial"
default_font_size = 9
default_geometry_x = 500
default_geometry_y = 400

root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Text specification
my_text = Text(root)

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
    text_colour = "#6b6567"
    
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
    text_colour = "#6a618a"
    
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

#Lavender Theme
def lavender():
    main_colour = "#ada6c2"
    second_colour = "#423b5c"
    text_colour = "#ffffff"
    select_colour = "#423b5c"

    root.config(bg=main_colour)
    my_text.config(fg=text_colour)
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="white")

    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    arithmetic_button.config(bg=main_colour, fg=select_colour, selectcolor="#F5F5DC")
    geometric_button.config(bg=main_colour, fg=select_colour, selectcolor="#F5F5DC")

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Fonts
def arial_font():
    first_term_entry.config(font=("Arial", 9))
    common_difference_entry.config(font=("Arial", 10))
    num_terms_entry.config(font=("Arial", 9))

    first_term_label.config(font=("Arial", 9))
    common_difference_label.config(font=("Arial", 9))
    common_difference_label.place(x=65, y=100)
    num_terms_label.config(font=("Arial", 9))
    error_label.config(font=("Arial", 9))

    arithmetic_button.config(font=("Arial", 9))
    geometric_button.config(font=("Arial", 9))

    sum_label.config(font=("Arial", 9))
    calculate_button.config(font=("Arial", 9))
    clear_button.config(font=("Arial", 9))
    
def century_gothic():
    first_term_entry.config(font=("Century Gothic", 9))
    common_difference_entry.config(font=("Century Gothic", 9))
    num_terms_entry.config(font=("Century Gothic", 9))

    first_term_label.config(font=("Century Gothic", 9))
    first_term_label.place(x=148, y=75)
    common_difference_label.config(font=("Century Gothic", 9))
    common_difference_label.place(x= 50, y=100)
    num_terms_label.config(font=("Century Gothic", 9))
    error_label.config(font=("Century Gothic", 9))

    arithmetic_button.config(font=("Century Gothic", 9))
    geometric_button.config(font=("Century Gothic", 9))

    sum_label.config(font=("Century Gothic", 9))
    calculate_button.config(font=("Century Gothic", 9))
    clear_button.config(font=("Century Gothic", 9))

def comicsans_font():
    
    first_term_entry.config(font=("Comic Sans MS", 9))
    common_difference_entry.config(font=("Comic Sans MS", 9))
    num_terms_entry.config(font=("Comic Sans MS", 9))

    first_term_label.config(font=("Comic Sans MS", 9))
    first_term_label.place(x=145, y=75)
    common_difference_label.config(font=("Comic Sans MS", 9))
    common_difference_label.place(x=65, y=100)
    num_terms_label.config(font=("Comic Sans MS", 9))
    error_label.config(font=("Comic Sans MS", 9))

    arithmetic_button.config(font=("Comic Sans MS", 9))
    geometric_button.config(font=("Comic Sans MS", 9))

    sum_label.config(font=("Comic Sans MS", 9))
    calculate_button.config(font=("Comic Sans MS", 9))
    clear_button.config(font=("Comic Sans MS", 9))

#test
font_name = default_font_name
font_size = 9
scaling_factor = 1.0

def reset_scaling():
    global font_size
    global geometry_x
    global geometry_y

    font_size = default_font_size * 1
    geometry_x = default_geometry_x * 1
    geometry_y = default_geometry_y * 1

    root.geometry("{width}x{height}".format(width=geometry_x, height=geometry_y))
    first_term_entry.config(font=(font_name , font_size))
    first_term_entry.place(x=220, y=75, width=150, height=20)
    common_difference_entry.config(font=(font_name , font_size))
    common_difference_entry.place(x=220, y=100, width=150, height=20)
    num_terms_entry.config(font=(font_name , font_size))
    num_terms_entry.place(x=220, y=125, width=150, height=20)

    first_term_label.config(font=(font_name , font_size))
    first_term_label.place(x=150, y=75)
    common_difference_label.config(font=(font_name , font_size))
    common_difference_label.place(x=65, y=100)
    num_terms_label.config(font=(font_name , font_size))
    num_terms_label.place(x=110, y=125)
    error_label.config(font=(font_name , font_size))
    error_label.place(x=200, y=250)

    arithmetic_button.config(font=(font_name , font_size))
    arithmetic_button.place(x=100, y=170)
    geometric_button.config(font=(font_name , font_size))
    geometric_button.place(x=100, y=190)

    sum_label.config(font=(font_name , font_size))
    sum_label.place(x=230, y=200)
    calculate_button.config(font=(font_name , font_size))
    calculate_button.place(x=275, y=160)
    clear_button.config(font=(font_name , font_size))
    clear_button.place(x=230, y=160)

    if font_name in ["Century Gothic"]:
        common_difference_label.place(x=55, y=100)
    
    elif font_name in ["Comic Sans MS"]:
        common_difference_label.place(x=70, y=100)
        num_terms_label.place(x=115, y=125)

    elif font_name in ["Georgia"]:
        first_term_label.place(x=140, y=75)
        common_difference_label.place(x=53, y=100)
        num_terms_label.place(x=100, y=125)

    elif font_name in ["Elephant"]:
        first_term_label.place(x=140, y=75)
        common_difference_label.place(x=50, y=100)
        num_terms_label.place(x=100, y=125)

def scaling_150():
    global font_size
    font_size = default_font_size * 2
    root.geometry("600x500")

    first_term_entry.config(font=(font_name , font_size))
    first_term_entry.place(x=300, y=70,width=200)
    common_difference_entry.config(font=(font_name , font_size))
    common_difference_entry.place(x=300, y=100,width=200)
    num_terms_entry.config(font=(font_name , font_size))
    num_terms_entry.place(x=300, y=130,width=200)

    first_term_label.config(font=(font_name , font_size))
    first_term_label.place(x=180, y=65)
    common_difference_label.config(font=(font_name , font_size))
    common_difference_label.place(x=15, y=95)
    num_terms_label.config(font=(font_name , font_size))
    num_terms_label.place(x=103, y=123)
    error_label.config(font=(font_name , font_size))
    error_label.place(x=70, y=300)

    arithmetic_button.config(font=(font_name , font_size))
    arithmetic_button.place(x=70, y=170)
    geometric_button.config(font=(font_name , font_size))
    geometric_button.place(x=70, y=200)

    sum_label.config(font=(font_name , font_size))
    sum_label.place(x=80, y=250)
    calculate_button.config(font=(font_name , font_size))
    calculate_button.place(x=390, y=180)
    clear_button.config(font=(font_name , font_size))
    clear_button.place(x=300, y=180)

    if font_name in ["Century Gothic"]:
        first_term_entry.place(x=330, y=70)
        common_difference_entry.place(x=330, y=100)
        num_terms_entry.place(x=330, y=130)

        first_term_label.place(x=210, y=60)
        common_difference_label.place(x=0, y=90)
        num_terms_label.place(x=117, y=120)

        arithmetic_button.place(x=70, y=170)
        geometric_button.place(x=70, y=205)
        clear_button.place(x=310, y=180)
        calculate_button.place(x=400, y=180)

    elif font_name in ["Comic Sans MS"]:
        first_term_entry.place(x=330, y=70)
        common_difference_entry.place(x=330, y=100)
        num_terms_entry.place(x=330, y=130)

        first_term_label.place(x=200, y=60)
        common_difference_label.place(x=30, y=90)
        num_terms_label.place(x=123, y=120)

        arithmetic_button.place(x=70, y=170)
        geometric_button.place(x=70, y=205)
        clear_button.place(x=310, y=180)
        calculate_button.place(x=400, y=180)
    
    elif font_name in ["Georgia"]:
        first_term_label.place(x=175, y=60)
        common_difference_label.place(x=5, y=90)
        num_terms_label.place(x=100, y=120)

    elif font_name in ["Elephant"]:
        first_term_entry.place(x=370, y=70)
        common_difference_entry.place(x=370, y=100)
        num_terms_entry.place(x=370, y=130)

        first_term_label.place(x=220, y=60)
        common_difference_label.place(x=33, y=90)
        num_terms_label.place(x=140, y=120)

        arithmetic_button.place(x=70, y=170)
        geometric_button.place(x=70, y=205)
        calculate_button.place(x=430, y=180)
        clear_button.place(x=330, y=180)



def update_font():
    new_font = (font_name, int(font_size * scaling_factor))
    for widget in root.winfo_children():
        if isinstance(widget, (Label, Entry, Button, Radiobutton, Text)):
            widget.config(font=new_font)
    if scaling_factor == 1.0:
        reset_scaling()
    elif scaling_factor == 1.5:
        scaling_150()

def change_font(new_font_name):
    global font_name
    font_name = new_font_name
    update_font()

def change_font_size(new_size):
    global font_size
    font_size = new_size
    update_font()

def change_scaling(new_scaling):
    global scaling_factor
    scaling_factor = new_scaling
    update_font()


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
my_menu.add_cascade(label="Themes", menu=options_menu)
options_menu.add_command(label='Original Theme',command = night_off)
options_menu.add_command(label='Night Mode', command = night_on)
options_menu.add_command(label="Beige", command = beige)
options_menu.add_command(label="Retro Beige", command = retro_beige)
options_menu.add_command(label="Aether", command=aether)
options_menu.add_command(label="Blueberry Light", command=blueberry_light)
options_menu.add_command(label="Lavender", command=lavender)

#Font Type buttons
fonts_menu = Menu(my_menu)
my_menu.add_cascade(label="Fonts", menu=fonts_menu)
fonts_menu.add_command(label="Arial", command=lambda: change_font("Arial"))
fonts_menu.add_command(label="Century Gothic", command=lambda: change_font("Century Gothic"))
fonts_menu.add_command(label="Comic Sans MS", command=lambda: change_font("Comic Sans MS"))
fonts_menu.add_command(label="Georgia", command=lambda: change_font("Georgia"))
fonts_menu.add_command(label="Elephant", command=lambda: change_font("Elephant"))

scaling_menu = Menu(my_menu)
my_menu.add_cascade(label="Scaling", menu= scaling_menu)
scaling_menu.add_command(label="100%" , command=lambda: change_scaling(1.0))
scaling_menu.add_command(label="150%" , command=lambda: change_scaling(1.5))


# Initialize font for all widgets
update_font()

#Loops the program
root.mainloop()