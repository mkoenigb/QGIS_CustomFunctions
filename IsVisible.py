from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def is_visible(inputlayername, feature, parent):
    layer = QgsProject.instance().mapLayersByName(inputlayername)[0]
    isvisible = 0 # reset indicator
    renderer = layer.renderer().clone()
    ctx = QgsRenderContext()
    renderer.startRender(ctx, QgsFields())
    ctx.expressionContext().setFeature(feature)
    if QgsProject.instance().layerTreeRoot().findLayer(layer.id()).isVisible(): # check if layer is visible
        if renderer.willRenderFeature(feature, ctx): # check if category is visible
            isvisible = 1
    renderer.stopRender(ctx)

    return isvisible
