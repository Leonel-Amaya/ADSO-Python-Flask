from sqlalchemy import Column, Integer, String
from src.models import session, Base
from sqlalchemy_serializer import SerializerMixin

class Clientes(Base, SerializerMixin):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre =Column(String(50), nullable=False)
    dni = Column(String(20), nullable=False)
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

    def obtener_cliente_por_id(id):
        cliente = session.query(Clientes).get(id)
        return cliente.to_dict()
    
    def obtener_cliente_por_dni(dni):
        cliente = session.query(Clientes).filter(Clientes.dni == dni).first()
        return cliente.to_dict()