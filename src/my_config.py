import os
import json


class Config:
    """
    Read default configurations from setting file
    """
    PATH_PARENT = os.path.dirname(os.getcwd())

    config_file = "{0}/config.json".format(PATH_PARENT)

    with open(config_file) as cf:
        config = json.load(cf)

        APP_NAME = config['APP_NAME']
        VERSION = config['VERSION']
        ENV = int(config['ENV'])

        PATH_SRC = config['PATHS']['SOURCE_CODE']
        PATH_DATA = config['PATHS']['DATA']
        PATH_DATA_INPUT = config['PATHS']['DATA_INPUT']
        PATH_DATA_OUTPUT = config['PATHS']['DATA_OUTPUT']
        PATH_LOG = config['PATHS']['LOG']
        PATH_TESTING = config['PATHS']['TESTING']

        INPUT_CRIME_DATA = config['INPUT']['CRIME_DATA']


class Environment:
    """
    Environment Value
    """
    UAT = 1
    PROD = 9
