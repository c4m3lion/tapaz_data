import telepot
from pprint import pprint
bot = telepot.Bot('2089847864:AAGYSe7eM-594Ht_kVqU48jjcwUliVZ5VSc')
chat_id = 1539723388

def sendMessage(data):
    bot.sendPhoto(chat_id, data['img'])
    allStr=data['name']+'\n'+str(data['price'])+'\n'+data['time']+'\n'+data['link'];
    bot.sendMessage(chat_id, allStr)

def getLastLink():
    response = bot.getUpdates()
    pprint(response)
getLastLink();