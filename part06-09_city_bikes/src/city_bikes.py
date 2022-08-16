# tee ratkaisu tänne
# Write your solution here
from math import sqrt

def reading_file(filename):
    result = []
    with open(filename) as f:
        for line in f:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            result.append(parts)
    return result

def get_station_data(filename: str):
    data = reading_file(filename)
    result = {}
    for line in data:
        result[line[3]] = (float(line[0]), float(line[1]))
    return result

def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    for station1 in stations:
        for station2 in stations:
            distance_bw = distance(stations, station1, station2)
            if distance_bw > max_distance:
                max_distance = distance_bw
                result  = (station1, station2, max_distance)
    return result 
