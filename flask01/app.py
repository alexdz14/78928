from flask import Flask

app = Flask(__name__)

@app.route('/saludar')
def hola_mundo():
    return "Hola mundo!"

@app.route('/despedir')
def adios_mundo():
    return '<h1 style="color:red;">Adios mundo!</h1>'

@app.route('/json')
def json():
    return '{"nombre":"John"}'


@app.route('/xml')
def xml():
    return '<nombre>John</nombre>'

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)
