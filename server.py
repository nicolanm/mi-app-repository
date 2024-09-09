from flask import Flask, render_template, request, redirect

# Importamos la clase de mascota.py

from mascota import Mascota

app = Flask(__name__)
@app.route("/")
def agregar():
   # Invocamos al método de clase get all para obtener todas las mascotas
   return render_template("agregar.html")
@app.route("/registro")
def registro():
   # Invocamos al método de clase get all para obtener todas las mascotas
   mascotas = Mascota.get_all()
   print(mascotas)
   return render_template("registro.html", todas_mascotas = mascotas)

@app.route("/crear_mascota", methods=['POST'])
def crear_mascota():
   datos = {
       "nombre": request.form['nombre'],
       "tipo": request.form['tipo'],
       "color": request.form['color']
   }
   Mascota.save(datos)
   return redirect('/')

if __name__ == "__main__":
   app.run(debug=True)