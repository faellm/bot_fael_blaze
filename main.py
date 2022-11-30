import requests
from time import sleep
from data import *

while True:
    
    url = 'https://blaze.com/api/roulette_games/recent'
    response = requests.get(url)
    
    r = response.json()
    
    ray = []
    
    for x in range(len(r)):
        
        val = r[x]['color']
        
        if val == 1:
            val = 'Vermelho'
            
        if val == 2:
            val = 'Preto'
            
        if val == 0:
            val = 'Branco'
            
        ray.append(val)
    
    
    print(ray)
    sleep(15)
    

    def resultado(num):
        token = '' # inserir token do botFather
        chat_id = '' #id do chat
        
        if num[0:4] == a2 :
            
            text = 'Green no Preto'
            print(text)
            
            import telebot
        
            bot = telebot.TeleBot(token)
        
            bot.send_message(chat_id, text)
            sleep(5)
            
            
        if num[0:3] == a1 :
            
            text = 'Entrada confirmado no Preto'
            print(text)

            import telebot
        
            bot = telebot.TeleBot(token)
        
            bot.send_message(chat_id, text)
            
            sleep(5)
            
        if num[0:3] == a3 :
            
            text = 'Entrada confirmado no Vermelho, mas com possibilidade de Branco'
            print(text)
            
            import telebot
        
            bot = telebot.TeleBot(token)
        
            bot.send_message(chat_id, text)
            
            
            sleep(5)
            
        if num[0:3] == a4 :
            
            text = 'possibilidade no Preto'
            print(text)
            
            import telebot
        
            
            bot = telebot.TeleBot(token)
        
            bot.send_message(chat_id, text)
            
            
           #adicionar mais tipos de analises 
        ''''
        if num[0:3] == a4 :
            
            text = 'possibilidade no Preto'
            print(text)
            
            import telebot
        
            
            bot = telebot.TeleBot(token)
        
            bot.send_message(chat_id, text)
            sleep(5)''''
    
    resultado(ray)
    
    
    sleep(5)
    
