from flask import render_template, request, redirect, url_for
from app.models.producto import Producto
from app import db

def home():
    productos = Producto.query.all()
    return render_template("index.html", productos=productos)

def agregar():
    if request.method == "POST":
        nuevo = Producto(
            nombre=request.form["nombre"],
            precio=float(request.form["precio"]),
            cantidad=int(request.form["cantidad"])
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("agregar.html")

def editar(id):
    producto = Producto.query.get_or_404(id)
    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.precio = float(request.form["precio"])
        producto.cantidad = int(request.form["cantidad"])
        db.session.commit()
    
        return redirect(url_for("main.home"))
    return render_template("editar.html", producto=producto)

def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for("main.home"))
