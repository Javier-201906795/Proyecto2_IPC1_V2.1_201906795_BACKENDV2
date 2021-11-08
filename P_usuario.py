class User:

    #Constructor
    def __init__(self, id, correo, pwd, nombre, genero, usuario):
            self.id = id
            self.correo = correo
            self.pwd = pwd
            self.nombre = nombre
            self.genero = genero
            self.usuario = usuario

    #Metodo transformador  a JSON
    def dump(self):
        return{
            'id': self.id,
            'correo': self.correo,
            'pwd': self.pwd,
            'nombre': self.nombre,
            'genero': self.genero,
            'usuario': self.usuario
        }