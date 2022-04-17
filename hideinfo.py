def writeinfo(info: str, image: str):
	with open(image, 'ab') as f:
		f.write(b"{info}")
		
		
def readinfo(encimg: str):
	try:
		with open(encimg, 'rb') as f:
			content = f.read()
			offset = content.index(bytes.fromhex('FFD9'))
			f.seek(offset + 2)
			#print(f.read())
			return f.read()
	except:
		return "not encoded"
	
import PIL.Image
import io

def writeimg(image: str, imgenc: str):
	img = PIL.Image.open(image)
	byte_arr = io.BytesIO()
	img.save(byte_arr, format='PNG')
	
	with open(imgenc, 'ab') as f:
		f.write(byte_arr.getvalue())

def readimg(imgenc: str, option="save"):
	try:
		with open(imgenc, 'rb') as f:
			content = f.read()
			offset = content.index(bytes.fromhex('FFD9')) 
			f.seek(offset + 2)
			if option == "save":
				new_img  = PIL.Image.open(io.BytesIO(f.read()))
				new_img.save('new image.png')
				return "image saved"
			else:
				return PIL.Image.open(io.BytesIO(f.read()))
	except:
		return "image not encoded"
		
#print('test image start..')
#a = input()
#writeinfo('hello world', "test.jpg")
#b = input()
#readimg()
#print('success..')