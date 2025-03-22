from flask_restful import Resource
from flask import request
from flask_cors import cross_origin

from src.models.productos import Productos
from src.models.categorias import Categorias

class ProductosApi(Resource):
    @cross_origin()
    def post(self):
        print(request.json)
        producto = Productos(descripcion = request.json["descripcion"], 
                             valor_unitario = request.json["valor_unitario"], 
                             unidad_medida = request.json["unidad_medida"], 
                             cantidad_stock = request.json["cantidad_stock"], 
                             categoria = request.json["categoria"])
        Productos.agregar_producto(producto)
        return "producto guardado"