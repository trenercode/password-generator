from flask import Flask, render_template, request
# Flask             -> создаёт веб-приложение
# render_template   -> подключает HTML файл
# request           -> получает данные из формы HTML

import random
# библиотека для случайных значений

import string
# библиотека с готовыми символами:
# буквы, цифры, спецсимволы


app = Flask(__name__)
# создаём Flask приложение


@app.route("/", methods=["GET", "POST"])
# "/" -> главная страница сайта
# GET  -> когда пользователь просто открыл страницу
# POST -> когда пользователь отправил форму (нажал кнопку)

def index():
    # функция главной страницы

    password = ""
    # пока пароль пустой


    if request.method == "POST":
        # проверяем:
        # нажал ли пользователь кнопку "Сгенерировать"

        
        length = int(request.form["length"])
        # получаем число из HTML input
        #
        # request.form["length"]
        # ищет поле:
        # <input name="length">
        #
        # int() превращает текст в число


        symbols = string.ascii_letters + string.digits + string.punctuation
        # создаём набор символов:
        #
        # ascii_letters -> буквы
        # digits        -> цифры
        # punctuation   -> спецсимволы


        for i in range(length):
            # цикл повторится столько раз,
            # какую длину пароля ввёл пользователь


            password += random.choice(symbols)
            # random.choice(symbols)
            # берёт случайный символ
            #
            # password +=
            # добавляет символ к паролю


    return render_template("index.html", password=password)
    # открываем HTML страницу index.html
    #
    # password=password
    # передаём переменную password в HTML
    #
    # в HTML она будет доступна как:
    # {{ password }}


app.run(debug=True)
# запускаем локальный сервер
#
# debug=True
# режим разработки:
# если будет ошибка — Flask покажет её подробно