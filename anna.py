import requests 
from bs4 import BeautifulSoup as bs
import openpyxl

def gettin():
	cars = {}


	headers = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
	}


	resp = requests.get('https://auto.drom.ru/', headers=headers)

	page = bs(resp.text, 'html.parser')

	elems = page.find_all('a', {'data-ftid': 'bulls-list_bull'})

	for i in range(0, len(elems)):
		
		link = elems[i]['href']
		title = elems[i].find('span', {'data-ftid': 'bull_title'})
		price = elems[i].find('span', {'data-ftid': 'bull_price'})
		
		cars[i] = [link, title.text, price.text]
	return cars
		


# Создаем новый файл
workbook = openpyxl.Workbook()

# Выбираем активный лист
sheet = workbook.active

# Добавляем новую строку
for i in gettin().values():
	new_row = i
	sheet.append(new_row)

# Сохраняем изменения
workbook.save('example.xlsx')
# print(elems)

