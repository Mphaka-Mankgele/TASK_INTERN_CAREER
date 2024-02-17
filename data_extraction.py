import requests
from bs4 import BeautifulSoup
import pandas as pd

links = []
pages = ["", "p=2&", "p=3&"]
for i in pages:
    url = f"https://www.incredible.co.za/products/cellphones-wearables/cellphones?{i}price=0-10000"
    response1 = requests.get(url)
    soup1 = BeautifulSoup(response1.content, "html.parser")

    product_list = soup1.find_all("li", class_="item product product-item")
    
    
    for product in product_list:
        links.append(product.find("a", class_="product photo product-item-photo").get("href"))
        
product_data = []

for link in links:
    response2 = requests.get(link)
    soup2 = BeautifulSoup(response2.content, "html.parser")
    
    try:
        product_name = soup2.find("h1", class_="page-title").text.replace('\n',"")
    except:
        product_name = None
        
    try:
        normal_price = soup2.find("span", class_="old-price").find("span", class_="price").text.replace('\n',"")
        special_price = soup2.find("span", class_="special-price").find("span", class_="price").text.replace('\n',"")
    except:
        normal_price = soup2.find("span", class_="price").text.replace('\n',"")
        special_price = None
    
    try:
        product_overview = soup2.find("div", class_="product attribute overview").text.replace('\n',"")
    except:
        product_overview = None
        
    phone = {"Name": product_name,
             "Price": normal_price,
             "Special Price": special_price,
             "Overview": product_overview}
    
    product_data.append(phone)

dataFrame = pd.DataFrame(product_data)
print(dataFrame)