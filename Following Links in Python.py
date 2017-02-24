import urllib.request as ur
from bs4 import BeautifulSoup
import ssl
url = input("Enter url: ")
# url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
# url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Taysia.html"
count = int(input("Enter count: "))
position = int(input("Enter position: "))

while count > 0:
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    taga = soup.find_all('a')
    url = taga[position - 1].get('href', None)
    result = taga[position - 1].string
    count = count - 1
print(result)