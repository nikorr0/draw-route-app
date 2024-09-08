import numpy as np
from datetime import datetime, date, timedelta
import pickle
from meteostat import Hourly, Point
import warnings
from .get_property import get_distance


with open("packages/model_files/linear_model_ridge.pickle", 'rb') as f:
    model = pickle.load(f)
    
with open("packages/model_files/scalers.pickle", 'rb') as f:
    scalers = pickle.load(f)

def string_to_datetime(date_time):
    if "." in date_time:
        date_time = date_time.split(".")[0]
        date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    
    elif "+" in date_time:
        date_time = date_time.split("+")[0]
        date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    
    else:
        date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
    
    start_date = str(date(year=date_time.year, month=date_time.month, day=date_time.day))
    return start_date, date_time.hour, date_time
        
def date_to_busy_day(x):
    x = datetime.strptime(x, '%Y-%m-%d')
    x = date(year=x.year, month=x.month, day=x.day)
    
    if np.is_busday(x, weekmask='0000011'):
        return 1
    else:
        return 0

def hour_to_rush_hour(x, rush_hours=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]):
    if x in rush_hours:
        return 1
    else:
        return 0
    
def change_weather(x):
    if x in [-1, 1, 2, 3, 4]:
        return 0 # no natural phenomena
    elif x in [5, 6]:
        return 1 # fog
    elif x in [7, 8]:
        return 2 # rain
    elif x in [9, 10, 11, 17, 18]:
        return 3 # heavy rain
    elif x in [12, 14, 15]:
        return 4 # snow
    elif x in [13, 16, 19, 20, 21, 22]:
        return 5 # heavy snow
    elif x in [23, 25, 26]:
        return 6 # thunderstorm
    elif x in [24, 27]:
        return 7 # hail/storm
    
def change_weather_to_str(x):
    if x == -1:
        return "Unknown"
    elif x == 0:
        return "No natural phenomena"
    elif x == 1:
        return "Fog"
    elif x == 2:
        return "Rain"
    elif x == 3:
        return "Heavy rain"
    elif x == 4:
        return "Snow"
    elif x == 5:
        return "Heavy snow"
    elif x == 6:
        return "Thunderstorm"
    elif x == 7:
        return "Hail or storm"
    else:
        return x

def get_weather(start_coords, start_date, start_hour):
    city = Point(start_coords[0], start_coords[1])

    year, month, day = start_date.split('-')
    start = datetime(int(year), int(month), 
                     int(day), int(start_hour), 0)
    
    try:
        data_weather = Hourly(city, start, start)
        data_weather = data_weather.fetch()
        weather, temperature, wind_speed, total_precipitation = data_weather.iloc[0][['coco', 'temp', 'wspd', 'prcp']]
    except:
        print("Warning: Weather information does not defined. \
            \nIt may be due to extraordinary date. Setting date to common values for the model prediction.")
        weather, temperature, wind_speed, total_precipitation = [np.NAN] * 4
    
    weather_data = [weather, temperature, wind_speed, total_precipitation]
    for i in range(len(weather_data)):
        if np.isnan(weather_data[i]):
            weather_data[i] = "Unknown"
    return weather_data

def weather_show_to_number(weather_show, temperature_show, 
                           wind_speed_show, total_precipitation_show):
    if type(weather_show) is str:
        weather_show = -1
    if type(temperature_show) is str:
        temperature_show = 20
    if type(wind_speed_show) is str:
        wind_speed_show = 0
    if type(total_precipitation_show) is str:
        total_precipitation_show = 0
    return weather_show, temperature_show, wind_speed_show, total_precipitation_show

def add_time(start_date_time, time_minutes):
    arrival_date = start_date_time + timedelta(seconds=time_minutes * 60)
    return str(arrival_date).split(".")[0]
    

def predict_traveled_time(coordinates, distance=None, 
                          date_time=None, calculate_distance=True):
    # Takes:
    # coordinates = [start_coords (the starting point of the path),
    # end_coords (the end point of the path)]
    # in format [latitude, longitude]
    # distance (optional) - route length in kilometers 
    # date_time in string "2024-03-25 12:00:00"
    # calculate_distance - calculates and returns distance
    
    # Returns: 
    # weather information, distance (km) (float), 
    # predicted travel time (minutes) (float)
    # and the date of arrival (str)
    
    # Weather information:
    # weather - natural phenomenon (str)
    # temperature - temperature (in degrees Celsius) (float64)
    # wind_speed - average wind speed (km/h) (float64)
    # total_precipitation - total precipitation per hour (mm) (float64)
    
    if date_time is None:
        date_time = "2024-03-25"

    if len(date_time.split(' ')) == 1:
        date_time += " 12:00:00"
        
    start_date, start_hour, date_time = string_to_datetime(date_time)
    busy_day = date_to_busy_day(start_date)
    rush_hour = hour_to_rush_hour(start_hour)
    start_coords = coordinates[0]
    end_coords = coordinates[-1]
    
    if calculate_distance and distance is not None:
        distance = get_distance(start_coords, end_coords)
    
    distance_scaled = scalers['distance'].transform([[distance]])[0][0]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        weather_show, temperature_show, wind_speed_show, total_precipitation_show = get_weather(start_coords, 
                                                                            start_date, start_hour)
    weather, temperature, wind_speed, total_precipitation = weather_show_to_number(weather_show, temperature_show, 
                                                                                   wind_speed_show, total_precipitation_show)
    if weather_show != 'Unknown':
          weather_show = change_weather(weather_show)
    
    weather = change_weather(weather)
    temperature_scaled = scalers['temperature'].transform([[temperature]])[0][0]
    wind_speed_scaled = scalers['wind_speed'].transform([[wind_speed]])[0][0]
    total_precipitation_scaled = scalers['total_precipitation'].transform([[total_precipitation]])[0][0]
    
    travel_data = np.array([busy_day, rush_hour, weather, temperature_scaled, 
                            wind_speed_scaled, total_precipitation_scaled, distance_scaled])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        time_traveled = round(model.predict(travel_data.reshape(1, -1))[0], 2)
    arrival_date = add_time(date_time, time_traveled)
    
    export = dict()
    export['weather'] = change_weather_to_str(weather_show)
    export['temperature'] = temperature_show
    export['wind_speed'] = wind_speed_show
    export['total_precipitation'] = total_precipitation_show
    export['predicted_time'] = time_traveled
    export['departure_date'] = date_time
    export['arrival_date'] = arrival_date
    
    if calculate_distance:
        export['distance'] = distance
    
    return export