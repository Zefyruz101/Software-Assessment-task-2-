from tkinter import *

def calculate_sum():
    pass

def clear():
    pass

#Main Window
root = Tk()
root.title("Summing Series")

#Labels and Entry Widgets
first_term = Label(root, text="First Term: ")
first_term.pack()
first_term_entry = Entry(root)
first_term_entry.pack()

common_difference = Label(root, text="Common Difference/Ratio:")
common_difference.pack()
common_difference_entry = Entry(root)
common_difference_entry.pack()

num_terms = Label(root, text="Number of Terms:")
num_terms.pack()
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


root.mainloop()