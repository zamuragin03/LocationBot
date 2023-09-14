from geopy import distance
from .LocationService import LocationService


class GeoService:

    def IsUserInArea(latitude, longitude, location_id):
        lat, lon = LocationService.GetLocationLonLat(location_id)
        dis = distance.distance(
            (float(lat),float(lon)),
            (float(latitude), float(longitude))
        ).m
        return dis < 250
