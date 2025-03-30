from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.proveedores import Proveedores

class ProveedorController(FlaskController):
    @app.route('/crear_proveedor', methods = ['POST', 'GET'])
    def crear_proveedor():

        if request.method == 'POST':

            nombre = request.form.get('nombre')
            nit = request.form.get('nit')
            direccion = request.form.get('direccion')

            proveedor = Proveedores(nombre, nit, direccion)
            Proveedores.agregar_proveedor(proveedor)

            return redirect(url_for('index'))
        
        return render_template('proveedor.html', title_page = 'SFI - Proveedor')
    
    @app.route('/ver_proveedores')
    def ver_proveedores():
        proveedores = Proveedores.obtener_proveedores()

        return render_template('tabla_proveedores.html', title_page = 'Ver proveedores', proveedores = proveedores)
    
    @app.route('/eliminar_proveedor/<id>')
    def eliminar_proveedor(id):
        print(id)
        Proveedores.eliminar_proveedor(id)
        proveedores = Proveedores.obtener_proveedores()
        return render_template('tabla_proveedores.html', title_page = 'Ver proveedores', proveedores = proveedores)