import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.moneycontrol.com/stocks/marketstats/gainerloser.php?optex=BSE&opttopic=topgainers&index=-1'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', attrs={'class': 'tbldata14 bdrtpg'})

#for row in table.findAll('tr'):
#    for cell in row.findAll('td'):
#        print cell.text

#for row in table.findAll('tr'):
#    for cell in row.findAll('td'):
#        print cell.text.replace('&nbsp;', '')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

print list_of_rows
