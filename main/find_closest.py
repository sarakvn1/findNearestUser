from math import cos, asin, sqrt


def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(hav))


def closest(data, v):
    return min(data, key=lambda p: [d:=distance(v['lat'], v['lon'], p['location']['lat'], p['location']['lon']),p.update({"distance":d})])

# min(data, key=lambda p: [d:=distance(v['lat'], v['lon'], p['location']['lat'], p['location']['lon']),p.update({"distance":d})])
# tempDataList = [{'lat': 39.7612992, 'lon': -86.1519681},
#                 {'lat': 39.762241, 'lon': -86.158436},
#                 {'lat': 39.7622292, 'lon': -86.1578917}]

v = {'lat': 39.7622290, 'lon': -86.1519750}
# print(closest(tempDataList, v))
