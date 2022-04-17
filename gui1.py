import tkinter as tk

num = 0
def display(num):
	text.set(str(num))
	
def add(num):
	num = num + 100
	display(num)

		
		
root = tk.Tk()

canvas = tk.Canvas(root, height=200, width=600)
canvas.grid(columnspan=6, rowspan=3)


	
	
	
text = tk.StringVar()
txt_label = tk.Label(root, textvariable=text)
text.set('hello world')
txt_label.grid(column=4, row=0)



button = tk.Button(root, text="add", command=add(num), bg="yellow")
button.grid(column=4, row=1)





menubar = tk.Menu(root)
menubar.add_cascade(label="                                          test")
root.config(menu=menubar)

root.mainloop()