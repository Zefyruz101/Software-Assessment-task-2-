from tkinter import *

#Main Window
root = Tk()
root.title("Summing Series")

#Text specification
my_text = Text(root, font=('arial', 14))

#Calculate Arithmetic and Geometric Series
def calculate_sum():
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

#Clear All Text
def clear():
    first_term_entry.delete(0,END)
    common_difference_entry.delete(0,END)
    num_terms_entry.delete(0,END)
    sum_label.config(text="Sum: ")

#Original Theme, turning off night mode
def night_off():
    main_colour = 'White'
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

    arithmetic_button.config(bg=main_colour, fg=text_colour, selectcolor='Black')
    geometric_button.config(bg=main_colour, fg=text_colour, selectcolor='Black')

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)

#Defining other themes
def brown(): #A0816C
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

    arithmetic_button.config(bg=main_colour, fg=text_colour)
    geometric_button.config(bg=main_colour, fg=text_colour)

    sum_label.config(bg=main_colour, fg=text_colour)
    calculate_button.config(bg=main_colour, fg=text_colour)
    clear_button.config(bg=main_colour, fg=text_colour)


#Labels and Entry Widgets
first_term_label = Label(root, text="First Term: ")
first_term_label.pack()
first_term_entry = Entry(root)
first_term_entry.pack()

common_difference_label = Label(root, text="Common Difference/Ratio:")
common_difference_label.pack()
common_difference_entry = Entry(root)
common_difference_entry.pack()

num_terms_label = Label(root, text="Number of Terms:")
num_terms_label.pack()
num_terms_entry = Entry(root)
num_terms_entry.pack()

#Radio Buttons
var = IntVar()
arithmetic_button = Radiobutton(root, variable=var, value=1, text="Arithmetic Series")
arithmetic_button.pack()

geometric_button = Radiobutton(root, variable=var, value=2, text="Geometric Series")
geometric_button.pack()

#Output Widgets
sum_label = Label(root, text = "Sum: ")
sum_label.pack()

#Calculate and Clear Buttons
calculate_button = Button(root, text="Calculate", command=calculate_sum)
calculate_button.pack()

clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()

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
options_menu.add_command(label="Beige", command = brown)

#Loops the program
root.mainloop()