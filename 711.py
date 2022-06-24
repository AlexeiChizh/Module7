

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table',{'class':'mfd-table mfd-currency-table'})

rows = table.find_all('td')
rows = (i.text for i in rows)

e=[]
for i in rows:
	e += str(i).split()

x=[]
y=[]

for i in range(len(e) - 1, 3, -4):
    x.append(str(e[i - 2]))
    y.append(float(str(e[i - 1])))

print(x)
print(y)