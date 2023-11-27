from flask import Flask, render_template, request, flash, url_for


app = Flask(__name__)

app.config['SECRET_KEY'] = "chave"


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/iniciar', methods=['POST', 'GET'])
def iniciar():
    url = request.form['url']
    return render_template('inicio.html', url=url)

if __name__ == "__main__":
    app.run(debug=True)