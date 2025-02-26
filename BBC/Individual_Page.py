import requests 
from bs4 import BeautifulSoup

url = "https://www.bbcgoodfood.com/recipes/rainbow-cookies"


page = requests.get(url)

doc = BeautifulSoup(page.text,"html.parser")

recipe_name = doc.find('h1',{'class':'heading-1'}).get_text() #name of the dish

ingredients = "" #ingredients for the dish
for ingredient in doc.find_all('li',{'class':"pb-xxs pt-xxs list-item list-item--separator"}):
        ingredients = ingredients + (ingredient.get_text())


recipe_steps = doc.find('div',{'class':'row recipe__instructions'}).get_text()  #how to make the dish


print(recipe_name)
#print(ingredients)
print(recipe_steps)
