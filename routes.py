from flask import jsonify, send_from_directory
from database import Ciudad
from sqlalchemy import func

def init_routes(app):
    @app.route('/ciudades', methods=['GET'])
    def get_ciudades():
        ciudades = Ciudad.query.all()
        return jsonify([{'nombre': c.nombre, 'poblacion': c.poblacion} for c in ciudades])
    
        
    @app.route('/')
    def home():
        return send_from_directory('static', 'index.html')
    
    @app.route('/ciudades/<nombre_ciudad>', methods=['GET'])
    def get_ciudad(nombre_ciudad):
        ciudad = Ciudad.query.filter(func.lower(Ciudad.nombre) == func.lower(nombre_ciudad)).first()
        if ciudad:
            return jsonify({'nombre': ciudad.nombre, 'poblacion': ciudad.poblacion})
        else:
            return jsonify({'error': 'Ciudad no encontrada'}), 404
