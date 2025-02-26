from traceback import print_stack
import requests 
from bs4 import BeautifulSoup

links = []
url = "https://www.bbcgoodfood.com/recipes/collection/cookie-recipes"

page = requests.get(url)

doc = BeautifulSoup(page.text,"html.parser")


""" for temp in  (doc.find_all("a",{ "class" : "standard-card-new__article-title"})):
    link = temp.find("a")
    #href = link.attrs['href']
    print(link) """
string = "https://www.bbcgoodfood.com"



string = "https://www.bbcgoodfood.com"

links = []
for link in doc.find_all("a",{'class':'link d-block'}):
    print(string + link.get("href"))
    #links.append(string + link.get("href"))

""" 
size = len(links)
links.pop(size-1)
#print(links)  """