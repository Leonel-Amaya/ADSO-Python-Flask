from sqlalchemy import Column, String, Integer, Time, ForeignKey

class Facturas():
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    fecha = Column(Time, nullable=False)
    cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    estado = Column(String(10))