import requests
from bs4 import BeautifulSoup

def emptyCheck(data):
    if len(data.strip()) == 0:
        print('No data available.')

url = "https://www.mahindrauniversity.edu.in/faculty/catherine-xavier"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent,'html.parser')
title = soup.title #<title>Om Prakash Patel | Mahindra University</title> # paras = soup.find_all('p') #gets all the paragraphs from the page with all the associated tags # print(soup.find('p')) prints the first paragraph/get the first element in html page #find_all gives all the paragraphs related to the tag
# get_text(strip=True) in the get text will put everything in one single line
description = soup.find('div', {'class': 'profile-details-block d-flex flex-column'}).get_text().strip() #name,profession,dept,email,phone
experience = soup.find('div',{'class':'faculty-tabs-content','id':'experience'}).get_text()
publications= soup.find('div',{'class':'faculty-tabs-content','id':'publications'}).get_text()
research = soup.find('div',{'class':'faculty-tabs-content','id':'research'}).get_text()
emptyCheck(description)
emptyCheck(experience)
emptyCheck(publications)
emptyCheck(research)
desclist = description.split('\n') #it is a list which has name, desgn, dept,email phone
""" for i in desclist:
    if(len(i) == 0):
        desclist.remove(i) 
         """

to_append = ([url, desclist[0], desclist[1], desclist[2], desclist[3],desclist[4]])
print(to_append)

for i in to_append:
    if(len(i) == 0):
        i = "NO Data"  

#desclist.pop(1) #removes the empty line bw name and designation

