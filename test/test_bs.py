from bs4 import BeautifulSoup


soup = BeautifulSoup(open("test1.html"),"lxml")
# soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

