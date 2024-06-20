import pandas as pd
import requests
from bs4 import BeautifulSoup

title = []
company = []
location = []

for pages in range(1,225):
    f = requests.get('https://internshala.com/internships/'+str(pages))
    soup = BeautifulSoup(f.text,features='html.parser')

    for i in soup.findAll("div",{"class":"company"}):
        title.append((i.find("h3",{"class":"job-internship-name"})).text)

    for j in soup.findAll("div",{"class":"company_and_premium"}):
        company.append((j.find("p",{"class":"company-name"})).text)

    for k in soup.findAll("div",{"class":"row-1-item locations"}):
        location.append((k.find("a")).text)

finaldf = pd.DataFrame(
    {'Job Title':title,
     'Company Name':company,
     'Location':location,})

print(finaldf)