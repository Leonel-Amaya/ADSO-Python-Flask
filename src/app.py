from flask import Flask, render_template, request, redirect, url_for
from src.models import Base, engine
from flask_controller import FlaskControllerRegister
from src.models.facturas import Facturas
from src.models.detalles_facturas import Detalles_Facturas
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)
