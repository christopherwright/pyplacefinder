import urllib
import json

VERSION = (0, 1, 0, "pre")
def get_version():
  version = '%s.%s' % (VERSION[0], VERSION[1])
  if VERSION[2]:
    version = '%s.%s' % (version, VERSION[2])
  if VERSION[3:]:
    version = '%s.%s' % (version, VERSION[3])
  return version


class PlaceFinderException(Exception):
  pass

class PlaceFinder(object):
  def __init__(self, appid=""):
    self.appid = appid
  
  def geocode(self, **params):
    try:
      results = self.query(params)
      return results
    except PlaceFinderException:
      return None
  
  def reverseGeocode(self, **params):
    params['gflags'] = 'r'
    return self.geocode(**params)
  
  def query(self, params):
    params['appid'] = self.appid
    params['flags'] = "j"
    
    url = "http://where.yahooapis.com/geocode?%s" % urllib.urlencode(params)
    connection = urllib.urlopen(url)
    
    try:
      data = json.loads(connection.read())
      if data['ResultSet']['Error'] > 0:
        raise PlaceFinderException(data['ResultSet']['ErrorMessage'])
      else:
        if len(data['ResultSet']['Results']) > 0:
          return data['ResultSet']['Results']
        else:
          return None
    except:
      raise PlaceFinderException
    finally:
      connection.close()
