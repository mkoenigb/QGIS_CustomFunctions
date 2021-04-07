@qgsfunction(args='auto', group='Custom')
def canvas_extent(feature, parent):    
    e = QgsGeometry.fromWkt(qgis.utils.iface.mapCanvas().extent().asWktPolygon())
    return e
