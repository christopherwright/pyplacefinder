# pyplacefinder

Want to know what's awesome?

Yahoo! PlaceFinder allows 50k free hits to their Geocode API each day - That's **20 times more than Google's**!

This simple module will allow you to query any location data as per their API (http://developer.yahoo.com/geo/placefinder/guide/requests.html), and read the data out as a dict.

Easy as bro.

## Using it
    
    import pyplacefinder
    ppf = pyplacefinder.PlaceFinder('YOUR_APP_ID_HERE')
    
    ppf.geocode(location='armadale, victoria, australia')
    >>> [{u'neighborhood': u'Armadale', u'house': '', u'county': '', u'street': '', u'radius': 1200, u'quality': 50, u'unit': '', u'city': u'Melbourne', u'countrycode': u'AU', u'woeid': 1107203, u'xstreet': '', u'line4': u'AUSTRALIA', u'line3': '', u'line2': u'ARMADALE  VIC  3143', u'line1': '', u'state': u'Victoria', u'latitude': u'-37.855560', u'hash': '', u'unittype': '', u'offsetlat': u'-37.855560', u'statecode': u'VIC', u'postal': u'3143', u'name': '', u'uzip': u'3143', u'country': u'Australia', u'longitude': u'145.021164', u'countycode': '', u'offsetlon': u'145.021164', u'woetype': 22}]
    
    ppf.geocode(name='sydney opera house')
    >>> [{u'neighborhood': '', u'house': '', u'county': '', u'street': '', u'radius': 200, u'quality': 90, u'unit': '', u'city': u'Sydney', u'countrycode': u'AU', u'woeid': 28717584, u'xstreet': '', u'line4': u'AUSTRALIA', u'line3': '', u'line2': u'SYDNEY  NSW  2000', u'line1': u'Sydney Opera House', u'state': u'New South Wales', u'latitude': u'-33.857639', u'hash': '', u'unittype': '', u'offsetlat': u'-33.857639', u'statecode': u'NSW', u'postal': u'2000', u'name': u'Sydney Opera House', u'uzip': u'2000', u'country': u'Australia', u'longitude': u'151.214706', u'countycode': '', u'offsetlon': u'151.214706', u'woetype': 20}]
    
    
    ppf.geocode(house='169', street='chapel st', city='melbourne', country='australia')
    >>> [{u'neighborhood': '', u'house': '', u'county': '', u'street': '', u'radius': 61600, u'quality': 40, u'unit': '', u'city': u'Melbourne', u'countrycode': u'AU', u'woeid': 1103816, u'xstreet': '', u'line4': u'AUSTRALIA', u'line3': '', u'line2': u'MELBOURNE  VIC', u'line1': '', u'state': u'Victoria', u'latitude': u'-37.817532', u'hash': '', u'unittype': '', u'offsetlat': u'-37.817532', u'statecode': u'VIC', u'postal': '', u'name': '', u'uzip': '', u'country': u'Australia', u'longitude': u'144.967148', u'countycode': '', u'offsetlon': u'144.967148', u'woetype': 7}]
    
    
    ppf.reverseGeocode(location='-33.87686,151.220967')
    [{u'neighborhood': '', u'house': u'229', u'county': '', u'street': u'Darlinghurst Rd', u'radius': 500, u'quality': 99, u'unit': '', u'city': u'Sydney', u'countrycode': u'AU', u'woeid': 12706670, u'xstreet': '', u'line4': u'AUSTRALIA', u'line3': '', u'line2': u'SYDNEY  NSW  2010', u'line1': u'229 Darlinghurst Rd', u'state': u'New South Wales', u'latitude': u'-33.876860', u'hash': '', u'unittype': '', u'offsetlat': u'-33.876860', u'statecode': u'NSW', u'postal': u'2010', u'name': '', u'uzip': u'2010', u'country': u'Australia', u'longitude': u'151.220967', u'countycode': '', u'offsetlon': u'151.220967', u'woetype': 11}]