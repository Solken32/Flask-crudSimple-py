from app.extensions import db

class Producto(db.Model):
    __tablename__ = "productos"

    id=db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)    