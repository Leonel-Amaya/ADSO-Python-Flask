from sqlalchemy import Column, String, Integer, DateTime, update
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
    
    def obtener_proveedores():
        proveedores = session.query(Proveedores).all()
        return proveedores
    
    def eliminar_proveedor(id):
        proveedor = session.query(Proveedores).get(id)
        session.delete(proveedor)
        session.commit()
        return proveedor
    
    def editar_proveedor(proveedor):
        proveedor_id = proveedor.id
        session.execute(update(Proveedores).where(Proveedores.id == proveedor_id).values(nombre = proveedor.nombre,
                direccion = proveedor.direccion))
        session.commit()
        return proveedor