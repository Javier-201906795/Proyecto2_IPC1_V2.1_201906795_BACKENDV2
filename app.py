#Importaciones Librerias
from logging import debug
from flask import Flask, json, request, jsonify
from flask_cors import CORS
#Importaciones Backend
from CRUD_Users import CRUD_User
from CRUD_Posts import CRUD_Post



# Inicializar servidor flask
app = Flask(__name__)
CORS(app)

# Inicializar Archivos Backend
crud_users = CRUD_User()
crud_posts = CRUD_Post()

# { CREAR USUARIO }
@app.route('/crateuser', methods=['PUT'])
def newuser():
    # Recivir del Frontend
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    nombre = request.json["nombre"]
    genero = request.json["genero"]
    usuario = request.json["usuario"]
    #Respuesta del CRUD
    respuesta = crud_users.createuser(correo, pwd, nombre, genero, usuario)
    #return
    return jsonify({"data": respuesta, "mensaje": "Ok"}), 200

# { LEER USUARIOS }
@app.route("/allusers", methods=["GET"])
def allusers():
    #Peticion a CRUD usuarios
    users = crud_users.readusers()
    return jsonify({"data": users, "mensaje": "OK"}), 200

# { LEER USUARIOS2 }
@app.route("/allusers", methods=["PUT"])
def allusers2():
    #Peticion a CRUD usuarios
    users = crud_users.readusers()
    return jsonify({"data": users, "mensaje": "OK"}), 200



# { LEER USUARIO }
@app.route("/userdata", methods=["PUT"])
def userdata():
    #Frontend
    id = request.json["id"]
    #Peticion a CRUD usuarios
    users = crud_users.readuser(id)
    return jsonify({"data": users, "mensaje": "OK"}), 200


# { LOGIN USER }
@app.route('/login', methods=["POST"])
def login():
    # Revir frontend
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    # Validacion Backend
    respuestacrud = crud_users.loginuser(correo, pwd)
    #Retornar
    if respuestacrud:
        return jsonify({"data": respuestacrud, "mensaje": "OK"}),200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas"}),404

# { ACTUALIZAR USUARIO }
@app.route('/updateuser', methods=['PUT'])
def updateuser():
    # 1.0 Recivir del Frontend
    id = request.json['id']
    correo = request.json["correo"]
    pwd = request.json["pwd"]
    nombre = request.json["nombre"]
    genero = request.json["genero"]
    usuario = request.json["usuario"]
    # 2.0 Respuesta CRUD 
    respuestacruduser = crud_users.updateuser(id, correo, pwd, nombre, genero, usuario)
    return jsonify({"data": respuestacruduser, "mensaje": "Ok"}),200

# { Eliminar POST }
@app.route('/deleteuser', methods=['PUT'])
def deleteuser():
    #1.0 Frontend
    idpost = request.json['id']
    #2.0 Respuesta CRUD
    respuestacrud = crud_users.deleteuser(idpost)
    #Return
    return jsonify({"data":respuestacrud, "mensaje": "id: "+ idpost}),200


# { CREAR NUEVO POST }
@app.route('/createpost', methods=['PUT'])
def createpost():
    # 1.0 Recivir del Frontend 
    portada = request.json['portada']
    tipo = request.json['tipo']
    descripcion = request.json['descripcion']
    categoria = request.json['categoria']
    fecha = request.json['fecha']
    usuario = request.json['usuario']
    likes = request.json['likes']
    # 2.0 Respuesta CRUD
    respuestacrud = crud_posts.createpost(portada, tipo, descripcion, categoria, fecha, usuario, likes)
    return jsonify({"data": respuestacrud, "mensaje": "OK"}),200

# { LEER POST }
@app.route('/leerpost', methods=['PUT'])
def leerpost():
    # 1.0 Recivir del Frontend 
    id = request.json['id']
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.readpost(id)
    return jsonify({"data": respuestacrud}),200
    

# { LEER TODOS LOS POSTS }
@app.route('/allposts', methods=['GET'])
def leerposts():
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.readposts()
    return jsonify({"data": respuestacrud}),200

# { 2LEER TODOS LOS POSTS }
@app.route('/allposts', methods=['PUT'])
def leerpostsput():
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.readposts()
    return jsonify({"data": respuestacrud}),200


# { VER POSTS USUARIO}
@app.route('/postsuser', methods=['PUT'])
def postsuser():
    # 1.0 Fronted
    user = request.json['usuario']
    # Respuesta CRUD
    respuestacrud = crud_posts.readpostsuser(user)
    # Return
    return jsonify({"data":respuestacrud, "mensaje": user}),200


# { MODIFICAR POST }
@app.route('/editpost', methods=['PUT'])
def editpost():
    #1.0 Frontend
    idpost = request.json['id']
    portada = request.json['portada']
    tipo = request.json['tipo']
    descripcion = request.json['descripcion']
    categoria = request.json['categoria']
    fecha = request.json['fecha']
    usuario = request.json['usuario']
    #2.0 Respuesta CRUD
    respuestacrud = crud_posts.editpost(idpost, portada, tipo, descripcion, categoria, fecha, usuario)
    #Return
    return jsonify({"data":respuestacrud, "mensaje": "id: "+ idpost}),200

# { Eliminar POST }
@app.route('/deletepost', methods=['PUT'])
def deletepost():
    #1.0 Frontend
    idpost = request.json['id']
    #2.0 Respuesta CRUD
    respuestacrud = crud_posts.deletepost(idpost)
    #Return
    return jsonify({"data":respuestacrud, "mensaje": "id: "+ idpost}),200

# { LIKE POST }
@app.route('/likepost', methods=['PUT'])
def likepost():
    # 1.0 Recivir del Frontend 
    id = request.json['id']
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.likepost(id)
    return jsonify({"data":respuestacrud, "mensaje": "id: "+ id}),200






# { FILTRO POR LIKE }
@app.route('/filterlike', methods=['PUT'])
def filterlike2():
    usuario = request.json['usuario']
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.filterlike()
    return jsonify({"data":respuestacrud, "mensaje": "ok"}),200



# { Carga masiva }
@app.route('/carga-masiva/usuarios', methods=["POST"])
def cargaMasiva():
    # Parametros que nos envia el frontend
    print(request)
    #convierte a archivo json
    print("JSON")
    usuarios = request.json["usuarios"]
    print(usuarios)
    #CRUD
    respuestacrud = crud_users.cargaMasiva(usuarios)
    #Return
    if respuestacrud == "OK":
        return jsonify({"data": crud_users.readusers(), "mensaje": "OK"}), 200
    else:
        return jsonify({"mensaje": "Hubo un error en la carga masiva"}), 400


# { Carga masiva POSTS }
@app.route('/carga-masiva/posts', methods=["POST"])
def cargaMasivaPOSTS():
    # Parametros que nos envia el frontend
    print(request)

    
    #convierte a archivo json
    print("JSON")
    imagenes = request.json['images']
    print(imagenes)

    respuestacrud = crud_posts.cargaMasiva(request)
    # usuarios = request.json["usuarios"]
    # print(usuarios)
    # #CRUD
    # respuestacrud = crud_users.cargaMasiva(usuarios)
    # #Return
    # if respuestacrud == "OK":
    #     return jsonify({"data": crud_users.readusers(), "mensaje": "OK"}), 200
    # else:
    #     return jsonify({"mensaje": "Hubo un error en la carga masiva"}), 400
    return jsonify({"mensaje": "OK"}), 200




# { REPORTE POSTS }
@app.route('/reporteposts', methods=['PUT'])
def reporteposts():
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.filterlike()
    return jsonify({"data":respuestacrud, "mensaje": "ok"}),200


# { REPORTE USERS }
@app.route('/reporteusers', methods=['PUT'])
def reporteusers():
    # 2.0 Respuesta CRUD
    respuestacrud =  crud_posts.reporteusers()
    return jsonify({"data":respuestacrud, "mensaje": "ok"}),200


# Test
@app.route('/test', methods=['PUT'])
def test():
    id = request.json['id']
    respuestacrud = crud_posts.idlibre(id)
    #respuestacrud = id
    return jsonify({"mensaje": respuestacrud}),200




# Metodo Main
if __name__ == '__main__':
    

    #Agregar Usuario ADMIN
    correo = "admin@ipc1.com"
    pwd = "admin@ipc1"
    nombre = "Cesar Josue Reyes Diaz"
    genero = "hombre"
    usuario = "admin"
    #Respuesta del CRUD
    respuesta = crud_users.createuser(correo, pwd, nombre, genero, usuario)

    #Agregar Nuevo Post
    portada = "https://img.freepik.com/foto-gratis/hermoso-camino-madera-que-impresionantes-arboles-coloridos-bosque_181624-5840.jpg?size=626&ext=jpg"
    tipo = "imagen"
    descripcion = "es un post nuevo, creado automaticamente."
    categoria = "Paisajes"
    fecha = "2/11/2021"
    usuario = "admin"
    likes = "0"
    crud_posts.createpost(portada, tipo, descripcion, categoria, fecha, usuario,12)
    
    

    #Iniciar servidor en el puerto 4000
    app.run(debug=False, port=8080)
