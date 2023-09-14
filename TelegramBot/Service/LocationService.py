from .API import LocationApi
from .ActionTypeService import ActionTypeService


class LocationService():
    def GetAllLocationsList():
        return [el['name'] for el in LocationApi.GetAllLocations()]

    def GetLastLocation(external_id):
        location_id = ActionTypeService.GetLastUserAction(
            external_id=external_id).get('location')
        return LocationApi.GetLocation(location_id).get('name')

    def GetLastLocationId(external_id):
        return ActionTypeService.GetLastUserAction(
            external_id=external_id).get('location').get('id')

    def GetLocationLonLat(id):
        location = LocationApi.GetLocation(id)
        return location.get('latitude'), location.get('longitude')

    def GetLocationNameById(id):
        return LocationApi.GetLocation(id).get('name')

    def GetLocationIdByName(name):
        locations = LocationApi.GetAllLocations()
        for el in locations:
            if el.get('name') == name:
                return el.get('id')
