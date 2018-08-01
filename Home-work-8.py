import requests
import os
from sys import getdefaultencoding

def translate_it(text, lang_from = 'en', lang_on = "ru"):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20180728T094444Z.1cc4d3de679e8357.8410a6efb60c113c3688a53f086cd153f2fe8131'

    params = {
        'key': key,
        'lang': lang_from + "-" + lang_on,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))

def read_file(way):
    text = ""
    with open(way, encoding=getdefaultencoding()) as file:
        text = file.read()
    return text

def wright_file(text, way):
    with open(way, "w", encoding=getdefaultencoding()) as file:
        file.write(text)

current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.join(current_dir, "Translate")
for root, dirs, files in os.walk(current_dir):
    for filename in files:
        if filename.endswith(".txt") and not filename.startswith("translate_"):
            way_file = os.path.join(current_dir, filename)
            text = read_file(way_file)
            lang_from = filename[:2].lower()
            lang_on = "ru"
            text_translate = translate_it(text, lang_from, lang_on)
            filename = os.path.join(current_dir, "translate_" + filename)
            wright_file(text_translate, filename)