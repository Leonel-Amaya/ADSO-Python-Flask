from flask import Flask, render_template, request, redirect, url_for
from src.models import Base, engine
from flask_controller import FlaskControllerRegister
from src.models.facturas import Facturas
from src.models.detalles_facturas import Detalles_Facturas

app = Flask(__name__)

Base.metadata.create_all(engine)

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

if __name__ == '__main__':
    app.run(debug=True)
