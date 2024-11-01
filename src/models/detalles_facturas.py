from sqlalchemy import Column, Integer, ForeignKey

class Detalles_Facturas():
    __tablename__ = 'detalles_facturas'
    id = Column(Integer, primary_key=True)
    factura = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    producto = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_total = Column(Integer, nullable=False)
