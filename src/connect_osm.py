from variables import GlobalVariables
import requests, os, yaml, json, descriptors_constructor

# IPv4 address OSM NBI
PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()

# endpoints for OSM NBI resources
endpoint_generate_token = '/admin/v1/tokens'
endpoint_vnf_packages = '/vnfpkgm/v1/vnf_packages'
endpoint_vim_accounts = '/admin/v1/vim_accounts'
endpoint_ns_packages = '/nsd/v1/ns_descriptors'
endpoint_ns_instances = '/nslcm/v1/ns_instances'
endpoint_del_ns_instances = '/nslcm/v1/ns_instances'
endpoint_vnf_packages_content = '/vnfpkgm/v1/vnf_packages_content'

class ConnectOSM:
    def verify_osm_status():
        """Verify  OSM (Open Source Mano) status. """
        print("Trying to connect OSM NorthBound Interface ... \n")
        is_online = True
        # headers necessary to return suitable response
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # endpoint for bearer authentication generation
        endpoint = PUBLIC_IP_OSM + endpoint_generate_token
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
        endpoint = PUBLIC_IP_OSM + endpoint_generate_token


        response = requests.post(endpoint, headers=headers,
                                 json={"username": "admin", "password": "admin"})

        # to restory the bearer authentication
        key_search = 'id'
        if key_search in response.json():
            value = response.json()[key_search]
            headers = {"Authorization": "Bearer " + value}

        return headers

    def get_vnf_packages(): # Query information about multiple VNF package resources
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # print(url)
        bearer = ConnectOSM.generate_nbi_token()
        headers.update(bearer)
        response = requests.get(endpoint, headers=headers)

        return response.json()


    # Management operations of NS descriptors and packages
    def get_ns_packages(): # Query information about multiple NS instances

        endpoint = PUBLIC_IP_OSM + endpoint_ns_packages

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        bearer = ConnectOSM.generate_nbi_token()
        headers.update(bearer)
        response = requests.get(endpoint, headers=headers)

        return response.json()

    # Management operations of NS instances
    def get_ns_instances():
        endpoint = PUBLIC_IP_OSM + endpoint_ns_instances

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # print(endpoint_ns_instances)
        bearer = ConnectOSM.generate_nbi_token()
        headers.update(bearer)
        response = requests.get(endpoint, headers=headers)
        return response.json()

    def get_vim_accounts():
        endpoint = PUBLIC_IP_OSM + endpoint_vim_accounts

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # to generate bearer value
        bearer = ConnectOSM.generate_nbi_token()
        # update headers with bearer authentication
        headers.update(bearer)
        # response - GET method
        response = requests.get(endpoint, headers=headers)
        return response.json()

    def post_vnf_packages(self, vnfd_data):
        '''Post a new VNFd content in JSON to OSM'''
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages_content
        print(endpoint)

        # print(endpoint)
        # ajustando para enviar dados de um arquivo YAML

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        bearer = ConnectOSM.generate_nbi_token()
        headers.update(bearer)

        response = requests.request("POST", endpoint, headers=headers,
                                    data=vnfd_data)

        if response.status_code == 409:
            print("The operation cannot be executed currently, due to a conflict with the state of the resource")
            return False

        if response.status_code == 201:
            print("Successfuly VNFd onboarding on Open Source Mano")

        return response
        # # to restory id value
        # key_search = 'id'
        # if key_search in response.json():
        #     id_value = response.json()[key_search]
        #
        #  return id_value


