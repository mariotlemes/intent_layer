from variables import GlobalVariables
import requests, os

PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()

def verify_osm_status():
    """Verify  OSM (Open Source Mano) status. """

    print("Trying to connect OSM NorthBound Interface ... \n")
    is_online = True
    # headers necessary to return suitable response
    headers = {"Accept": "application/json", "Content_Type": "application/json"}
    # endpoint for bearer authentication generation
    endpoint = PUBLIC_IP_OSM + '/admin/v1/tokens'
    # print(endpoint)
    try:
    # send a POST request to generate token
        response = requests.post(endpoint, headers=headers,
                                 json={"username": "admin", "password": "admin"})
        print("Connected!")
    except requests.Timeout:
        print("\nTimeout! OSM is probably down...")
        is_online = False
    except requests.RequestException as e:
        print("Error:", e)

    return is_online

def generate_nbi_token():
    """Generarte token for NBI authentication"""

    # necessary to return json object
    headers = {"Accept": "application/json", "Content_Type": "application/json"}
    # endpoint for bearer authentication generation
    endpoint = PUBLIC_IP_OSM + '/admin/v1/tokens'

    # print(endpoint)

    response = requests.post(endpoint, headers=headers,
                             json={"username": "admin", "password": "admin"})

    # print(response.status_code)

    # to restory the bearer authentication
    key_search = 'id'
    if key_search in response.json():
        value = response.json()[key_search]
        headers = {"Authorization": "Bearer " + value}

    return headers

