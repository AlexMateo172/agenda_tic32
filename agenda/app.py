import web


urls = (
    '/', 'index',
    '/lista_contactos','Lista_contactos',
    '/ver_contacto','Ver_contacto',
    '/editar_contacto','Editar_contacto',
    '/borrar_contacto','Borrar_contacto'
    
)
app = web.application(urls, globals())
render = web.template.render('views')

    
class Lista_contactos:
    def GET(self):    
        return render.lista_contactos()

class Ver_contacto:
     def GET(self):
         return render.ver_contacto()

class Editar_contacto:
     def GET(self):
         return render.editar_contacto()   

class Borrar_contacto:
     def GET(self):
         return render.borrar_contacto()          


if __name__ == "__main__":
    app.run()