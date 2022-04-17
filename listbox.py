from tkinter import *
  
  
# create a root window.
top = Tk()
  
# create listbox object
listbox = Listbox(top, bg = "grey", font = "Helvetica", fg = "yellow")
  
# Define the size of the window.
#top.geometry("300x250")  
  
# Define a label for the list.  
label = Label(top, text = " FOOD ITEMS") 
  
# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")
  
# pack the widgets
label.pack()
listbox.pack(pady=50)
  
  
# Display untill User 
# exits themselves.
top.mainloop()