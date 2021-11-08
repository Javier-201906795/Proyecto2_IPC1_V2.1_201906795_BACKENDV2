# Importa metodo constructor de usuarios
from P_usuario import User

#Nueva Clase
class CRUD_User:
    # Constructor
    def __init__(self):
        #Simular base de datos (Array Vacio)
        self.usuarios = []

    # CRUD => CREATE READ UPDATE DELETE

    # { CREATE }
    def createuser(self, correo, pwd, nombre, genero, usuario):
        #1.0 Validar nombre de usuario
        for usuariofor in self.usuarios:
            if usuariofor.usuario == usuario:
                return "Nombre de usuario ya esta en uso elija otro porfavor"
        
        #2.0 Obtiene el id con el numero de elementos en el array usuarios
        id = len(self.usuarios)
        #3.0 Crea Nuevo usuario
        nuevousuario = User(id, correo, pwd, nombre, genero, usuario)
        #4.0 Agrega el usaurio al listado 
        self.usuarios.append(nuevousuario)
        #5.0 IMPRIMIR usuario
        print("Nuevo usaurio: ",nuevousuario.dump())
        #6.0 Return mensaje
        return "Usuario creado exitosamente"

    # { READ }
    def readuser(self, id):
        iid = int(id)
        for usuario in self.usuarios:
            if usuario.id == iid:
                return usuario.dump()
        return "No se encontro el usuario"

    # { READ USERS }
    def readusers(self):
        #Arreglo
        usuarios_json = []
        #Almacena los json de los usuarios
        for usuario in self.usuarios:
            usuarios_json.append(usuario.dump())
        #envia todo en un json
        return usuarios_json


    # { LOGIN }
    def loginuser(self, correo, pwd):
        #1.0 Evaluar Datos
        for usuario in self.usuarios:
            #1.1 Evalua si es el correo o usaurio correcto (si existe en DB)
            if usuario.correo == correo or usuario.usuario == correo:
                #1.2 Evalua si la contraseña es correcta
                if  usuario.pwd == pwd:
                    print('Usuario ' + correo + " loggeado correctamente.")
                    #1.3 Return  con los datos del usuario 
                    return usuario.dump()
        return None


    # { UPDATE }
    def updateuser(self,id, correo, pwd, nombre, genero, usuario):
        #0.0 Convertir id a int
        intid = int(id)
        #1.0 Validar nombre de usuario
        if self.usuarios[intid].usuario != usuario:
            for usuariofor in self.usuarios:
                if usuariofor.usuario == usuario:
                    return {'mensaje': "Nombre de usuario ya esta en uso elija otro porfavor"}

        #2.0 Actualiza la informacion 
        #2.2 sobreescribie los datos
        self.usuarios[intid].nombre = nombre
        self.usuarios[intid].correo = correo
        self.usuarios[intid].pwd = pwd
        self.usuarios[intid].genero = genero
        self.usuarios[intid].usuario = usuario
        return  {
            'usuario':{
                'id': self.usuarios[intid].id,
                'correo': self.usuarios[intid].correo,
                'pwd': self.usuarios[intid].pwd,
                'nombre': self.usuarios[intid].nombre,
                'genero': self.usuarios[intid].genero,
                'usuario': self.usuarios[intid].usuario
            },
            'mensaje': "Usuario Actualizado"
        }
    

    # { DELETE USER }
    def deleteuser(self, id):
        intid = int(id)
        #1.0 Busca el Post
        c=-1
        for user in self.usuarios:
            c += 1
            if user.id == intid:
                if user.id == 0:
                    return {'mensajecrud': "No se puede eliminar el usaurio admin", "codigo": 200}        
                else:
                    #1.2 Eliminar
                    print("c=>",c)
                    self.usuarios.pop(c)
                    return {'mensajecrud': "Usuario eliminado correctamente", "codigo": 200}        
        return {'mensajecrud': "No se encontro el usuario a a elminar", "codigo": 400}    

    # { Carga masiva }
    def cargaMasiva(self, usuarios_cm):
        # 1.0 Crea usuarios con el array recivido
        for usuario in usuarios_cm:
            self.createusermasiva(usuario['email'],usuario['password'], usuario['name'], usuario['gender'], usuario['username'])
        return "OK"

    # { CREATE }
    def createusermasiva(self, correo, pwd, nombre, genero, usuario):
        #0.0 traduce genero
        if genero == "F" or genero == "f":
            genero = "mujer"
        else:
            genero = "hombre"

        #1.0 Validar nombre de usuario
        for usuariofor in self.usuarios:
            if usuariofor.usuario == usuario:
                return "Nombre de usuario ya esta en uso elija otro porfavor"
        
        #2.0 Obtiene el id con el numero de elementos en el array usuarios
        id = len(self.usuarios)
        #3.0 Crea Nuevo usuario
        nuevousuario = User(id, correo, pwd, nombre, genero, usuario)
        #4.0 Agrega el usaurio al listado 
        self.usuarios.append(nuevousuario)
        #5.0 IMPRIMIR usuario
        print("Nuevo usaurio: ",nuevousuario.dump())
        #6.0 Return mensaje
        return "Usuario creado exitosamente"


    #{ REPORTE USERS }
    def reporteusers(self):
        print("hola")
        return "OK"


    # {B1 OBTENR RANKING POR LIKE }
    def rankingorden(self):
        #1.0 llenar array 
        lengtharreglo = len(self.usuarios)
        arrayfiltro  = []
        for post in self.usuarios:
            arrayfiltro.append(post)
        
        # { ORDENAMIENTO METODO BURBUJA }        
        #1.0 Ordenar por Like
        temp = 0
        #2.1 reccorrre el array
        for h in range(lengtharreglo-1,0,-1):
            for i in range(h):
                #Valida si es mayor
                if int(arrayfiltro[i].likes) < int(arrayfiltro[i+1].likes):
                    temp = arrayfiltro[i]
                    arrayfiltro[i] =arrayfiltro[i+1]
                    arrayfiltro[i+1] = temp
        print("fin ordenamiento por metodo burbuja")

        #3.0 Guarda el rankgin
        lengtharreglo = len(arrayfiltro)
        for j in range(0,lengtharreglo,1):
            for k in range(0,lengtharreglo,1):
                if arrayfiltro[k].id == self.posts[j].id:
                    self.posts[j].ranking = k

        #4.0 guardar array
        self.postslikes = arrayfiltro

    # { TEST }
    def test(self):
        mensaje = "hola"
        return mensaje