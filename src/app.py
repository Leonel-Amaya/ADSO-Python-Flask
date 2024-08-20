from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('principal.html')

@app.route('/registrar-producto')
def crear_producto:
    return render_template('producto.html')

@app.route('/registrar-cliente')
def crear_cliente:
    return render_template('cliente.html')

@app.route('/registrar-proveedor')
def crear_proveedor:
    return render_template('proveedor.html')

@app.route('/registrar-factura')
def crear_factura:
    return render_template('facturar.html')