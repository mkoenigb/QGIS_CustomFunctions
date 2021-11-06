from qgis.core import *
from qgis.gui import *
import json

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def keyvalues_from_nested_dict(inp, k, feature, parent):
    outp = []
    li = json.loads(inp) # convert the string representation of a list to an actual list
    for dic in li: # iterate over this list of dictionaries
        for k1,v1 in dic.items(): # iterate over the first dict
            if k1 == k: # if the current key is the key we are searching for, append its value to the outputlist
                outp.append(v1)
            if type(v1) == dict: # if the current value is of type dict, iterate over this sub-dictionary
                for k2,v2 in v1.items():
                    if k2 == k:
                        outp.append(v2)
                    if type(v2) == dict:
                        for k3,v3 in v2.items():
                            if k3 == k:
                                outp.append(v3)
    return outp
