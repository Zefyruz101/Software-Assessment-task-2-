from tkinter import *

#Main Window
root = Tk()
root.title("Summing Series")

#Labels and Entry Widgets
first_term = Label(root, text="First Term: ")
first_term.pack()
first_term_entry = Entry(root)
first_term_entry.pack()

common_difference_label = Label(root, text="Common Difference:")
common_difference_entry = Entry(root)

num_terms_label = Label(root, text="Number of Terms:")
num_terms_entry = Entry(root)
root.mainloop()