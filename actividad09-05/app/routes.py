from flask import Blueprint, render_template
from .database import obtener_notas_estudiante, obtener_notas_por_curso

bp = Blueprint('routes', __name__)

# Ruta raíz: Página de inicio
@bp.route('/')
def index():
    return 'Bienvenido al sistema de notas'

# Ruta para obtener las notas de un estudiante
@bp.route('/notas/estudiante/<int:id_estudiante>', methods=['GET'])
def notas_estudiante(id_estudiante):
    notas = obtener_notas_estudiante(id_estudiante)
    return render_template('notas_estudiante.html', notas=notas)

# Ruta para obtener las notas por curso
@bp.route('/notas/curso/<int:id_curso>', methods=['GET'])
def notas_curso(id_curso):
    notas = obtener_notas_por_curso(id_curso)
    return render_template('notas_curso.html', notas=notas)
