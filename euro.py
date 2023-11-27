import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from playsound import playsound
import os


def speak(text):
    tts = gTTS(text=text, lang='ru', slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")


def evro():
    url = 'https://finance.rambler.ru/currencies/EUR/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        eu = soup.find("div", class_="finance-currency-plate__currency")
        if eu is not None:
            eu = eu.text.strip()
            eu = eu.replace('.', ' целых ')
            eeu = eu.replace(' целых ', ',')
            print('Курс евро сейчас: '+eeu+'₽')
            speak('Курс евро сейчас: '+eeu+'₽')
