
from flask import Flask
from flask_cors import CORS
from app.models.database import db
from app.models.admin_user import AdminUser
from app.routes.url_checker import url_checker
from app.routes.admin import admin
from app.routes.export import export

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://sql8789185:x8RdbVlGdj@sql8.freesqldatabase.com:3306/sql8789185'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# print(app.config['SQLALCHEMY_DATABASE_URI'])


CORS(app, resources={r"/api/*": {"origins": "*"}})
db.init_app(app)

app.register_blueprint(url_checker)
app.register_blueprint(admin)
app.register_blueprint(export)

@app.route('/')
def home():
    return 'Phishing Detection API is running.'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=10000)
