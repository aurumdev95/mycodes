import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=6, rowspan=3)

image = Image.open('test.png')
image = ImageTk.PhotoImage(image)
image_label = tk.Label(image=image)
image_label.image = image
image_label.grid(column=5, row=0)

def open_file():
	text.set('its working')
text = tk.StringVar()
instr = tk.Label(root, textvariable=text)
text.set('hello world')
instr.grid(columnspan=3, column=4, row=1)

browse_text = tk.StringVar()
button = tk.Button(root, textvariable=browse_text, command=open_file, bg='blue', fg="white", height=2, width=15)
browse_text.set('hey')
button.grid(column=5, row=2)

root.mainloop() 
  
   
    
 