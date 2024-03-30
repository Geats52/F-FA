from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/')
def index():
    # устанавливаем cookie
    response = make_response("Cookie")
    response.set_cookie('name', 'mail')
    return response

@app.route('/getcookie/')
def get_cookies():
    # получаем значение cookie
    name = request.cookies.get('name')
    return f"Значение cookie: {name}"

if __name__ =='__main__':
    app.run(debug=True)