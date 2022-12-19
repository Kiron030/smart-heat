import qgis.core
import qgis.utils

# Load a shapefile containing geospatial data
shapefile = r"C:\Users\User\Desktop\Workbench\GIS\Tests für OpenData 11.2022\Postleitzahlengebiete_-_Berlin\PLZ_Berlin.shp"

# "path/to/shapefile.shp"

layer = qgis.utils.iface.addVectorLayer(shapefile, "Shapefile", "ogr")

# Access the features in the layer
features = layer.getFeatures()

# Loop through each feature and print its attributes
for feature in features:
    attributes = feature.attributes()
    print(attributes)

# Access a specific attribute of each feature
for feature in features:
    attribute = feature["field_name"]
    print(attribute)

# Change the style of the layer
symbol = qgis.core.QgsFillSymbol()
layer.setRenderer(qgis.core.QgsSingleSymbolRenderer(symbol))

# Refresh the map canvas
qgis.utils.iface.mapCanvas().refresh()