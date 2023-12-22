import os

class GlobalVariables:
    PUBLIC_IP_OSM = 'http://' + os.environ.get('IP_ADDRESS_OSM') + '/osm'

    @classmethod
    def get_public_ip_osm(cls):
        return cls.PUBLIC_IP_OSM

    @classmethod
    def set_public_ip_osm(cls, value):
        cls.PUBLIC_IP_OSM = value

