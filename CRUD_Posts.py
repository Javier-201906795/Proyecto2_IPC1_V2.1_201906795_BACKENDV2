# Importa metodo constructor 
from P_post import Post

#Nueva Clase
class CRUD_Post:
    # Constructor
    def __init__(self):
        #Simular base de datos (Array Vacio)
        self.posts = []
        self.postslikes = []
        self.newid = -1

    # CRUD => CREATE READ UPDATE DELETE

    # {A2 | VERIFICA ID  }
    def verifyid(self,id):
        #1.0 converir id a int para compar
        intid = int(id)
        #2.0 Buscar si el id existe
        for post in self.posts:
            #2.1 si existe 
            if post.id == intid:
                #2.2 retornar 
                return False
        #3.0 no se encontraron id iguales
        return True

    # {A1 | ENCONTRAR ID LIBRE }
    def idlibre(self,id):
        intid = int(id)
        #1.0 verificar si el id esta en uso
        idlibre = self.verifyid(id)
        print("id=>", id,"idlibre=>", idlibre)
        # Valida
        if idlibre == True:
            self.newid = intid
        else:
            self.idlibre(intid+1)
        return self.newid


    # { CREATE }
    def createpost(self, portada, tipo, descripcion, categoria, fecha, usuario,likes):
        # 1.0 Obtiene el id con el numero de elementos en el array 
        id = len(self.posts)
        # 1.1 Verificar si el id no esta en uso
        newid = self.idlibre(id)
        # 3.0 Crea Nuevo Post
        nuevopost = Post(newid,portada, tipo,descripcion, categoria,fecha,usuario,likes,0)
        # 4.0 Agrega el usaurio al listado 
        self.posts.append(nuevopost)
        # 5.0 IMPRIMIR usuario
        print("Nuevo Post: ",nuevopost.dump())
        # Actualizar ranking
        self.rankingorden()
        #6.0 Return mensaje
        return {'id': str(newid),'mensaje': "Post Creado exitosamente"}

    

    # { READ }
    def readpost(self, id):
        # Actualizar ranking
        self.rankingorden()
        # 1.0 convertir a int
        intid = int(id)
        print(id)
        print(intid)
        for post in self.posts:
            print(post.dump())
            if post.id == intid:
                print(post.dump())
                return  {'datacrud': post.dump(),'mensajecrud': "post encontrado"}
        return {'mensajecrud': "Post no encontrado"}


    # { READ ALL POSTS }
    def readposts(self):
        # Actualizar ranking
        self.rankingorden()
        #Arreglo
        arreglo_json = []
        #Almacena los json de los usuarios
        for post in self.posts:
            arreglo_json.append(post.dump())
        #envia todo en un json
        return arreglo_json


    # { READ POSTS USER }
    def readpostsuser(self, user):
        # Actualizar ranking
        self.rankingorden()
        #1.0 Arreglo con los Posts
        arreglo_json = []
        #2.0 Busca posts user
        for post in self.posts:
            if post.usuario == user:
                #2.1 agrega post encontrados
                arreglo_json.append(post.dump())
        #Return
        if arreglo_json == [] :
            return {'datacrud': arreglo_json,'mensajecrud': "No se encontraron post crados con este usuario"}
        return  {'datacrud': arreglo_json,'mensajecrud': "Post encontrados exitosamente"}


    # { EDIT POST }
    def editpost(self, idpost, portada, tipo, descripcion, categoria, fecha, usuario):
        #1.0 convertir id a int
        intid = int(idpost)
        #2.0 Buscar post
        for post in self.posts:
            #2.1 encontrar post 
            if post.id == intid:
                #2.2 actualizar informacion
                post.portada = portada
                post.tipo = tipo
                post.descripcion = descripcion
                post.categoria = categoria
                post.fecha = fecha
                post.usuario = usuario
                return {'datacrud': post.dump(),'mensajecrud': "Post Modificado con exito.", "codigo": 200}
        #3.0 no se encontro ningun post
        return {'datacrud': [],'mensajecrud': "No se encontro ningun Post con el id " + idpost, "codigo": 400}    

    # { DELETE POST }
    def deletepost(self, id):
        intid = int(id)
        #1.0 Busca el Post
        c=-1
        for post in self.posts:
            c += 1
            if post.id == intid:
                #1.2 Eliminar
                print("c=>",c)
                self.posts.pop(c)
                return {'mensajecrud': "Post eliminado correctamente", "codigo": 200}        
        return {'mensajecrud': "No se encontro el post a a elminar", "codigo": 400}    
    

    # { LIKE POST }
    def likepost(self,id):
        intid = int(id)
        #1.0 recorre arreglo
        for post in self.posts:
            #1.1 busca post
            if post.id == intid:
                #1.2 actualiza la infomracion
                print(post.likes)
                post.likes = int(post.likes) + 1
                # Actualizar ranking
                self.rankingorden()
                return {'mensajecrud': "Like agregadro exitosamente | Likes actuales: " + str(post.likes), "codigo": 200}    
        return {'mensajecrud': "No se encontro el post", "codigo": 400}    

    # {B1 OBTENR RANKING POR LIKE }
    def rankingorden(self):
        #1.0 llenar array 
        lengtharreglo = len(self.posts)
        arrayfiltro  = []
        #2.0 Busca posts user
        for post in self.posts:
            arrayfiltro.append(post)

        
        # { ORDENAMIENTO METODO BURBUJA }        
        #1.0 Ordenar por Like
        temp = 0
        #2.0 obtiene el largo del arreglo
        lengtharreglo = len(arrayfiltro)
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


    # {B2 FILTER LIKE }
    def filterlike(self):
        for post in self.posts:
            print("ID: ", post.id, " R: ",post.ranking," Like ",post.likes)
        
        #Ejecuta orden por likes
        self.rankingorden()
        
        
        print("///")
        for post in self.posts:
            print("ID: ", post.id, " R: ",post.ranking," Like ",post.likes)
        print("/// filtro")
        for post in self.postslikes:
            print("ID: ", post.id, " R: ",post.ranking," Like ",post.likes)

        #1.0 Arreglo con los Posts
        arreglo_json = []
        #2.0 Busca posts user
        for post in self.postslikes:
            arreglo_json.append(post.dump())

        return {'datacrud':arreglo_json,'mensajecrud': "Filtrado con exito", "codigo": 200}  



    # { CARGA MASIVA }
    def cargaMasiva(self, request):
        print("CRUD")
        arrayimagenes = request.json['images']
        arrayvideos = request.json['videos']
        # 1.0 Crea POSTS
        for datos1 in arrayimagenes:
            self.createpost(datos1['url'], "imagen", "Descripcion: Post Carga Masiva", datos1['category'], datos1['date'], "admin",0)
            
        # 1.0 Crea POSTS
        for datos2 in arrayvideos:
            self.createpost(datos2['url'], "video", "Descripcion: Post Carga Masiva", datos2['category'], datos2['date'], "admin",0)
        return "OK"


    # { REPORTE USUARIO }
    def reporteusers(self):
        print("hola")
        return "OK"


    # { TEST }
    def test(self):
        mensaje = "hola"
        return mensaje