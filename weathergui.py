import requests
from tkinter import *
font = ('calibri', 7, 'bold')
root = Tk()

def main():
	#api_key 
	city = e.get()
	try:
		data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=54c46528d01118ffff548326dbdbb0f6').json()
		#print(data)
		
		#datas
		
		lon = data['coord']['lon']
		lat = data['coord']['lat']
		weather = data['weather']
		main = weather[0]['main']
		main2 = weather[0]['description']
		mainw = data['main']
		t = mainw['temp']
		t_max = mainw['temp_max']
		t_min = mainw['temp_min']
		pressure = mainw['pressure']
		hum = mainw['humidity']
		visibility = data['visibility']
		wind = data['wind']
		try:
			rain = data['rain']
		except:
			rain = "can not get rain data.."
		clouds = data['clouds']
		country = 				  data['sys']['country']
		#print(lon, lat, weather, main2, t, t_max, t_min, pressure, hum, visibility, wind, rain, clouds, country)

		label.config(text=f"city name:{city}, country:{country}\n\ncity coordinates:latitude:{lat},longitude:{lon}\n\nthere will be {main}, {main2}\n\ntemperature: {t},\n- max temperature:{t_max} min temperature:{t_min}\n\npressure:{pressure}\n\nhumidity:{hum}\n\nvisibility:{visibility}\n\nwind: speed:{wind['speed']}, direction:{wind['deg']}\n\nrain: {rain}\n\nclouds: {clouds}")
	except:
		label.config(text='error please check city name or connection')
	
	



def click():
	label.config(text='hello:' + e.get())

e = Entry(root)
e.pack(pady=20)
e.insert(0, 'enter city name')

label = Label(root, text='weather data here..', font=font)
label.pack(pady=20)

button = Button(root, text='load data', command=main)
button.pack()

menubar = Menu(root)
menubar.add_cascade(label="                              weather app ")
root.config(menu=menubar)
root.mainloop()


#{'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'base': 'stations', 'main': {'temp': 280, 'feels_like': 277.82, 'temp_min': 278.87, 'temp_max': 281.07, 'pressure': 1011, 'humidity': 92}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 230}, 'rain': {'1h': 0.56}, 'clouds': {'all': 82}, 'dt': 1641509942, 'sys': {'type': 2, 'id': 2019646, 'country': 'GB', 'sunrise': 1641456297, 'sunset': 1641485233}, 'timezone': 0, 'id': 2643743, 'name': 'London', 'cod': 200}

