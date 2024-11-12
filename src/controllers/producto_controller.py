from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.categorias import Categorias

class ProductoController(FlaskController):
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

        categorias = Categorias.obtener_categorias()

        return render_template('producto.html', title_page = 'SFI - Productos', categorias = categorias)