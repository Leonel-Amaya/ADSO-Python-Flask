from sqlalchemy import Column, String, Integer, DateTime
from src.models import session, Base
from datetime import datetime

class Proveedores(Base):
    __tablename__ = 'proveedores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    nit = Column(Integer, nullable=False)
    fecha_vinculacion = Column(DateTime)
    direccion = Column(String(100))

    def __init__(self, nombre, nit, direccion):
        self.nombre = nombre
        self.nit = nit
        self.fecha_vinculacion = datetime.now()
        self.direccion = direccion

    def agregar_proveedor(proveedor):
        proveedor = session.add(proveedor)
        session.commit()
        return proveedor