from flask_smorest import Blueprint

bp = Blueprint('posts', __name__, description='Ops on Posts', url_prefix='/post')

from . import routes