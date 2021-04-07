from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def get_projectcrs(project_crs, feature, parent):
    return QgsCoordinateReferenceSystem(project_crs).description()
