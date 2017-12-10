import geojson
import shapely
from shapely import geometry

baltimore_boxes_geojson_string = open("modified_data/boxed_baltimore.geojson").read()
baltimore_boxes_geojson = geojson.loads(baltimore_boxes_geojson_string)

geoBoxDict = {}
for feature in baltimore_boxes_geojson["features"]:
    featureId = feature["id"]
    polygonPtList = [(pt[0], pt[1]) for pt in feature["geometry"]["coordinates"][0]]
    geoBoxDict[featureId] = shapely.geometry.polygon.Polygon(polygonPtList)
    
# Assumes we are working in Baltimore
def getBoxIdForGeo(pt):
    point1 = pt[0]
    point2 = pt[1]
    if pt[0] > 0: # Then the point is (latitude, longitude)
        point1 = pt[1]
        point2 = pt[0]
    for key,value in geoBoxDict.items():
        pointToCheck = shapely.geometry.Point(point1, point2)
        if value.contains(pointToCheck):
            return key