"""
LIRE:
- Controle de windows por comando de voz
"""

# Importando bibliotecas
from datetime import datetime          # O módulo datetime fornece classes para manipular datas e horas
import subprocess                      # O módulo subprocesso permite gerar novos processos
                                       #              
import speech_recognition as sr        # O módulo speech_recognition contem o reconhecimento de fala 
                                       # com suporte para o Google Speech Recognition, etc.


# Obtendo audio atraves do microfone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga Algo!")
    audio = r.listen(source)

# reconhecimento de fala usando o Google Speech Recognition
Query = r.recognize_google(audio)
print(Query)


# Executa aplicativos com função de comando de voz
def get_app(Q):
    if Q == "horas":
        print(datetime.now())
    elif Q == "bloco de nota":
        subprocess.call(['Notepad.exe'])
    elif Q == "calculadora":
        subprocess.call(['calc.exe'])
    elif Q == "stikynot":
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":
        subprocess.call(['cmd.exe'])
    elif Q == "navegador":
        subprocess.call(['C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
    else:
        print("Desculpe ! Tente novamente...")
    return


# Chamando metodo com Recognition
get_app(Query)