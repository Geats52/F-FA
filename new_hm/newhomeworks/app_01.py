'''
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
'''

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def math_operation():
    if request.method == 'POST':
        number = request.form.get('first_num')
        res = int(number) ** 2 
        return str(res)
    return render_template('tsotn.html')

if __name__ == '__main__':
    app.run(debug=True)