import requests
from bs4 import BeautifulSoup



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



links = []
for url in all_url:
    page = requests.get(url)

    doc = BeautifulSoup(page.text,"html.parser")

    string = "https://www.mahindrauniversity.edu.in"
    for temp in  (doc.find_all("li",{ "class" : "specialisation-block col-lg-4 col-md-6 col-sm-12 col-12"})):
        link = temp.find("a")
        href = link.attrs['href']
        #links.append(string + href)
        print(string + href)

#print(links)
