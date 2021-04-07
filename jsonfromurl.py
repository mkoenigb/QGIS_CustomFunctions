from qgis.core import *
from qgis.gui import *
import urllib.request
import urllib
import json

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def json_from_url(url, feature, parent, context):
    header = {"accept":"application/json"}
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    encoding = response.info().get_content_charset('utf-8')
    data = json.loads(response_data.decode(encoding))
    #txt = json.dumps(data) #uncomment this line to receive data as string. also change next line to: return txt
    return data
