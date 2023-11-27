import webbrowser
from urllib.parse import quote
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


def usd():
    url = 'https://finance.rambler.ru/currencies/USD/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        doll = soup.find("div", class_="finance-currency-plate__currency")
        if doll is not None:
            doll = doll.text.strip()
            doll = doll.replace('.', ' целых ')
            dell = doll.replace(' целых ', ',')
            print('Курс доллара сейчас: '+dell+'₽')
            speak('Курс доллара сейчас: '+dell+'₽')
