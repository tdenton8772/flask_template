from application import application
import logging
import logging.config

def default(_value):
    application.logger.debug(_value)
    return True