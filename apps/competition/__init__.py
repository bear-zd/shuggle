from flask import Blueprint

competition = Blueprint(name='competition', import_name=__name__)

from . import views