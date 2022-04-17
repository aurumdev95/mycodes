#bitcion
import requests
import tkinter as tk
from datetime import datetime

def bitcoin():
	url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
	try:
		response = requests.get(url).json()
		#price = response["USD"]
		time = datetime.now().strftime("%H:%M:%S")
		
		labelprice_us.config(text="USA:"+str(response["USD"]) + "$")
		labelprice_eu.config(text="europe:"+str(response["EUR"]) + "£")
		labelprice_jp.config(text="japan:"+str(response["JPY"]) + "¥")
		
		labeltime.config(text="updated at:"+time)
		canvas.after(1000, bitcoin)
	except:
		labelprice_us.config(text="no connection")
		
canvas = tk.Tk()
#canvas.geometry("400×500")
#canvas.title("bitcoin tracker")


f1 = ("poopins", 15, "bold")
f2 = ("poopins", 13, "bold")
f3 = ("poopins", 10, "normal")


label = tk.Label(canvas, text="Bitcion price", font=f1)
label.pack(pady=20)


labelprice_us = tk.Label(canvas, font=f2)
labelprice_us.pack(pady=20)

labelprice_eu = tk.Label(canvas, font=f2)
labelprice_eu.pack(pady=20)

labelprice_jp = tk.Label(canvas, font=f2)
labelprice_jp.pack(pady=20)

labeltime = tk.Label(canvas, font=f2)
labeltime.pack(pady=20)

bitcoin()
canvas.mainloop()


