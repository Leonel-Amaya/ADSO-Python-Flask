from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from src.models import session, Base

class Facturas(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, nullable=False)
    cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    estado = Column(String(10))

    def __init__(self, cliente, estado):
        self.fecha = datetime.now()
        self.cliente = cliente
        self.estado = estado

    def agregar_factura(factura):
        factura = session.add(factura)
        session.commit()
        return factura