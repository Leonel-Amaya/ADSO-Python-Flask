from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.clientes import Clientes

class ClienteController(FlaskController):
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