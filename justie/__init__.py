from flask import Flask

from justie.views.routes import views

app = Flask(__name__)

app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"

app.register_blueprint(views)