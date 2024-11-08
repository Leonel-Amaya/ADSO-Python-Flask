from flask import Flask, render_template
from src.models import Base, engine
from src.models.categorias import Categorias
from src.models.productos import Productos
from src.models.clientes import Clientes
from src.models.facturas import Facturas
from src.models.detalles_facturas import Detalles_Facturas

app = Flask(__name__)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('principal.html', title_page = 'SFI - Home')

@app.route('/registrar-producto')
def crear_producto():
    return render_template('producto.html', title_page = 'SFI - Productos')

@app.route('/registrar-cliente')
def crear_cliente():
    return render_template('cliente.html', title_page = 'SFI - Cliente')

@app.route('/registrar-proveedor')
def crear_proveedor():
    return render_template('proveedor.html', title_page = 'SFI - Proveedor')

@app.route('/registrar-factura')
def crear_factura():
    return render_template('facturar.html', title_page = 'SFI - Factura')