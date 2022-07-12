from importlib_metadata import metadata
from app.db_sqlachemy import db_sqlalchemy
from app.models.producto import Producto
db= db_sqlalchemy
metadata=db.MetaData()

class Talle(db.Model):
    __tablename__ = 'talle'
    idTalle= db.Column(db.Integer,primary_key=True)
    talle = db.Column(db.String(20))
    cantidad = db.Column(db.Integer)
    producto_id=db.Column(db.Integer,db.ForeignKey('producto.idProducto'))

    def __init__(self, talle, cantidad,idProducto):
        self.talle=talle
        self.cantidad=cantidad
        self.producto_id=idProducto
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True
