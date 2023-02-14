"""
Helper functions to assist with Mongo setup.
"""

def construct_url(env, pw):
  """ constructs the proper mongo connection string using config.ini and secrets """
  return env['MONGO_URL_FIRST'] + pw + env['MONGO_URL_SECOND']