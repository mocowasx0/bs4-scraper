from bs4 import BeautifulSoup
import requests

def parcePrice():
    url = "https://finance.yahoo.com/quote/FB?p=FB"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    price = soup.find('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"}).find('span').text
    return price

while True:
    print("current FB ticker price: " +str(parcePrice()))
