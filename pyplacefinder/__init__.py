from geopy.point import Point
from geopy.location import Location
from geopy import geocoders

VERSION = (0, 1, 0, "pre")

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:]:
        version = '%s.%s' % (version, VERSION[3])
    return version

# import urllib 
# from django.conf import settings 
# from django.utils import simplejson as json 
# class YahooException(Exception): 
#   pass 
# # interface that behaves similarly to geopy's geocoders 
# class YahooGeocode(object): 
#   @classmethod 
#   def strip_result(cls, result): 
#     if not result['postal']: 
#       result['postal'] = result.get('uzip', '') 
#     place = '%(city)s, %(statecode)s %(postal)s' % result 
#     # return things in a geopy compatible format 
#     return place, (float(result['latitude']), 
# float(result['longitude'])) 
#   def geocode(self, query, exactly_one=False): 
#     try: 
#       results = [YahooGeocode.strip_result(r) for r in 
# placefind(query)] 
#       return results[0] if exactly_one else results 
#     except YahooException: 
#       return None 
# def placefind(query): 
#   file = urllib.urlopen("http://where.yahooapis.com/geocode?%s" % 
# urllib.urlencode({ 
#     'appid': settings.YAHOO_APP_ID, 
#     'flags': 'j', 
#     'q': query 
#   })) 
#   try: 
#     result = json.loads(file.read()) 
#     return result['ResultSet']['Results'] 
#   except: 
#     raise YahooException() 
#   finally: 
#     file.close() 