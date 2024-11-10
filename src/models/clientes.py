from sqlalchemy import Column, Integer, String
from src.models import session, Base

class Clientes(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre =Column(String(50), nullable=False)
    direccion = Column(String(50))
    email = Column(String(100), nullable=False)
    telefono = Column(String(50), nullable=False)

    def __init__(self, nombre, direccion, email, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono

    def agregar_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente