import geopy
from geopy import distance

def check_if_in_area(selected_point, borders):
    if (selected_point[0] > borders[1] and selected_point[0] < borders[0]) and\
          (selected_point[1] > borders[3] and selected_point[1] < borders[2]):
        return True
    else:
        return False

def get_distance(point_from, point_to, more_precise=True):
    dist = geopy.distance.distance(point_from, point_to).km
    if more_precise:
        # The distance is calculated as the shortest line 
        # between two points, it can be considered as a hypotenuse, 
        # and to find the sum of the legs (and a = b, since we assume 
        # that our path is the rectangular triangle and it is isosceles), 
        # therefore, by the formula, multiply the hypotenuse by the root of 2. 
        # Sometimes it's still less than the actual distance, sometimes more.
        dist *= 2**0.5 
    return float(round(dist, 2))