from flask import Blueprint

competition = Blueprint(name='competition', import_name=__name__,url_prefix='/competition')

from . import views