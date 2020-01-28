
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Lire')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train(r'C:\Users\900159\Documents\GitHub\Machine_Learning\Python\Chatbot\portuguese\games.yml')


# bot = trainer(
# "Terminal",
# storage_adapter="chatterbot.storage.SQLStorageAdapter",
# logic_adapters=[
# "chatterbot.logic.MathematicalEvaluation",
# "chatterbot.logic.TimeLogicAdapter",
# "chatterbot.logic.BestMatch"
# ],

# input_adapter="chatterbot.input.TerminalAdapter",
# output_adapter="chatterbot.output.TerminalAdapter",
# database_uri="../database.db"
# )

while True:
    response = bot.get_response(input("Você: "))
    print("Lire: ", response)