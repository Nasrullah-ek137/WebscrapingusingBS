import requests
from bs4 import BeautifulSoup

url="https://www.iplt20.com/"

web=requests.get(url)

#print(web)
#print(web.content)
#print(web.url)
#print(web.status_code)

soup= BeautifulSoup(web.content,"html.parser")
#print(soup.prettify())

#print(soup.title)
#print(soup.title.name)
#print(soup.a)
#print(soup.p)
#print(soup.h1)

# this is tag obj

'''tag=soup.p
print(tag)

# navigablestring obj
nav=soup.a.string
print(nav)

# beautifulsoup obj
bs=soup.body
print(bs)

bs1=soup.find('a')
print(bs1)

bs2=soup.find_all('a')
print(bs2)'''

# Finding element by Class and Id
# a) class
class_data=soup.find_all("h2",class_="ap-foot-head")
print(class_data)

# b) id
id_data=soup.find_all("header",id="header-main")
print(id_data)

# link web page
for i in soup.find_all("a"):
    print(i.get("href"))

# extracted image in web page
for im in soup.find_all("img"):
    print(im.get("src"))
