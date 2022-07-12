from importlib_metadata import metadata
from app.db_sqlachemy import db_sqlalchemy
db= db_sqlalchemy
metadata=db.MetaData()

class Categoria(db.Model):
    __tablename__ = 'categoria'
    idCategoria= db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100))
    productos=db.relationship("Producto", backref="categoria")

    def __init__(self, nombre):
        self.nombre=nombre
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True