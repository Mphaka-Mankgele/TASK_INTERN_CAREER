import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule, time

def get_product_links(pages):
    links = []
    for page in pages:
        url = f"https://www.incredible.co.za/products/cellphones-wearables/cellphones?{page}price=0-10000"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        product_list = soup.find_all("li", class_="item product product-item")
        for product in product_list:
            links.append(product.find("a", class_="product photo product-item-photo").get("href"))
    return links

def extract_product_data(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    product_name = soup.find("h1", class_="page-title").text.strip() if soup.find("h1", class_="page-title") else None
    try:
        normal_price = soup.find("span", class_="old-price").find("span", class_="price").text.strip()
        special_price = soup.find("span", class_="special-price").find("span", class_="price").text.strip()
    except AttributeError:
        normal_price = soup.find("span", class_="price").text.strip() if soup.find("span", class_="price") else None
        special_price = 0
    product_overview = soup.find("div", class_="product attribute overview").text.strip() if soup.find("div", class_="product attribute overview") else None
    return {"Name": product_name, "Price": normal_price, "Special Price": special_price, "Overview": product_overview}

def extract_data():
    pages = ["", "p=2&", "p=3&"]
    links = get_product_links(pages)
    product_data = [extract_product_data(link) for link in links]
    df = pd.DataFrame(product_data)
    print(df)

if __name__ == "__main__":
    schedule.every().wednesday.at("21:32").do(extract_data)
    while True:
        schedule.run_pending()
        time.sleep(1)