from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController

class FacturaController(FlaskController):
    @app.route('/registrar-factura')
    def crear_factura():
        return render_template('facturar.html', title_page = 'SFI - Factura')