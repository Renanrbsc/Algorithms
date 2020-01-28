# -*- coding: utf-8 -*-

#----- importing libraries -----#
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

#----- Instantiating Chatbot named Lire -----#
bot = ChatBot('Lire')

#----- Defining initial conversation list -----#
conversation = [
    'oi',
    'olá',
    'tudo bem?',
    'tudo e com você',
    'estou bem',
    'que otimo, fico feliz',
    'qual o seu nome?',
    'Lire',
    'prazer em te conhecer',
    'Prazer é meu',
    'o que você é?',
    'sou um bot criado por você!'
]

#----- Instantiating training to the bot -----#
trainer = ListTrainer(bot)

#----- setting conversation to the bot -----#
trainer.train(4)

#----- progress looping -----#
while True:
    #----- Defining condition based on degree of confidence -----#
    try:
        resposta = bot.get_response(input("Você: "))
        if float(resposta.confidence) > 0.5:
            print("Lire: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    