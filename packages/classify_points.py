import osmnx as ox
import shapely
import geopy
from geopy import distance

def change_to_classes(x):
    if x in ["restaurant", "cafe", "fast_food"]:
        return "Restaurant"
    elif x in ["bar", "pub"]:
        return "Bar"
    elif x in ["hospital", "doctors", "clinic"]:
        return "Hospital"
    else:
        return x.capitalize()

def points_to_coords(object):
    if type(object) is shapely.geometry.point.Point:
        x, y = object.y, object.x
        
    else:
        x, y = object.centroid.y, object.centroid.x

    return f"{x}/{y}"

def calculate_distance(x, point):
    return round(geopy.distance.distance(x.split("/"), point).meters)

def classify_points(origin_dest_coords, city_places=None, return_str=True,
                    tags="default", dist=8000, max_distance=100):
    # Takes:
    # origin_dest_coords - a list of coordinates in format: [(x1, y1), (x2, y2)] 
    # where (x1, y1) is point of departure; (x2, y2) is point of arrival
    # x = lat, y = lon

    # city_places - a table with the coordinates of all places in the city and their classes,
    # city_places="None" - creates a table from scratch at the midpoint (between two)
    # tags - tags of places to find,
    # return_str=False - returns {'origin': ['bar', 24], 'destiny': ['Residential unit', 'None']
    # return_str=True - returns {'origin': ['bar', '24'], 'destiny': ['Residential unit', 'None']
    # The distance became string, not integer.
    
    # max_distance - the maximum distance at which we belong to the class
    # if the distance is greater, then it is the residential building

    # Returns dict, example: {'origin': ['bar', 24], 'destiny': ['Residential unit', 'None']}
    # 'origin' - place of departure, 'destiny' - place of arrival
    
    # if not lat_lon:
    #     for i in range(len(origin_dest_coords)):
    #         origin_dest_coords[i] = origin_dest_coords[i][::-1]
        
    if len(origin_dest_coords) != 2:
        raise Exception("Wrong coordinates!")
        
    if city_places is None:
        if tags == "default":
            tags = {"amenity": ["restaurant", "cafe", 
                            "fast_food", "bar", 
                            "pub", "cinema",
                            "hospital", "doctors", "clinic"]} 
        
        middle_point = ((origin_dest_coords[0][0] + origin_dest_coords[1][0]) / 2, 
                       (origin_dest_coords[0][1] + origin_dest_coords[1][1]) / 2)

        city_places = ox.features_from_point(middle_point, tags, dist=dist)[['amenity', 'geometry']]
        city_places['amenity'] = city_places['amenity'].apply(change_to_classes)
        city_places['x/y'] = city_places['geometry'].apply(points_to_coords)
    
    city_places['origin_distance'] = city_places['x/y'].apply(calculate_distance, point=origin_dest_coords[0])
    city_places['destiny_distance'] = city_places['x/y'].apply(calculate_distance, point=origin_dest_coords[1])
    
    origin_distance = list(city_places.loc[city_places['origin_distance'].idxmin()][['amenity', 'origin_distance']].values)
    origin_distance[1] = int(origin_distance[1])
    destiny_distance = list(city_places.loc[city_places['destiny_distance'].idxmin()][['amenity', 'destiny_distance']].values)
    destiny_distance[1] = int(destiny_distance[1])
    
    if origin_distance[1] > max_distance:
        origin_distance = ['Residential unit', '']
        
    if destiny_distance[1] > max_distance:
        destiny_distance = ['Residential unit', '']
    
    distances = dict()
    distances['origin'] = origin_distance
    distances['destiny'] = destiny_distance
    
    if return_str:
        distances['origin'][1] = str(distances['origin'][1])
        distances['destiny'][1] = str(distances['destiny'][1])
    
    return distances