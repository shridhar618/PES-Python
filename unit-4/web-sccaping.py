
from urllib.request import urlopen
#Web scraping of static web page using BeautifulSoup
from bs4 import BeautifulSoup as bs

#specify the url containing the dataset
url = "https://tatamumbaimarathon.procam.in/results/race-results"

#pass the url to urlopen function and get the webpage
html = urlopen(url)
#content is writtened as file like a object that can be read and processed
type(html)

#construct a beautiful soup object using the html content
soup = bs(html, 'lxml')
#it interprets the html
#it takes the unprocessed html text and converts it into python objrects
#lxml refers to html parser
type(soup)


title=soup.title
print(title)
print(type(title))



text=soup.get_text()
print(text)
print(type(text))
print(soup.text)


soup.find_all('a')
all_links=soup.find_all('a')
for link in all_links:
    print(link.get('href'))
    
    
#extract tabular data
rows=soup.find_all('tr')
print(rows)
print("\n\n")
print(type(rows))


