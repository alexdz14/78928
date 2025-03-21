from flask import Flask, render_template
from producto import Producto
from flask import request
from flask import Response
from flask import redirect, url_for 
app = Flask(__name__)

productos = [Producto("Computadora", 200), Producto("Impresora", 50)]


@app.route('/')
def index():
    # productos = [Producto("Computadora", 200), Producto("Impresora", 50)]
    return render_template('productos.html', productos=productos)

@app.route('/editar/<producto>/<precio>')
def editar(producto,precio):
    #recuperar el producto
        print(producto,precio)
        return render_template('editar.html', producto=producto, precio=precio)

@app.route('/guardar', methods=['POST'])
def guardar():
    n=request.form['nombre']
    p=request.form['precio']
    print(n,p)
    i = 0
    for e in productos:
        if e.nombre == n:
            productos[i] = Producto(n,p)
            print(f"{e.nombre} {e.precio}")
        i += 1
    return Response("guardado", headers={'Location': '/'}, status=302)

@app.route('/eliminar/<nombre>')
def eliminar(nombre):
    i = 0
    for e in productos:
        if e.nombre == nombre:
            productos.pop(i)
            print(f"{e.nombre} {e.precio}")
        i += 1
    return Response("eliminado", headers={'Location': '/'}, status=302)

@app.route('/crear', methods=['POST'])
def crear():
    n=request.form['nombre']
    p=request.form['precio']
    print(n,p)
    productos.append(Producto(n,p))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)