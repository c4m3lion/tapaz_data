webUrl = "https://tap.az/elanlar/elektronika/telefonlar?utf8=%E2%9C%93&order=&q%5Buser_id%5D=&q%5Bcontact_id%5D=&q%5Bprice%5D%5B%5D=&q%5Bprice%5D%5B%5D=&p%5B749%5D=3855&p%5B916%5D=&p%5B917%5D=&p%5B918%5D=&p%5B920%5D=&p%5B743%5D=true&p%5B853%5D=&q%5Bregion_id%5D=&keywords=";
# Import Required Modules
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import json

# HTML Code
html_content = requests.get(webUrl).content
driver = webdriver.Firefox()
driver.get(webUrl);
file1 = open("myfile.html","wb")
# Parse the html content
 
products = {}
section = driver.find_element(By.CSS_SELECTOR , 'div.js-endless-container');
products = section.find_elements(By.CSS_SELECTOR, 'div.products-i')
i=0;
for product in products:
    
    name = product.find_element(By.CSS_SELECTOR,'div.products-name').text
    price = product.find_element(By.CSS_SELECTOR,'span.price-val').text
    timeCreated = product.find_element(By.CSS_SELECTOR,'div.products-created').text

    products[i] = {'name': name,
                    'price': price,
                    'time': timeCreated}
    i+=1;

for section in products:
    print("------------------------------------");
    print(section['names']);
    print(section['prices']);
    print(section['time']);

with open('test.json', 'w') as fout:
    json.dump(products , fout)

with open(r"test.json", "r") as read_file:
    data = json.load(read_file)
#print(data)

file1.close()