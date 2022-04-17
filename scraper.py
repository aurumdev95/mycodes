import requests
payload = {'api_key': 'a97e78b9cb40d10651d64862fc0d9514', 'url': 'https://www.sciencealert.com/'}
r = requests.get('http://api.scraperapi.com', params=payload)
print(r.text)