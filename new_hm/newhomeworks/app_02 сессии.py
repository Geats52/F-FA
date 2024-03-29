'''
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.


'''
from flask import Flask, render_template, redirect, url_for, make_response, request, session

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('mail')
        if "@" in mail and (".ru" in mail or ".com" in mail) and not '@.'in mail:

            return render_template('greeting.html', n = name)
        else:
            return 'Недопустимый адрес эл. почты'           
    return render_template('base.html')

@app.route('/get', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        return redirect(url_for('user'))
    return render_template('greeting.html')


if __name__ =='__main__':
    app.run(debug=True)


#bak@mail.com