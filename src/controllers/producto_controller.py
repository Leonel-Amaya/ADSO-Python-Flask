from src.app import app
from flask import render_template, request, redirect, url_for, jsonify
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

            return redirect(url_for('ver_productos'))

        categorias = Categorias.obtener_categorias()

        return render_template('producto.html', title_page = 'SFI - Productos', categorias = categorias)
    
    @app.route('/ver_productos')
    def ver_productos():
        productos = Productos.obtener_productos()
        return render_template('tabla_productos.html', title_page = 'SFI - Productos', productos = productos)
    
    @app.route('/eliminar_producto/<id>')
    def eliminar_producto(id):
        Productos.eliminar_producto(id)
        productos = Productos.obtener_productos()
        return render_template('tabla_productos.html', title_page = 'SFI - Productos', productos = productos)
    
    
    @app.route('/editar_producto/<id>', methods=['POST', 'GET'])
    def editar_producto(id):
        
        producto = Productos.obtener_un_producto(id)

        if request.method == 'POST':

            producto_solo = Productos.obtener_producto_solo(id)

            producto_solo.descripcion = request.form.get('descripcion')
            producto_solo.valor_unitario = request.form.get('valor_unitario')
            producto_solo.cantidad_stock = request.form.get('cantidad_stock')
            
            Productos.editar_producto(producto_solo)

            return redirect(url_for('ver_productos'))
        
        return render_template('editar_producto.html', title_page = 'SFI - Productos', producto = producto)
    
    @app.route('/buscar_producto', methods = ['GET', 'POST'])
    def buscar_producto():
        termino_busqueda = request.args.get('query')
        productos = Productos.buscar_productos(termino_busqueda)

        for producto in productos:
            print(producto.descripcion)

        # resultados = [{'id': p.id, 'descripcion': p.descripcion, 'valor_unitario': p.valor_unitario} for p in productos]
        # return jsonify(resultados)
    
        return jsonify(success=True, productos=[{'id': p.id, 'nombre': p.descripcion, 'precio': p.valor_unitario} for p in productos])

