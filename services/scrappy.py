import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edge/12.0'
}

senahmi_page = requests.get('https://www.senamhi.gob.pe/?p=pronostico-meteorologico', headers=headers)

soup = BeautifulSoup(senahmi_page.text, 'html.parser')

place = []
libertad_place = []
list_1 = []
list_2 = []
place_elements = soup.select('tr > td')
places = soup.find_all('div', class_='row m-3')

# for place_element in place_elements:
#     id = place_element.select('div > strong > span > a')[0].get('href')
#     id = id[-4:]
#     lugar = place_element.select('div > strong > span > a')[0].get_text().strip()
#     items = place_element.find_all('div', class_='row m-3')
#
#     for item in items:
#         fecha = item.select('div')[0].get_text().strip()
#         max = item.select('div > strong')[0].get_text().strip()
#         min = item.select('div > strong')[1].get_text().strip()
#         descripcion = item.select('div')[4].get_text().strip()
#
#         place.append(
#             {
#                 'id': id,
#                 'lugar': lugar,
#                 'fecha': fecha,
#                 'max': max,
#                 'min': min,
#                 'descripcion': descripcion
#             }
#         )
for place_element in place_elements:
    id = place_element.select('div > strong > span > a')[0].get('href')
    id = id[-4:]
    lugar = place_element.select('div > strong > span > a')[0].get_text().strip()
    list_1.append(
        {
            'id': id,
            'lugar': lugar,
        }
    )

for value in places:
    fecha = value.select('div')[0].get_text().strip()
    max = value.select('div > strong')[0].get_text().strip() #1
    min = value.select('div > strong')[1].get_text().strip() #2
    descripcion = value.select('div')[4].get_text().strip()
    list_2.append(
        {
            'fecha': fecha,
            'max': max,
            'min': min,
            'descripcion': descripcion
        }
    )

new_lista = []
n = len(list_1)
m = len(list_2) // n

for i in range(n):
    for j in range(m):
        temp_dict = {}
        temp_dict["id"] = list_1[i]['id']
        temp_dict["lugar"] = list_1[i]['lugar']
        temp_dict["fecha"] = list_2[i*m+j]['fecha']
        temp_dict["max"] = list_2[i*m+j]['max']
        temp_dict["min"] = list_2[i*m+j]['min']
        temp_dict["descripcion"] = list_2[i*m+j]['descripcion']

        new_lista.append(temp_dict)

for dato in new_lista:
    lugar_name = dato['lugar']
    if (lugar_name.split('-')[1]).strip() == 'LA LIBERTAD':
        libertad_place.append(dato)
