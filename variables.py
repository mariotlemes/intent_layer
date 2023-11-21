import os

class GlobalVariables:
    IP = os.environ.get('IP_ADDRESS_OSM')
    print(IP)
    PUBLIC_IP_OSM = 'http://' + IP + '/osm'
    print(PUBLIC_IP_OSM)

    @classmethod
    def get_public_ip_osm(cls):
        return cls.PUBLIC_IP_OSM

    @classmethod
    def set_public_ip_osm(cls, value):
        cls.PUBLIC_IP_OSM = value

