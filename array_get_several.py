from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
# arr is an array-input you want to return several values from by their index
# idxarr is an array-input containing the indizes you want to return from arr
def array_get_several(arr, idxarr, feature, parent):
    elements = [arr[i] for i in idxarr]
    return elements
