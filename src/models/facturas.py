from sqlalchemy import Column, String, Integer, Time, ForeignKey
from src.models import session, Base

class Facturas(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    fecha = Column(Time, nullable=False)
    cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    estado = Column(String(10))

def __init__(self, fecha, cliente, estado):
    self.fecha = fecha
    self.cliente = cliente
    self.estado = estado