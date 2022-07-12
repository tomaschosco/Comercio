from importlib_metadata import metadata
from app.db_sqlachemy import db_sqlalchemy
from app.models.categoria import Categoria
db= db_sqlalchemy
metadata=db.MetaData()

class Producto(db.Model):
    __tablename__ = 'producto'
    idProducto= db.Column(db.Integer,primary_key=True)
    imagen = db.Column(db.String(200))
    nombre = db.Column(db.String(45))
    precio= db.Column(db.Float)
    enable=db.Column(db.Integer)
    descripcion=db.Column(db.String(45))
    categoria_id=db.Column(db.Integer, db.ForeignKey('categoria.idCategoria'))
    talles=db.relationship("Talle", backref="producto")
    def __init__(self, nombre, imagen, precio, descripcion,idCategoria):
        self.nombre=nombre
        self.imagen=imagen
        self.precio=precio
        self.enable=1
        self.descripcion=descripcion
        self.categoria_id=idCategoria
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True
    @staticmethod
    def all():
        return Producto.query.all()
    def habilitados():
        return Producto.query.filter_by(enable=1).all()
    def eliminar(id):
        producto=Producto.query.get(id)
        producto.enable=0 
        producto.save()
        return "eliminadooo"