from main import create_app, db
import os

app = create_app()

#Esto permite acceder a la propiedades de la app en cualquier parte del sis
app.app_context().push()

if __name__ == '__main__':

    #Me crea o me carga las tablas
    db.create_all()

    app.run(port=os.getenv("PORT"), debug=True)
