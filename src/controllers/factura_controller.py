from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController

from src.models.facturas import Facturas


class FacturaController(FlaskController):
    @app.route('/crear_factura', methods=['GET', 'POST'])
    def crear_factura():

        if request.method == "POST":
            id_cliente = request.form.get('id_cliente')

            factura = Facturas(id_cliente, "pagado")
            Facturas.agregar_factura(factura)

            return redirect(url_for('index'))

        return render_template('facturar.html', title_page = 'SFI - Factura')