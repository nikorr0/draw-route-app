import warnings
import matplotlib.pyplot as plt
import osmnx as ox
from time import time
from os.path import exists
from os import makedirs
from shutil import rmtree

from . import get_property

def draw_area_map_route_precise(coordinates, dist=None, bgcolor='white', edge_color='gray',
                        route_color='#D4AC0D', alpha_route=0.8, alpha_points=0.8, legend=True, middle_point=None,
                        departure_point_color='#CB4335', departure_point_size=70, arrival_point_color='#28B463', arrival_point_size=70,
                        title=None, title_fontsize=15, filename="map_", directory='maps', save_map=True, set_file_id=True,
                        place_intermediate_points=True, intermediate_point_color="route_color", intermediate_point_size=70):

    if len(coordinates) < 2:
        raise Exception("The list contains less than 2 points!")

    if dist is None:
        dist = 0
        for i in range(0, len(coordinates)-1): 
            dist += get_property.get_distance(coordinates[i], coordinates[i+1], more_precise=True) * 1000
            
    if set_file_id:
        file_id = "time_" + str(round(time(), 2)).replace(".", "_")
        
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # creating map (only roads)
        if middle_point is None:
            middle_point = ((coordinates[0][0] + coordinates[-1][0]) / 2, (coordinates[0][1] + coordinates[-1][1]) / 2)
        graph = ox.graph_from_point(middle_point, dist=dist, 
                                    network_type="drive", dist_type='network',)
        
        x1, y1 = coordinates[0]
        orig_first = ox.nearest_nodes(graph, y1, x1)
        origin_point = (graph.nodes[orig_first]['x'], graph.nodes[orig_first]['y'])

        x2, y2 = coordinates[-1]
        dest_last = ox.nearest_nodes(graph, y2, x2)
        destination_point = (graph.nodes[dest_last]['x'], graph.nodes[dest_last]['y'])
        # if orig_first == dest_last:
        #     raise Exception("The nodes of the graph with the places of departure and arrival correspond! The points on the map are the same.")

    routes = list()
    if place_intermediate_points:
        intermediate_points = list()
        for i in range(1, len(coordinates)-1):
            x1, y1 = coordinates[i]
            inter = ox.nearest_nodes(graph, y1, x1)
            intermediate_points.append((graph.nodes[inter]['x'], graph.nodes[inter]['y']))
                
    for i in range(0, len(coordinates)-1): 
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i+1]

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # getting the nearest node to the points
            orig = ox.nearest_nodes(graph, y1, x1)
            dest = ox.nearest_nodes(graph, y2, x2)

            # getting the shortest route between two points
            route = ox.shortest_path(graph, orig, dest, cpus=None)
            # adding the route into a list (for further drawing it on the map)
            routes.append(route)


    if len(routes) > 1 or len(routes) == 1:
        # drawing routes on map
        if len(routes) > 1:
            fig, ax = ox.plot_graph_routes(graph, routes, node_size=0, route_colors=route_color,
                                            route_alpha=alpha_route, edge_color=edge_color,
                                            bgcolor=bgcolor, show=False, close=False, orig_dest_size=0)

        elif len(routes) == 1:
            fig, ax = ox.plot_graph_route(graph, routes[0], node_size=0, route_color=route_color,
                                        route_alpha=alpha_route, edge_color=edge_color,
                                        bgcolor=bgcolor, show=False, close=False, orig_dest_size=0)
                
        # drawing departure and arrival points with different colors
        ax.scatter(
            origin_point[0], 
            origin_point[1],
            c=departure_point_color, 
            s=departure_point_size,
            label='Point of departure', 
            alpha=alpha_points,
            zorder=5)
        
        if (place_intermediate_points) and (len(intermediate_points) > 0):
            if intermediate_point_color == "route_color":
                intermediate_point_color = route_color

            ax.scatter(
                list(map(lambda x: x[0], intermediate_points)),
                list(map(lambda x: x[1], intermediate_points)),
                c=intermediate_point_color, 
                s=intermediate_point_size, 
                label='Intermediate point', 
                alpha=alpha_points,
                zorder=5)
        
        ax.scatter(
            destination_point[0], 
            destination_point[1], 
            c=arrival_point_color, 
            s=arrival_point_size, 
            label='Point of arrival', 
            alpha=alpha_points,
            zorder=5)
        
    
    if title is not None:
        ax.set_title(title, fontsize=title_fontsize)

    if legend:
        plt.legend() # adding legend for departure and arrival points
    if set_file_id:
        filename += file_id # creating filename
    
    if not exists(directory):
        makedirs(directory)
    
    path_to_image = f"{directory}/{filename}.png"
    fig.set_frameon(True)
    fig.savefig(path_to_image, transparent=False, facecolor=bgcolor, bbox_inches='tight')

    if not save_map:
        rmtree(directory)
        
    values_to_return = dict() 
    values_to_return['map_image'] = path_to_image
    values_to_return['distance_km'] = round(dist / 1000, 2)
    
    return values_to_return