# -*- coding: utf-8 -*-

#----- importing libraries -----#
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#----- Instantiating Chatbot named Lire -----#
bot = ChatBot('Lire')

#----- Defining initial conversation list -----#
conversation = []
arquivo = open('C:/Users/Usuario/Documents/GitHub/Machine_Learning/Python/Chatbot/dialogo.txt','r', encoding='utf-8')
for i in arquivo:
    a = i.strip()
    conversation.append(a)

#----- Instantiating training to the bot -----#
trainer = ListTrainer(bot)

#----- setting conversation to the bot -----#
trainer.train(conversation)

#----- progress looping -----#
while True:
    response = bot.get_response(input("Você: "))
    print("Lire: ", response)
