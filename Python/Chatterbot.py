from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Lire')

bot = ChatBot(
    'Lire',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
    
conversa = ListTrainer(bot)
conversa.train([
    'Oi',
    'Olá',
    'Tudo bem?',
    'Tudo e com você',
    'Estou bem',
    'Que ótimo, fico feliz!'
    'Qual o seu nome?',
    'Lire',
    'Prazer em te conhecer',
    'Prazer é meu',
    'O que você é?',
    'Sou um bot criado por você!'
])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Lire: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break