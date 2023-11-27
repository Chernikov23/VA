import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import subprocess
import jokes as jk
import random
import requests 
from gpytranslate import SyncTranslator
from gigachat import GigaChat
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser
import osascript
from urllib.parse import quote

r = sr.Recognizer()
language = "ru"
slow = 2

credentials = 'EnterYourApiKeyForGigaChat'


def speak(text):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")


def searchBrowser(query):
    encoded_query = quote(query, safe='')


    search_url = f"https://yandex.ru/search/?text={encoded_query}"

    webbrowser.open(search_url)


def translate():
    print('с какого языка?')
    speak('С какого языка?')
    with sr.Microphone() as source:
        print('говорите...')
        audio1 = r.listen(source)
        query1 = r.recognize_google(audio1, language='ru-RU').lower()
    if query1 == 'английский':
        print('На какой язык')
        speak('На какой язык')
        with sr.Microphone() as source:
            print('говорите...')
            audio2 = r.listen(source)
            query2 = r.recognize_google(audio2, language='ru-RU').lower()
        if query2 == 'русский':
            print('Произнесите текст для перевода')
            speak('Произнесите текст для перевода')
            with sr.Microphone() as source:
                print('говорите...')
                audio3 = r.listen(source)
                query3 = r.recognize_google(audio3, language='ru-RU').lower()
            print(query3)
            t = SyncTranslator()
            translation = t.translate(text=query3, targetlang="ru")
            translation = translation.text
            print(f"Перевод: {translation}")
            speak(translation)
            with open('messages.txt', 'a') as mega:
                mega.write(f"Ответ: {translation}\n")
                mega.write('\n')
        elif query2 == 'испанский':
            print('Произнесите текст для перевода')
            speak('Произнесите текст для перевода')
            with sr.Microphone() as source:
                print('говорите...')
                audio3 = r.listen(source)
                query3 = r.recognize_google(audio3, language='ru-RU').lower()
            print(query3)
            t = SyncTranslator()
            translation = t.translate(text=query3, targetlang="es")
            translation = translation.text
            print(f"Перевод: {translation}")
            speak(translation)
            with open('messages.txt', 'a') as mega:
                mega.write(f"Ответ: {translation}\n")
                mega.write('\n')

    elif query1 == 'русский':
        print('На какой язык')
        speak('На какой язык')
        with sr.Microphone() as source:
            print('говорите...')
            audio2 = r.listen(source)
            query2 = r.recognize_google(audio2, language='ru-RU').lower()
        if query2 == 'английский':
            print('Произнесите текст для перевода')
            speak('Произнесите текст для перевода')
            with sr.Microphone() as source:
                print('говорите...')
                audio3 = r.listen(source)
                query3 = r.recognize_google(audio3, language='ru-RU').lower()
            print(query3)
            t = SyncTranslator()
            translation = t.translate(text=query3, targetlang="en")
            translation = translation.text
            print(f"Перевод: {translation}")
            speak(translation)
        elif query2 == 'испанский':
            print('Произнесите текст для перевода')
            speak('Произнесите текст для перевода')
            with sr.Microphone() as source:
                print('говорите...')
                audio3 = r.listen(source)
                query3 = r.recognize_google(audio3, language='ru-RU').lower()
            print(query3)
            t = SyncTranslator()
            translation = t.translate(text=query3, targetlang="es")
            translation = translation.text
            print(f"Перевод: {translation}")
            speak(translation)
    elif query1 == 'испанский':
        print('На какой язык')
        speak('На какой язык')
        with sr.Microphone() as source:
            print('говорите...')
            audio2 = r.listen(source)
            query2 = r.recognize_google(audio2, language='ru-RU').lower()
        if query2 == 'английский':
            print('Произнесите текст для перевода')
            speak('Произнесите текст для перевода')
            with sr.Microphone() as source:
                print('говорите...')
                audio3 = r.listen(source)
                query3 = r.recognize_google(audio3, language='ru-RU').lower()
            print(query3)
            t = SyncTranslator()
            translation = t.translate(text=query3, targetlang="en")
            translation = translation.text
            print(f"Перевод: {translation}")
            speak(translation)
        elif query2 == 'русский':
            print('Произнесите текст для перевода')
            speak('Произнесите текст для перевода')
            with sr.Microphone() as source:
                print('говорите...')
                audio3 = r.listen(source)
                query3 = r.recognize_google(audio3, language='ru-RU').lower()
            print(query3)
            t = SyncTranslator()
            translation = t.translate(text=query3, targetlang="ru")
            translation = translation.text
            print(f"Перевод: {translation}")
            speak(translation)


def nowTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Текущее время: ", current_time)
    speak("Текущее время: " + current_time)


def play_music():
    osascript.run('tell application "Safari" to activate')
    time.sleep(2)

    webbrowser.get("safari").open("https://music.yandex.ru/home")
    time.sleep(2)
    osascript.run('tell application "System Events" to keystroke "Мне нравится" & return')
    osascript.run('tell application "System Events" to key code 76')


def weather():
    url = 'https://pogoda.mail.ru/prognoz/sankt_peterburg/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temp = soup.find("div", class_="information__content__temperature")
        feels = soup.find("div", class_='information__content__additional__item')
        if temp is not None:
            temp = temp.text.strip()
            print(temp)
        else:
            print("Не удалось найти температуру на странице")
        if feels is not None:
            feels = feels.text.strip()
            print(feels)
    else:
        print("Не удалось подключиться к сайту")
    speak(temp + feels)


def OpenYoutube(url):
    subprocess.Popen(['open', '-a', 'Safari', url])


def jokes():
    if 'расскажи анекдот' in query:
        joke = jk.nice
        print(joke)
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: {joke} \n")
            mega.write('\n')
        speak(joke)

    elif 'расскажи пошлую шутку' in query:
        joke = jk.bad
        print(joke)
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: {joke} \n")
            mega.write('\n')
        speak(joke)
    elif 'расскажи шутку про негров' in query:
        joke = random.choice(jk.negr)
        print(joke)
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: {joke} \n")
            mega.write('\n')
        speak(joke)


def openApp():
    if query == 'открой заметки':
        subprocess.Popen(['open', '-a', 'Notes'])
        print('Открываю')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Открываю \n")
            mega.write('\n')
        speak('Открываю')
    elif query == 'открой финдер':
        subprocess.Popen(['open', '-a', 'Finder'])
        print('Открываю')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Открываю \n")
            mega.write('\n')
        speak('Открываю')
    elif query == 'открой пайчарм':
        subprocess.Popen(['open', '-a', 'PyCharm CE'])
        print('Открываю')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Открываю \n")
            mega.write('\n')
        speak('Открываю')
    elif 'открой telegram' in query:
        subprocess.Popen(['open', '-a', 'Telegram'])
        print('Открываю')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Открываю \n")
            mega.write('\n')
        speak('Открываю')
    elif query == 'открой сафари':
        subprocess.Popen(['open', '-a', 'Safari'])
        print('Открываю')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Открываю \n")
            mega.write('\n')
        speak('Открываю')


def set_timer(query):
    count = 0
    if '10 секунд' in query:
        timer = 10
        print('Таймер установлен на 10 секунд')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Таймер установлен на 10 секунд \n")
            mega.write('\n')
        speak('Таймер установлен на 10 секунд')
    elif '1 минуту' in query or 'одну минуту' in query:
        timer = 60
        print('Таймер установлен на 1 минуту')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Таймер установлен на 1 минуту \n")
            mega.write('\n')
        speak('Таймер установлен на одну минуту')
    elif query == 'поставь таймер на 30 секунд' or query == 'поставь таймер на полминуты':
        timer = 30
        print('Таймер установлен на 30 секунд')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Таймер установлен на 30 секунд \n")
            mega.write('\n')
        speak('Таймер установлен на 30 секунд')
    elif query == 'поставь таймер на полторы минуты':
        timer = 90
        print('Таймер установлен на полторы минуты')
        with open('messages.txt', 'a') as mega:
            mega.write(f"Ответ: Таймер установлен на полторы минуты \n")
            mega.write('\n')
        speak('Таймер установлен на полторы минуты')
    else:
        return

    while count < timer:
        count += 1
        print(timer - count)
        time.sleep(1)
    print('Время истекло')
    with open('messages.txt', 'a') as mega:
        mega.write(f"Ответ: Время истекло \n")
        mega.write('\n')
    speak('Время истекло')
    playsound('timer.mp3')


while True:
    with sr.Microphone() as source:
        print('говорите...')
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='ru-RU').lower()
        with open('messages.txt', 'a') as file:
            file.write(f"Вы сказали: {query} \n")
            file.write('\n')
            print('ваш запрос: ' + query)

        if any(keyword in query for keyword in ('установи таймер на', 'таймер на', 'set timer')):
            set_timer(query)
        elif query == 'открой youtube':
            print('Открываю')
            with open('messages.txt', 'a') as mega:
                mega.write(f"Ответ: Открываю \n")
                mega.write('\n')
            speak('Открываю')
            OpenYoutube('https://www.youtube.com')
        elif query == 'открой заметки' or query == 'открой финдер' or 'открой telegram' in query or query == ('открой '
                                                                                                              'пайчарм') or query == 'открой сафари':
            openApp()
        elif 'расскажи андекдот' in query or 'расскажи пошлую шутку' in query or 'расскажи пошлый анекдот' in query or 'расскажи шутку про негров' in query:
            jokes()
        elif query == 'погода сейчас' or query == 'какая сейчас погода':
            weather()
        elif query == 'включи музыку':
            print('Включаю музыку')
            speak('Включаю музыку')
            play_music()
            break
        elif query == 'поиск в браузере':
            print('Что вы хотите найти?')
            speak('Что вы хотите найти?')
            with sr.Microphone() as source:
                print('говорите...')
                audio = r.listen(source)
                query = r.recognize_google(audio, language='ru-RU').lower()
            searchBrowser(query)
        elif query == 'время' or query == 'время сейчас' or query == 'сколько сейчас времени':
            nowTime()
        elif query == 'переведи текст':
            translate()
        elif query == 'стоп машина' or query == 'конец' or query == 'заканчивай':
            print('Конечно, хозяин')
            with open('messages.txt', 'a') as mega:
                mega.write(f"Ответ: Конечно, хозяин \n")
                mega.write('\n')
            speak('Конечно, хозяин')
            break
        else:
            with GigaChat(credentials=credentials, verify_ssl_certs=False) as giga:
                response = giga.chat(query)
                print(response.choices[0].message.content)

                speak(response.choices[0].message.content)
                with open('messages.txt', 'a') as mega:
                    mega.write(f"Ответ: {response.choices[0].message.content}")
                    mega.write('\n')

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass

