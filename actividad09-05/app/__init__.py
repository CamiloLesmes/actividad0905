from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la aplicación
    app.config.from_object('config.Config')

    # Registro de las rutas
    from . import routes
    app.register_blueprint(routes.bp)

    return app
