'''
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон.
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('clothes and costumes.html')

@app.route('/scarves/')
def scarves():
    return render_template('scarfs and scarves.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes and boots.html')






if __name__ =='__main__':
    app.run(debug=True)