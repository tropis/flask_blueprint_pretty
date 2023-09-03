# config.py 
# This is located outside the main package.
# instance_relative_config=True means config file is in the parent folder flask_soicat

class Config:
    PLACE = "Home"
    COLOR = "white"

class ConfigProd(Config):
    COLOR = "red"

class ConfigDev(Config):
    COLOR = "blue"

class ConfigTest(ConfigDev):
    COLOR = "green"

