from sqlalchemy import Column, Integer, String, Float, ForeignKey, update
from src.models import session, Base
from src.models.categorias import Categorias

class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key = True)
    descripcion = Column(String(300), unique = True, nullable = False)
    valor_unitario = Column(Float(10, 8))
    unidad_medida = Column(String(3), nullable = False)
    cantidad_stock = Column(Float(10, 8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)


    def __init__(self, descripcion, valor_unitario, unidad_medida, cantidad_stock, categoria):
        self.descripcion = descripcion
        self.valor_unitario = valor_unitario
        self.unidad_medida = unidad_medida
        self.cantidad_stock = cantidad_stock
        self.categoria = categoria

    def obtener_productos():
        productos = session.query(Productos, Categorias).join(Categorias, Productos.categoria == Categorias.id).all()
        return productos

    def agregar_producto(producto):
        producto = session.add(producto)
        session.commit()
        return producto
    
    def eliminar_producto(id):
        producto = session.query(Productos).get(id)
        session.delete(producto)
        session.commit()
        return producto
    
    def editar_producto(producto):
        producto_id = producto.id
        session.execute(update(Productos).where(Productos.id == producto_id).values(descripcion=producto.descripcion,
                valor_unitario=producto.valor_unitario,
                cantidad_stock=producto.cantidad_stock))
        session.commit()
    
    def obtener_un_producto(id):
        producto = session.query(Productos, Categorias).join(Categorias).filter(Productos.id == id).first()
        return producto
    
    def obtener_producto_solo(id):
        producto = session.query(Productos).get(id)
        return producto
    
    def buscar_productos(termino_busqueda):
        productos = session.query(Productos).filter(Productos.descripcion.ilike(f'%{termino_busqueda}%')).all()
        return productos