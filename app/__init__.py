# -*- coding: iso-8859-1 -*-

from flask_restx import Api
from flask import Blueprint

from app.main.controller import api as sample_namespace

blueprint = Blueprint('api', __name__)

# TODO: Change
api = Api(blueprint,
          title='PROJECT-NAME',
          version='1.0',
          description='Project description')

api.add_namespace(sample_namespace)
