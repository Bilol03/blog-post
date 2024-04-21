from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask import Flask
from routes.route import main

from models.db import db
app = Flask(__name__)
app.register_blueprint(main)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
CKEditor(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db.init_app(app)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, port=5003)
