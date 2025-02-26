from csv import excel
import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()

sheet = excel.active
sheet.title = 'MU Faculty Data'

sheet.append(['URL','Name', 'Profession', 'Department', 'Emil-Id And Phone Number','experience', 'publications', 'research'])


def emptyCheck(data):
    if len(data.strip()) == 0:
        print('No data available.')


all_url = [
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=0",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=1",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=2",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=3",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=4",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=5",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=6",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=7",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=8",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=9",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=10",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=11"
]
for url in all_url:
    page = requests.get(url)

    doc = BeautifulSoup(page.text,"html.parser")

    string = "https://www.mahindrauniversity.edu.in"
    for temp in  (doc.find_all("li",{ "class" : "specialisation-block col-lg-4 col-md-6 col-sm-12 col-12"})):
        link = temp.find("a")
        href = link.attrs['href']
        url = (string + href)
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')
        title = soup.title #<title>Om Prakash Patel | Mahindra University</title> # paras = soup.find_all('p') #gets all the paragraphs from the page with all the associated tags # print(soup.find('p')) prints the first paragraph/get the first element in html page #find_all gives all the paragraphs related to the tag
        # get_text(strip=True) in the get text will put everything in one single line
        description = soup.find('div', {'class': 'profile-details-block d-flex flex-column'}).get_text().strip() #name,profession,dept,email,phone
        experience = soup.find('div',{'class':'faculty-tabs-content','id':'experience'}).get_text()
        publications= soup.find('div',{'class':'faculty-tabs-content','id':'publications'}).get_text()
        research = soup.find('div',{'class':'faculty-tabs-content','id':'research'}).get_text()
        emptyCheck(description) #ensuring there is a description
        emptyCheck(experience) #ensuring there is a experience
        emptyCheck(publications) #ensuring there is a publications
        emptyCheck(research) #ensuring there is a research
        desclist = description.split('\n') #it is a list which has name, desgn, dept,email phone
        for i in desclist:
            if(len(i) == 0):
                desclist.remove(i) 
        sheet.append([url, desclist[0], desclist[1], desclist[2], desclist[3],experience,publications,research])

excel.save("MU_Chat_Faculty.xlsx")