import requests
from BeautifulSoup import BeautifulSoup


def myfun (arg):
    url = arg

    response = requests.get(url.strip())
#add .strip() to remove \n from begining and end
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find('table', attrs={'class': 'tbldata14 bdrtpg'})

    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        print list_of_cells



with open('cpu.txt') as f:
    for line in f:
	myfun(line);
	print 'helloooooooooo'

#save url in file without quotes, and between two consecutive lines don't leave a newline as a gap...
