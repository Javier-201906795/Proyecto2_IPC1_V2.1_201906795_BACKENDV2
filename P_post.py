class Post:
    #Constructor
    def __init__(self, id, portada, tipo, descripcion, categoria, fecha, usuario,likes,ranking):
            self.id = id
            self.portada = portada
            self.tipo = tipo
            self.descripcion = descripcion
            self.categoria = categoria
            self.fecha = fecha
            self.usuario = usuario
            self.likes = likes
            self.ranking = ranking

    #Metodo transformador  a JSON
    def dump(self):
        return{
            'id': self.id,
            'portada': self.portada,
            'tipo': self.tipo,
            'descripcion': self.descripcion,
            'categoria': self.categoria,
            'fecha': self.fecha,
            'usuario': self.usuario,
            'likes': self.likes,
            'ranking': self.ranking
        }