from tkinter import *

#Main Window
root = Tk()
root.title("Summing Series")

#Setting basic variables for fonts, and window sizing
default_font_name = "Arial"
default_font_size = 9
default_geometry_x = 500
default_geometry_y = 400

#Calling variables for window sizing
root.geometry("{width}x{height}".format(width=default_geometry_x, height=default_geometry_y))

#Text specification
my_text = Text(root)

#Calculate Arithmetic and Geometric Series
def calculate_sum():
    try: #Using entry fields to obtain float integers and save it 
        first_term = float(first_term_entry.get())
        common_difference = float(common_difference_entry.get())
        num_terms = int(num_terms_entry.get())

        if var.get() == 1: 
            #arithmetic series calculations, if series button is pressed
            sum_series = (num_terms/2) * (2 * first_term + (num_terms - 1) * common_difference)
        else:
            #geometric series calculations, if option 2 of series button is pressed
            sum_series = (first_term*(1-common_difference**num_terms) / (1-common_difference))
        #Displaying sum of chosen series, attached onto label
        sum_label.config(text="Sum: " + str(sum_series))
    #When a non integer is entered into entry fields  
    except ValueError:
        show_error("Invalid input! Please enter a valid number")

#Calculating an error message if an invalid input is entered
def show_error(message=""):
    error_label.config(text=message)

    if message: # 3000 being 3 seconds, timing for the error before dissapearing
        root.after(3000, show_error)

#Clear All Text in Entry Fields
def clear():
    first_term_entry.delete(0,END) #Delete terms in first entry field
    common_difference_entry.delete(0,END) # Delete terms in second entry field
    num_terms_entry.delete(0,END) # Delete terms in third entry fields
    sum_label.config(text="Sum: ") # Delete printed value in sum_label

#Original Theme, turning off night mode
def night_off():
    main_colour = '#f0f0f0' # Setting variables to be called within the function
    second_colour = 'White' # Hex codes / colours 
    text_colour = 'Black' # Three main colours

    root.config(bg=main_colour) # Background set to main colour
    my_text.config(fg=text_colour) # Text colour set for text 
    first_term_entry.config(fg=text_colour, bg=second_colour, insertbackground="black") # secondary colour for entry fields, and text cursor colour
    common_difference_entry.config(fg=text_colour, bg=second_colour, insertbackground="black") #insertbackground = cursor colour
    num_terms_entry.config(fg=text_colour, bg=second_colour, insertbackground="black")

    #Setting label colours  
    first_term_label.config(bg=main_colour, fg=text_colour)
    common_difference_label.config(bg=main_colour, fg=text_colour)
    num_terms_label.config(bg=main_colour, fg=text_colour)
    error_label.config(bg=main_colour, fg=text_colour)

    #Select colour being colour of selected radiobutton
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

#Define variables for scaling, and font size
font_name = default_font_name
font_size = 9
scaling_factor = 1.0

#100% scaling, original scaling
def reset_scaling():
    global font_size #Setting global font size to 9 
    global geometry_x # Setting x window size
    global geometry_y # Setting y window size

    font_size = default_font_size * 1 # Multiplying font size by 1 for basic scaling
    geometry_x = default_geometry_x * 1 # Multiplying x window size by 1 for original scaling
    geometry_y = default_geometry_y * 1 # Multiplying y window size by 1 for original scaling

    root.geometry("{width}x{height}".format(width=geometry_x, height=geometry_y)) # Window size
    first_term_entry.config(font=(font_name , font_size)) # Selected font name and font size for each entries
    first_term_entry.place(x=220, y=75, width=150, height=20) # Placing in correct position 
    common_difference_entry.config(font=(font_name , font_size))
    common_difference_entry.place(x=220, y=100, width=150, height=20) # Placing in correct position 
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

#150% scaling, 1,5 * original_scaling
def scaling_150():
    global font_size 
    font_size = default_font_size * 2
    root.geometry("600x500") # Window size for scaling * 1.5

    #Same usage of font_name, size and placing in new window size of Arial Font
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

    #If selected font is Century Gothic, place in these positions 
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

    #If selected font is Comic Sans MS, place in these positions 
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
    
    #If selected font is Georgia, place in these positions 
    elif font_name in ["Georgia"]:
        first_term_label.place(x=175, y=60)
        common_difference_label.place(x=5, y=90)
        num_terms_label.place(x=100, y=120)

    #If selected font is Elephant, place in these positions 
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

#Updating font when different font is selected, including all children inside window
def update_font():
    new_font = (font_name, int(font_size * scaling_factor)) #font name * scaling factor
    for widget in root.winfo_children():
        if isinstance(widget, (Label, Entry, Button, Radiobutton, Text)):
            widget.config(font=new_font) # Changing font into new font if selected
    if scaling_factor == 1.0: # If scaling factor = 1, revert to original scaling / 100%
        reset_scaling()
    elif scaling_factor == 1.5: # If scaling factor = 1.5, change to 150% scaling 
        scaling_150()

def change_font(new_font_name): # Define global font, update font name with selected font
    global font_name
    font_name = new_font_name
    update_font()

def change_font_size(new_size): # Define global font size, update font size depending on scaling
    global font_size
    font_size = new_size
    update_font()

def change_scaling(new_scaling): # Define global scaling size, update scalign size depending on selected option
    global scaling_factor
    scaling_factor = new_scaling
    update_font()

#Labels and Entry Widgets
first_term_label = Label(root, text="First Term: ")
first_term_label.place(x=150, y=75)
first_term_entry = Entry(root)
first_term_entry.place(x=220, y=75, width=150, height=20)

#Error label when incorrect variable is entered
error_label = Label(root, text="")
error_label.place(x=200, y=250)

#Common Difference / Ratio labels and entry fields
common_difference_label = Label(root, text="Common Difference/Ratio:")
common_difference_label.place(x=65, y=100) 
common_difference_entry = Entry(root)
common_difference_entry.place(x=220, y=100, width=150, height=20)

#Number of terms labels and entry fields
num_terms_label = Label(root, text="Number of Terms:")
num_terms_label.place(x=110, y=125)
num_terms_entry = Entry(root)
num_terms_entry.place(x=220, y=125, width=150, height=20)

#Radio Buttons
var = IntVar() 
#Defining as radiobutton, giving value of 1 and placing
arithmetic_button = Radiobutton(root, variable=var, value=1, text="Arithmetic Series")
arithmetic_button.place(x=100, y=170)

#Defining as radiobutton, giving value of 2 and placing
geometric_button = Radiobutton(root, variable=var, value=2, text="Geometric Series")
geometric_button.place(x=100, y=190)

#Output Widgets for Sum
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

#Menu for exiting
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.destroy)

#Themes & Options
themes_menu = Menu(my_menu)
my_menu.add_cascade(label="Themes", menu=themes_menu)
themes_menu.add_command(label='Original Theme',command = night_off)
themes_menu.add_command(label='Night Mode', command = night_on)
themes_menu.add_command(label="Beige", command = beige)
themes_menu.add_command(label="Retro Beige", command = retro_beige)
themes_menu.add_command(label="Aether", command=aether)
themes_menu.add_command(label="Blueberry Light", command=blueberry_light)
themes_menu.add_command(label="Lavender", command=lavender)

#Font Type Selection
fonts_menu = Menu(my_menu)
my_menu.add_cascade(label="Fonts", menu=fonts_menu)
fonts_menu.add_command(label="Arial", command=lambda: change_font("Arial")) # Setting to Arial
fonts_menu.add_command(label="Century Gothic", command=lambda: change_font("Century Gothic")) # Setting to Century Gothic
fonts_menu.add_command(label="Comic Sans MS", command=lambda: change_font("Comic Sans MS")) # Setting to Comic Sans MS
fonts_menu.add_command(label="Georgia", command=lambda: change_font("Georgia")) # Setting to Georgia
fonts_menu.add_command(label="Elephant", command=lambda: change_font("Elephant")) # Setting to Elephant

#Scaling menu of 100% and 150%
scaling_menu = Menu(my_menu)
my_menu.add_cascade(label="Scaling", menu= scaling_menu)
scaling_menu.add_command(label="100%" , command=lambda: change_scaling(1.0)) #New scaling factor is set to 1.0
scaling_menu.add_command(label="150%" , command=lambda: change_scaling(1.5)) # New scaling factor is set to 1.5


# Initialize font for all widgets
update_font()

#Loops the program
root.mainloop()