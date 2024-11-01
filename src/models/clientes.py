from sqlalchemy import Column, Integer, String

class Clientes():
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre =Column(String(50), nullable=False)
    direccion = Column(String(50))
    email = Column(String(100), nullable=False)
    telefono = Column(String(50), nullable=False)