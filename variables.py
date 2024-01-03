import os
import sys


class GlobalVariables:
    if not os.environ.get('IP_ADDRESS_OSM'):
        print("TIP: export an IP_ADDRESS_OSM environment variable "
              "(e.g. $ export IP_ADDRESS_OSM='A.B.C.D'), where A.B.C.D is the OSM IP address! Exiting...")
        sys.exit()

    PUBLIC_IP_OSM = 'http://' + os.environ.get('IP_ADDRESS_OSM') + '/osm'

    @classmethod
    def get_public_ip_osm(cls):
        return cls.PUBLIC_IP_OSM

    @classmethod
    def set_public_ip_osm(cls, value):
        cls.PUBLIC_IP_OSM = value

