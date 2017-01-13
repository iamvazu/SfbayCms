#-------------------------------------------------------------------------------
# Name:        config.py
# Purpose:      Sets global configuration options for mockRealestateApplicatoin
#
# Author:      Lord Azu
#
# Created:     12/01/2017
# Copyright:   (c) Lord Azu 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Config(object):
    """"""
    pass

class DevelopmentConfig(Config):
    """ Configuration used on dev machine
    \
    Config: dict"""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    LOGGING = True # enable step by step walkthrough details

class ProductionConfig(Config):
    """Configuration used in production
    \
    Config: dict"""
    DEBUG = False
    LOGGING = True

class TesttingConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    LOGGING = True
    TESTING = True

app_config = {
            'development' : DevelopmentConfig,
            'production' : ProductionConfig
            }

