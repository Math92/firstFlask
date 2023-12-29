from flask import Flask
from database import db
import routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


routes.init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
