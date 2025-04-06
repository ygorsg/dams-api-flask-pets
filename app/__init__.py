from flask import Flask, Blueprint
from flask_restx import Api  # alterado de flask_restplus para flask_restx
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.pet.pet_controller import api as home_ns  # importando o namespace home_ns do arquivo pet_controller.py

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app, title='Api Flask Experiments', version='1.0', description='Api de experimentos com python flask', prefix='/api')
# adicionando namespace pet para rotas
api.add_namespace(home_ns, path='/pet')