import requests
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/results.html/2023/drivers.html'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', {'class': 'resultsarchive-table'})
    
    rows = table.find_all('tr')
    
    driver_data = ""

    for row in rows[1:]: 
        columns = row.find_all('td')
        position = columns[1].text
        driver_name = " ".join(columns[2].stripped_strings)  
        team = columns[3].text
        nationality = columns[4].text
        points = columns[5].text
        
        driver_data += f'Pozycja: {position}, Kierowca: {driver_name.strip()}, Zespół: {team.strip()}, Narodowość: {nationality.strip()}, Punkty: {points.strip()}\n'
    
    print(driver_data)
else:
    print('Nie udało się pobrać strony.')

