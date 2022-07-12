from fileinput import filename
from flask import render_template, request
from app.models.producto import Producto
from app.db_sqlachemy import db_sqlalchemy
from app.models.talle import Talle
from flask import current_app
from werkzeug.utils import secure_filename
import os

def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['PNG','png','JPEG','jpeg','JPG','jpg'])
    list= filename.split(".")
    return  list[1] in ALLOWED_EXTENSIONS

def nuevo():
    #Tomar datos del formulario
    nombre= request.form['nombreProd']
    descripcion=request.form['descripcionProd']
    precio=float(request.form['precioProd'])
    talles= request.form.getlist('talles[]')
    stocks=request.form.getlist('stocks[]')
    #SUBIR IMAGEN A LA CARPETA
    file= request.files["uploadFile"]
    fileName= secure_filename(file.filename)
    file_path = os.path.join(
                "app/", current_app.config['UPLOAD_FOLDER'], fileName)
    file.save(file_path)
    # subiendo a la BD, el id de la categoria es a mano por el momento
    newProducto= Producto(nombre,fileName,precio,descripcion,1)
    newProducto.save()
    for i in range(0,len(stocks)):
        newTalle= Talle(talles[i],int(stocks[i]),newProducto.idProducto)
        newTalle.save()
    return 'ESTOY ACA'
def form():
    return render_template("formProduct.html")
def listado():
    productos= Producto.habilitados()
    return render_template("productos.html", productos=productos)
def editar(id):
    print(id)
    producto=Producto.query.get(id)
    form= request.form
    if request.method == "POST":
        #imprimirDatos(form,request.files["uploadFile"])
        comprobarDatos(form,id,producto,request.files["uploadFile"])
        return render_template("editar_Producto.html",producto=producto)
    else :
        return render_template("editar_Producto.html",producto=producto)
def eliminar(id):
    Producto.eliminar(id)
    productos= Producto.habilitados()
    return render_template("productos.html", productos=productos)
def comprobarDatos(formDatos,idProducto,producto,file):
    nombreForm= formDatos['nombreProd']
    descripcionForm=formDatos['descripcionProd']
    precioForm=float(formDatos['precioProd'])
    tallesNombreForm= formDatos.getlist('tallesNombres[]')
    tallesCantForm=formDatos.getlist('tallesCantidad[]')
    #Productos nuevos a Agregar
    talleNuevoNomForm=formDatos.getlist('tallesNombresNew[]')
    talleNuevoCantForm=formDatos.getlist('tallesCantidadNew[]')
    if(nombreForm!=producto.nombre):
        producto.nombre=nombreForm
    if(descripcionForm != producto.descripcion):
        producto.descripcion=descripcionForm
    if(precioForm != producto.precio):
        producto.precio=precioForm
    #foto del producto
    fileName= secure_filename(file.filename)
    if(fileName!=""):
        #eliminar de la carpeta uploads el anterior
        fileDelete=producto.imagen
        os.unlink(os.path.join("app/", current_app.config['UPLOAD_FOLDER'], fileDelete))
        #agrego el nuevo
        file_path = os.path.join(
                "app/", current_app.config['UPLOAD_FOLDER'], fileName)
        file.save(file_path)
        producto.imagen=fileName

    productoTalles= producto.talles
    for i in range(0, len(productoTalles)):
        talleActual=productoTalles[i]
        actualizar=False
        #tallenuevo=productoTallesNuevo[i]
        if(tallesNombreForm[i] ==""):
            #eliminar no tengo el dato asi que si el stock es 0 es borrado
            talleActual.cantidad=0
            actualizar=True
        ##comparo los valores
        else:
            if(talleActual.talle != tallesNombreForm[i]):
                talleActual.talle=tallesNombreForm[i]
                actualizar=True

            if(talleActual.cantidad != tallesCantForm[i]):
                talleActual.cantidad=tallesCantForm[i]
                actualizar=True
        if(actualizar):
            talleActual.save()
    for i in range(0,len(talleNuevoNomForm)):
        newTalle= Talle(talleNuevoNomForm[i],int(talleNuevoCantForm[i]),idProducto)
        newTalle.save()
    return ""