import requests
from bs4 import BeautifulSoup as bs

github_user=input("Input Giithub Username:")
url="https://github.com/"+github_user
r=requests.get(url)
soup=bs(r.content,'html.parser')
profile_image=soup.find('img', class_='avatar-user')['src']
print(profile_image)