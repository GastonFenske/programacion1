from main import create_app
import os

app = create_app()


#Esto permite acceder a la propiedades de la app en cualquier parte del sis
app.app_context().push()

if __name__ == '__main__':
    app.run(port=os.getenv("PORT"), debug=True)
