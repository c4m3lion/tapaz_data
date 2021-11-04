webUrl = "https://tap.az/elanlar/elektronika/telefonlar?utf8=%E2%9C%93&order=&q%5Buser_id%5D=&q%5Bcontact_id%5D=&q%5Bprice%5D%5B%5D=&q%5Bprice%5D%5B%5D=&p%5B749%5D=3855&p%5B916%5D=&p%5B917%5D=&p%5B918%5D=&p%5B920%5D=&p%5B743%5D=true&p%5B853%5D=&q%5Bregion_id%5D=&keywords=";
# Import Required Modules
#from sys import last_type
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import json
import tapBot
import time
lastPassed = False;
veryFirstTime = True;
lastPost = {}
def process():
    global veryFirstTime;
    global lastPost;
    global lastPassed
    #driver = webdriver.Chrome()
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get(webUrl);
    
    productsList = {}
    sectionContainer = driver.find_element(By.CSS_SELECTOR , 'div.js-endless-container');
    products = sectionContainer.find_elements(By.CSS_SELECTOR, 'div.products-i')
    i=0;
    
    for product in products:
        imgClass = product.find_element(By.CSS_SELECTOR, 'img');
        imgLink = imgClass.get_attribute("src")
        name = product.find_element(By.CSS_SELECTOR,'div.products-name').text
        price = product.find_element(By.CSS_SELECTOR,'span.price-val').text
        timeCreated = product.find_element(By.CSS_SELECTOR,'div.products-created').text
        linkTo = product.find_element(By.CSS_SELECTOR, 'a.products-link').get_attribute('href');
        intPrice = int(price.replace(' ',''));
        productsList[i] = {'name': name,
                        'img': imgLink,
                        'price': intPrice,
                        'time': timeCreated,
                        'link': linkTo}
        i+=1;
    for section in reversed(productsList):
        sec = productsList[section];
        if(veryFirstTime):
            lastPost = sec;
            tapBot.sendMessage(sec);

        if(veryFirstTime == False):
            if(lastPost['link'] == sec['link']):
                lastPassed = True;
            elif(lastPassed):
                lastPost = sec;
                tapBot.sendMessage(sec);
    if(lastPassed==False and veryFirstTime==False):
        for section in reversed(productsList):
            sec = productsList[section];
            lastPost = sec;
            tapBot.sendMessage(sec);

    done();


def done():
    firstTimeRun = False;
    

while(1):
    process();
    time.sleep(2);