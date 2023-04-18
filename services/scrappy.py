import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/12.0'
}

senahmi_page = requests.get('https://www.senamhi.gob.pe/?p=pronostico-meteorologico', headers=headers)

soup = BeautifulSoup(senahmi_page.text, 'html.parser')

place = []
libertad_place = []
place_elements = soup.select('tr > td')

for place_element in place_elements:
    id = place_element.select('div > strong > span > a')[0].get('href')
    id = id[-4:]
    lugar = place_element.select('div > strong > span > a')[0].get_text().strip()
    items = place_element.find_all('div', class_='row m-3')

    for item in items:
        fecha = item.select('div')[0].get_text().strip()
        max = item.select('div > strong')[0].get_text().strip()
        min = item.select('div > strong')[1].get_text().strip()
        descripcion = item.select('div')[4].get_text().strip()

        place.append(
            {
                'id': id,
                'lugar': lugar,
                'fecha': fecha,
                'max': max,
                'min': min,
                'descripcion': descripcion
            }
        )

for dato in place:
    lugar_name = dato['lugar']
    if lugar_name[-11:] == 'LA LIBERTAD':
        libertad_place.append(dato)
