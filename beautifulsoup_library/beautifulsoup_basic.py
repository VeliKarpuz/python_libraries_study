import requests
from bs4 import BeautifulSoup


udemy_url= "https://www.udemy.com/?utm=bf4fa0cac2c70663b23770d896db6ff5&track=1&pt=2"
udemy = requests.get(udemy_url)
udemy.status_code
udemy_home = udemy.content

soup = BeautifulSoup(udemy_home,"html.parser")
print(udemy_home)
