from app import create_app

# Crear la aplicación Flask
app = create_app()

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
