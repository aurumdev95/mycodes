import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link: ")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = soup.find_all('a')
a = []
for link in links:
	a.append(link.text)
print(a)
	
#for link in soup.find_all("a"):
#    links.append(link.get("href"))
#print(links)

# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
#with open("myLinks.txt", 'a') as saved:
    #print(links[:10], file=saved)
