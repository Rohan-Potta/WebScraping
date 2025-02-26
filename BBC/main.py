import openpyxl
from bs4 import BeautifulSoup
import requests

excel = openpyxl.Workbook()

sheet = excel.active
sheet.title = 'Chicken Traybake'

sheet.append(['URL','Recipe Name','Ingredient','Recipe'])

urls = ["https://www.bbcgoodfood.com/recipes/collection/cookie-recipes",
    #"https://www.bbcgoodfood.com/recipes/collection/family-meal-recipes",
    #"https://www.bbcgoodfood.com/recipes/collection/risotto-recipes",
]

for url in urls:

    main_page = requests.get(url)

    main_doc = BeautifulSoup(main_page.text,"html.parser")

    string = "https://www.bbcgoodfood.com"

    links = []
    for link in main_doc.find_all("a",{'class':'link d-block'}):
        links.append(string + link.get("href"))


    size = len(links)
    links.pop(size-1)

    for url in links:

        page = requests.get(url)

        doc = BeautifulSoup(page.text,"html.parser")

        recipe_name = doc.find('h1',{'class':'heading-1'}).get_text() #name of the dish

        ingredients = "" #ingredients for the dish
        for ingredient in doc.find_all('li',{'class':"pb-xxs pt-xxs list-item list-item--separator"}):
                ingredients = ingredients + (ingredient.get_text())


        recipe_steps = doc.find('div',{'class':'grouped-list'}).get_text()  #how to make the dish


        sheet.append([url,recipe_name,ingredients,recipe_steps])


excel.save("BBC_Recipe1.xlsx")

