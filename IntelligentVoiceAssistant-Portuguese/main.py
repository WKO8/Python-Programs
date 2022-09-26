# Importing libraries
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Ir às compras', "Limpar o quarto", "Gravar um vídeo", "Programar"]


def create_note():
    global recognizer

    speaker.say("O que você quer escrever na sua anotação?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language="pt-BR")
                note = note.lower()

                speaker.say("Escolha um nome para o arquivo!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio, language="pt-BR")
                filename = filename.lower()

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"Eu criei com sucesso a anotação {filename}.")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Eu não consegui entender você. Por favor, tente novamente!")
            speaker.runAndWait()



def add_todo():

    global recognizer

    speaker.say("O que você quer adicionar?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio, language="pt-BR")
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"Eu adicionei {item} na lista de tarefas!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("Eu não consegui entender você. Por favor tente novamente!")
            speaker.runAndWait()


def show_todos():

    speaker.say("Os itens na sua lista de tarefas são os seguintes:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("Olá. O que eu posso fazer por você?")
    speaker.runAndWait()


def quit():
    speaker.say("Até mais!")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio, language="pt-BR")
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()