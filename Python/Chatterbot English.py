# -*- coding: utf-8 -*-

#----- importing libraries -----#
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#----- Instantiating Chatbot named Lire -----#
bot = ChatBot('Lire')

#----- Instantiating training to the bot -----#
trainer = ChatterBotCorpusTrainer(bot)

#----- setting conversation to the bot -----#
trainer.train(
    "chatterbot.corpus.english"
)

#----- progress looping -----#
while True:
    response = bot.get_response(input("Você: "))
    print("Lire: ", response)

    #----- Defining condition based on degree of confidence -----#
    # try:
    #     response = bot.get_response(input("Você: "))
    #     if float(response.confidence) > 0.1:
    #         print("Lire: ", response)
    #     else:
    #         print("Eu não entendi :(")
    # except(KeyboardInterrupt, EOFError, SystemExit):
    #     break
    