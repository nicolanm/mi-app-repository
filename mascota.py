# Importamos la función que devolverá una instancia de una conexión

from mysqlconnection import connectToMySQL

# Creamos la clase basada en la tabla de mascotas

class Mascota:

   def __init__( self , data ):
       self.id = data['id']
       self.nombre = data['nombre']
       self.tipo = data['tipo']
       self.color = data['color']

   # Creamos un método de clase para consultar nuestra base de datos

   @classmethod
   def get_all(cls):
       query = "SELECT * FROM mascotas;"
       # Llamamos a función connectToMySQL con el esquema al que te diriges
       resultados = connectToMySQL('pet').query_db(query)
       # Creamos una lista vacía para agregar nuestras instancias de mascota
       mascotas = []
       # Iteramos sobre los resultados de la base de datos y crear instancias de mascota con cls
       for mascota in resultados:
           mascotas.append( cls(mascota) )
       return mascotas

   @classmethod
   def save(cls, datos):
       query = "INSERT INTO mascotas (nombre, tipo, color) VALUES (%(nombre)s, %(tipo)s, %(color)s);"
       return connectToMySQL('pet').query_db(query, datos)