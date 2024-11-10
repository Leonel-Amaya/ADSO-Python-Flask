from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/crear_producto', methods=['POST','GET'])
def crear_producto():

    if request.method == 'POST':

        descripcion = request.form.get('descripcion')
        valor_unitario = request.form.get('valor_unitario')    
        unidad_medida = request.form.get('unidad_medida')    
        cantidad_stock = request.form.get('cantidad_stock')
        categoria = request.form.get('categoria')

        producto = Productos(descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria)
        Productos.agregar_producto(producto)

        return redirect(url_for('index'))
    
    return render_template('producto.html', title_page = 'SFI - Productos')

@app.route('/crear_cliente', methods = ['POST', 'GET'])
def crear_cliente():

    if request.method == 'POST':

        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        email = request.form.get('email')
        telefono = request.form.get('telefono')

        cliente = Clientes(nombre, direccion, email, telefono)
        Clientes.agregar_cliente(cliente)

        return redirect(url_for('index'))

    return render_template('cliente.html', title_page = 'SFI - Cliente')

@app.route('/registrar-proveedor')
def crear_proveedor():
    return render_template('proveedor.html', title_page = 'SFI - Proveedor')

@app.route('/registrar-factura')
def crear_factura():
    return render_template('facturar.html', title_page = 'SFI - Factura')