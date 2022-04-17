import speech_recognition as sr
r = sr.Recognizer()

def record_audio():
	with sr.Microphone as source:
		audio = r.listen(source, 5, 5)
		voice_data = ""
		try:
			voice_data = r.recognize_google(audio)
			
		except sr.UnknownValueError:
			print("error")
		except sr.RequestError:
			print("server down")
			
	print(">>", voice_data.lower())
	
record_audio()
	
			
			