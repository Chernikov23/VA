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


def ton():
    url = 'https://coinmarketcap.com/currencies/toncoin/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tan = soup.find("span", class_="sc-f70bb44c-0 jxpCgO base-text")
        if ton is not None:
            tan = tan.text.strip()
            tan = tan.replace('.', ' целых ')
            ten = tan.replace(' целых ', ',')
            print('Курс Toncoin сейчас: ', ten)
            speak('Курс Тон коин сейчас: ' + ten)


