import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.n11.com/arama?q=telefon")
kaynak = BeautifulSoup(r.content, "lxml")
aa = kaynak.find("ins")
g_data = kaynak.find_all("div", {"class": "info"})
for item in g_data:
    print (item.text)

for item in g_data:
    isim = print(item.contents[0].find_all("h3", {"class": "productName bold"})[0])
    fiyat = print(item.contents[1].find_all("input", {"class": "productDisplayPrice"})[1])
    print(isim , fiyat)