from bs4 import BeautifulSoup
import requests

source = "playlist.html"

with open(source) as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

print(soup.prettify())

match = soup.title.text
match

match = soup.findAll('div', class_='titles')

for i, title in enumerate(match):
  index = ''
  if len(str(i)) == 1:
    index += '0' + str(i) + "_"
  else:
    index += str(i) + "_"
  t = index +  title.text.strip()
  print(t)

with open('file_names.txt', 'w') as f:
  for i, title in enumerate(match):
    index = ''
    if len(str(i)) == 1:
      index += '0' + str(i) + "_"
    else:
      index += str(i) + "_"
    t = index +  title.text.strip() + '\n'
    f.writelines(t)

