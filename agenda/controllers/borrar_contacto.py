import web
import sqlite3

render = web.template.render('views', base='layout')

class Borrar_contacto:

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
            print(f"ERROR Borrar 100: {error.args}")
            return None
        finally:
            conn.close()

    def eliminarContacto(self, id_contacto:int):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "DELETE FROM contactos WHERE id_contacto = ?"
            cursor.execute(query, (id_contacto,))
            conn.commit() # Importante: ¡guardar los cambios!
        except Exception as error:
            print(f"ERROR Borrar 101: {error.args}")
        finally:
            conn.close()

    def GET(self, id_contacto):
        contacto = self.obtenerContacto(id_contacto)
        # Renderiza la vista pidiendo confirmación (ej. "¿Seguro que deseas borrar a John?")
        return render.borrar_contacto(contacto)

    def POST(self, id_contacto):
        # Cuando se envía el formulario de confirmación, se borra y redirige a la lista
        self.eliminarContacto(id_contacto)
        raise web.seeother('/lista_contactos')