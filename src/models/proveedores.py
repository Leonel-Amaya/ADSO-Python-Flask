from sqlalchemy import Column, String, Integer, Time
from src.models import session, Base

class Proveedores(Base):
    __tablename__ = 'proveedores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    nit = Column(Integer, nullable=False)
    fecha_vinculacion = Column(Time)
    direccion = Column(String(100))

    def __init__(self, nombre, nit, fecha_vinculacion, direccion):
        self.nombre = nombre
        self.nit = nit
        self.fecha_vinculacion = fecha_vinculacion
        self.direccion = direccion