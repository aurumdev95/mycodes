import tkinter as tk
import requests 
import datetime
#funcs

def getcoviddata():
	api = 'https://disease.sh/v3/covid-19/all'
	json_data = requests.get(api).json()
	total_cases = str(json_data['cases'])
	total_deaths = str(json_data['deaths'])
	today_cases = str(json_data['todayCases'])
	today_deaths = str(json_data['todayDeaths'])
	today_recovered = str(json_data['todayRecovered'])
	update_at = json_data['updated']
	date = datetime.datetime.fromtimestamp(update_at/1e3)
	label.config(text='total cases:'+total_cases+'\ntotal deaths:'+total_deaths+'\ntoday cases:'+today_cases+'\ntoday deaths:'+today_deaths+'\ntoday recovered:'+today_recovered)
	
	label2.config(text=date)
	



root = tk.Tk()

root.geometry()
root.title('tracker')

button = tk.Button(root, text="load", command=getcoviddata, bg='yellow')
button.pack(pady=20)

label = tk.Label(root)
label.pack(pady=20)


label2 = tk.Label(root)
label2.pack()

menubar = tk.Menu(root)
menubar.add_cascade(label="                        covid 19 tracker")
root.config(menu=menubar)
root.mainloop()