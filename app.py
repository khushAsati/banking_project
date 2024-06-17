from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import initialize_db


app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)
initialize_db(app)

from controllers import customer_controller, banker_controller

app.register_blueprint(customer_controller)
app.register_blueprint(banker_controller)

if __name__ == '__main__':
    app.run(debug=True)