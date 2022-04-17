import requests
from bs4 import BeautifulSoup
import webbrowser

site = requests.get('https://www.reb.gov.rw/home')

html = BeautifulSoup(site.text, 'html.parser')

#href = html.find_all('href')
#print(href)
#print(html.prettify())
links = [a['href'] for a in html.find_all('a', href=True) if a.text] 
#for link in range(len(links)):
#	print(link, links[link])

#tags = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag.text) ...
#links = [a['href'] for a in soup.find_all('a', href=True)]



#webbrowser.open(links[17])
#import webbrowser


#webbrowser.get("google-chrome").open(links[17])