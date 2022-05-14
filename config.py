import os
class Config:
  '''
  '''
  SECRET_KEY='1234'
  SQLALCHEMY_TRACK_MODIFICATIONS = False 
  
  
class ProdConfig(Config):
  '''
  '''
  pass
  
 

class DevConfig(Config):
  '''
  '''
  pass
  DEBUG=True  

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}