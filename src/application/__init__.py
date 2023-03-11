from flask import Flask, request
from config import configure_app
from flask_session import Session
import logging
import json

application = Flask(__name__)

configure_app(application)
Session(application)

@application.errorhandler(500)
def internal_server_error(error):
    application.logger.error('Client Error: {}, path: {}'.format(error, request.path))
    error = 'Server Error: %s', (error)
    return 'Server Error:'

@application.errorhandler(404)
def page_not_found(error):
    application.logger.error('Client Error: {}, path: {}'.format(error, request.path))
    error = 'Client Error %s', (error)
    return 'Client Error:'

@application.errorhandler(Exception)
def unhandled_exception(error):
   application.logger.error('Client Error: {}, path: {}'.format(error, request.path))
   error = 'Unhandled Exception: %s', (error)
   return 'Server Error:'

from application.views import base
application.register_blueprint(base.mod)


if __name__ == 'application':
    from application import views