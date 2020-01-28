import speech_recognition as sr

def reconhecer():
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)

        while True:
            audio = rec.listen(s)

            entrada = rec.recognize_google(audio, language="pt")
            return f"Voce disse: {entrada}"

print('Ouvindo...........')

while True:
        
    fala = reconhecer()
    print(fala)



