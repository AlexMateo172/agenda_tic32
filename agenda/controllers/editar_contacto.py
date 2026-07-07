import web
import sqlite3

render = web.template.render('views', base='layout')

class Editar_contacto:

    def obtenerContacto(self, id_contacto:int):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            row = cursor.fetchone()
            
            if row:
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                return contacto
            return None
        except Exception as error:
            print(f"ERROR Editar 100: {error.args}")
            return None
        finally:
            conn.close()

    def actualizarContacto(self, id_contacto:int, datos):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = """
                UPDATE contactos 
                SET nombre=?, primer_apellido=?, segundo_apellido=?, email=?, telefono=?
                WHERE id_contacto=?
            """
            cursor.execute(query, (datos.nombre, datos.primer_apellido, datos.segundo_apellido, datos.email, datos.telefono, id_contacto))
        except Exception as error:
            print(f"ERROR Editar 101: {error.args}")
        finally:
            conn.close()

    def GET(self, id_contacto):
        contacto = self.obtenerContacto(id_contacto)
        # Muestra el formulario con los datos actuales
        return render.editar_contacto(contacto)

    