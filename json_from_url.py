from qgis.core import *
from qgis.gui import *
import urllib
import json
import xmltodict

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def json_from_url(url, feature, parent):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    
    try: # handle JSON response
        encoding = response.info().get_content_charset('utf-8')
        data = json.loads(response_data.decode(encoding))
        data_string = json.dumps(data) # make it a string
    except: # handle XML response
        data = xmltodict.parse(response_data)
        data_string = json.dumps(data) # make it a string

    return data_string
