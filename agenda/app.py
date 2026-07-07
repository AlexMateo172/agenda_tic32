import web


urls = (
    '/', 'controllers.index.Index',
    '/lista_contactos','controllers.lista_contactos.Lista_contactos',
    '/ver_contacto/(.*)','controllers.ver_contacto.Ver_contacto',
    '/editar_contacto/(.*)','controllers.editar_contacto.Editar_contacto',
    '/borrar_contacto/(.*)','controllers.borrar_contacto.Borrar_contacto'
    
)
app = web.application(urls, globals())
render = web.template.render('views')

    


if __name__ == "__main__":
    app.run()