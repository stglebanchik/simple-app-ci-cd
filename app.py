from flask import Flask, request, render_template_string

app = Flask(__name__)

# Главная страница с простой HTML-разметкой
@app.route('/')
def home():
    return render_template_string('''
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>Мой Flask‑сайт</title>
      </head>
      <body>
        <h1>Добро пожаловать на мой сайт!</h1>
        <p>Это простой пример приложения на Flask внутри Docker.</p>
        <ul>
          <li><a href="/about">О приложении</a></li>
          <li><a href="/echo?msg=Привет!!!">Echo-параметр</a></li>
        </ul>
      </body>
    </html>
    ''')

# Страница «О приложении»
@app.route('/about')
def about():
    return render_template_string('''
    <!doctype html>
    <html>
      <head><meta charset="utf-8"><title>О приложении</title></head>
      <body>
        <h1>О приложении</h1>
        <p>Это демо‑приложение на Flask, упакованное в Docker.</p>
        <p><a href="/">← Назад на главную</a></p>
      </body>
    </html>
    ''')

# Пример получения параметра из URL: /echo?msg=ВашеСообщение
@app.route('/echo')
def echo():
    msg = request.args.get('msg', 'Параметр msg не передан')
    return render_template_string('''
    <!doctype html>
    <html>
      <head><meta charset="utf-8"><title>Echo</title></head>
      <body>
        <h1>Echo</h1>
        <p>Вы передали: <strong>{{ message }}</strong></p>
        <p><a href="/">← На главную</a></p>
      </body>
    </html>
    ''', message=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)