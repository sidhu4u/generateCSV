from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.worldometers.info/geography/alphabetical-list-of-countries/"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

tbody = soup.find('tbody')
tr_tags = tbody.find_all('tr')

with open('CountrywithPopulation.csv', 'w', encoding='utf8', newline='') as file:
    thewriter = writer(file)
    header = ['Serial_Num', 'Country_Name', 'Population', 'Land_Area']
    thewriter.writerow(header)

    for tr in tr_tags:
        td_tags = tr.find_all('td')

        serialnum = td_tags[0].text
        country = td_tags[1].text
        population = td_tags[2].text
        landarea = td_tags[3].text

        countryInfo = [serialnum, country, population, landarea]
        thewriter.writerow(countryInfo)
