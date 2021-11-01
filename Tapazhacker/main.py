from bs4 import BeautifulSoup 
import requests 
page = requests.get("https://tap.az/elanlar/elektronika/telefonlar?utf8=%E2%9C%93&order=&q[user_id]=&q[contact_id]=&q[price][]=&q[price][]=&p[749]=3855&p[916]=&p[917]=&p[918]=&p[920]=&p[743]=true&p[853]=&q[region_id]=&keywords=")

soup = BeautifulSoup(page.content)
print(soup);
txt = soup;
file1 = open("myfile.html","wb")
file1.write(txt.encode('utf-8'))
file1.close()