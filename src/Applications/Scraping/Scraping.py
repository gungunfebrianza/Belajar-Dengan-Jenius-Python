import requests
from bs4 import BeautifulSoup as BS

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)  # Read Status Code
# print(page.content)
soup = BS(page.content, 'html.parser')
# print(soup.prettify())
# print(list(soup.children))
html = list(soup.children)[2]
print(html)
print("---- List HTML Child")
print(list(html.children))
print("---- List Body")
body = list(html.children)[3]
print(body)
print("---- List Body Child")
print(list(body.children))
p = list(body.children)[1]
print("---- Paragraph Child")
print(p.get_text())

print(soup.find_all('p'))
soup.find_all('p')[0].get_text()
