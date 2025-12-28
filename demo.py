'''import requests as re
from bs4 import BeautifulSoup

url='https://www.tutorialsfreak.com/'
web=re.get(url)
'''
#print(web)
#print(web.content)
#print(web.url)
#print(web.status_code)

# Html parseing
#soup=BeautifulSoup(web.content,'html.parser')
#print(soup)
#print(soup.prettify())

#print(soup.title)
#print(soup.title.name)

#print(soup.p)
#print(soup.p.title)

#print(soup.body)
#print(soup.h1)

# Kind of object

# 1) Tag

'''tag=soup.p
print(tag)

tag=soup.h1
print(tag)

tag=soup.a
print(tag)'''

# 2) Navigablestring

'''nav=soup.p.string
print(nav)

nav=soup.a.string
print(nav)

nav=soup.h1.string
print(nav)

nav=soup.body.string
print(nav)'''

# 3)Beautifulsoup

'''f=soup.find('p')
print(f)

f=soup.find('h1')
print(f)

fa=soup.find_all('p')
print(fa)

fa=soup.find_all('a')
print(fa)

fa=soup.find_all('h1')
print(fa)'''

# Finding element in web page

# a) finding element by class

'''import requests as re
from bs4 import BeautifulSoup

url="https://www.tutorialsfreak.com/"
web=re.get(url)

#print(web.content)

soup=BeautifulSoup(web.content,"html.parser")
# print(soup.prettify())

extract=soup.find_all('p',class_="fw-400 fs-20 lh-30 label-color-2 mb-lg-5")
print(extract)

extract2=soup.find('button',class_='tf-button')
print(extract2)'''


# b) finding element by Id

'''
import requests as re
from bs4 import BeautifulSoup

url="https://www.tutorialsfreak.com/"
web=re.get(url)

soup=BeautifulSoup(web.content,"html.parser")

extracid=soup.find('div',id='__next')
#print(extracid)

extracid2=soup.find('script',id='__NEXT_DATA__')
print(extracid2)'''


# Extract text from tags in web pge..
'''import requests as re
from bs4 import BeautifulSoup

url="https://www.tutorialsfreak.com/"
web=re.get(url)

soup=BeautifulSoup(web.content,"html.parser")

t=soup.find('p',class_='fs-16 fw-400 lh-24 label-color-1 card-text')
#print(t)

for txt in t:
    print(txt.text)

tt=soup.find('h4',class_='fw-600 fs-36 label-color-14')
#print(tt)
for txt2 in tt:
    print(txt2.text)'''



# Extract link from tags
'''import requests as re
from bs4 import BeautifulSoup

url="https://www.tutorialsfreak.com/"
web=re.get(url)

soup=BeautifulSoup(web.content,"html.parser")

a=soup.find_all('a')
for i in a:
    print(i.get('href'))'''


import requests as re
from bs4 import BeautifulSoup

url="https://www.tutorialsfreak.com/"
web=re.get(url)

soup=BeautifulSoup(web.content,"html.parser")

'''
im=soup.find_all('img')
for i in im:
    print(i.get('src'))'''

im=soup.find_all('img')
for i in im:
    print(i.get('alt'))

