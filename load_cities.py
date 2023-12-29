from database import db, Ciudad
from app import app


def load_data():
    with app.app_context():  # Utiliza el contexto de la aplicación
        data = [
        ('Montevideo', 1529082), ('Salto', 110828), ('Ciudad de la Costa', 104694), 
        ('Paysandú', 96690), ('Maldonado', 95182), ('Rivera', 85900), 
        ('Las Piedras', 70247), ('Tacuarembó', 56757), ('Melo', 56245), 
        ('Artigas', 48567), ('Mercedes', 45975), ('Minas', 42446), 
        ('San José de Mayo', 40747), ('Durazno', 37466), ('Florida', 33640), 
        ('Treinta y Tres', 33458), ('Barros Blancos', 31650), ('Ciudad del Plata', 31146), 
        ('San Carlos', 27471), ('Colonia del Sacramento', 26231), ('Pando', 25949), 
        ('Rocha', 25422), ('Fray Bentos', 25191), ('Salinas', 23005), 
        ('Trinidad', 22402), ('18 de Mayo', 21871), ('La Paz', 21526), 
        ('Canelones', 21265), ('Dolores', 20935), ('Carmelo', 20541), 
        ('Bella Unión', 20377), ('Young', 19756), ('Santa Lucía', 19742), 
        ('Progreso', 19244), ('Paso Carrasco', 18908), ('Joaquín Suárez', 18865), 
        ('General Líber Seregni', 18656), ('Río Branco', 18604), ('Nueva Helvecia', 18401), 
        ('Toledo', 18210), ('Paso de los Toros', 18105), ('Juan Lacaze', 17816), 
        ('Punta del Este', 17123), ('Parque del Plata', 16942), ('Piriápolis', 16833), 
        ('Rosario', 14688), ('Libertad', 12166), ('Nueva Palmira', 10857), 
        ('Chuy', 10724), ('Castillos', 10252)
    ]

        for nombre, poblacion in data:
            ciudad = Ciudad(nombre=nombre, poblacion=poblacion)
            db.session.add(ciudad)
        db.session.commit()

if __name__ == '__main__':
    load_data()



