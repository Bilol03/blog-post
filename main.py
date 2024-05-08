from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask import Flask
from routes.route import main
from flask_login import LoginManager
from models.db import db, User
from flask_gravatar import Gravatar
import os

app = Flask(__name__)
app.register_blueprint(main)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


Bootstrap5(app)
CKEditor(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI', 'sqlite:///posts.db')
db.init_app(app)


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, port=4200)
