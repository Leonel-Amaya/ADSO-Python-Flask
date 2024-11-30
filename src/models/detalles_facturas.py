from sqlalchemy import Column, Integer, ForeignKey
from src.models import session, Base

class Detalles_Facturas(Base):
    __tablename__ = 'detalles_facturas'
    id = Column(Integer, primary_key=True)
    factura = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    producto = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_total = Column(Integer, nullable=False)

    def __init__(self, factura, producto, cantidad, precio_total):
        self.factura = factura
        self.producto = producto
        self.cantidad = cantidad
        self.precio_total = precio_total

    def agregar_detalle_factura(detalle):
        detalle = session.add(detalle)
        session.commit()
        return detalle