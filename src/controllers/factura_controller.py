from src.app import app
from flask import render_template, request, redirect, url_for, jsonify
from flask_controller import FlaskController

from src.models.facturas import Facturas
from src.models.detalles_facturas import Detalles_Facturas


class FacturaController(FlaskController):
    @app.route('/crear_factura', methods=['GET', 'POST'])
    def crear_factura():

        if request.method == "POST":

            data = request.get_json()

            id_cliente = data.get('id_cliente')
            carrito = data.get('carrito')

            factura = Facturas(id_cliente, "pagado")
            Facturas.agregar_factura(factura)

            for item in carrito:
                detalle = Detalles_Facturas(factura.id, item['producto_id'], item['cantidad'], 0)

                Detalles_Facturas.agregar_detalle_factura(detalle)
            return jsonify(success=True, redirect_url=url_for('ver_facturas'))

        return render_template('facturar.html', title_page = 'SFI - Factura')
    
    @app.route('/ver_facturas')
    def ver_facturas():
        facturas = Facturas.obtener_facturas()
        
        return render_template('tabla_facturas.html', title_page = 'Ver facturas', facturas = facturas)