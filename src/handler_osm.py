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
enpoint_ns_packages_content = '/nsd/v1/ns_descriptors_content'
endpoint_ns_create_instances = '/nslcm/v1/ns_instances_content'

class HandlerOSM:
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

    def get_vnf_packages(self): # Query information about multiple VNF package resources
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # print(url)
        bearer = HandlerOSM.generate_nbi_token()
        headers.update(bearer)
        response = requests.get(endpoint, headers=headers)

        key_search = '_id'
        if key_search in response.json():
            value = response.json()[key_search]
            headers = {"Authorization": "Bearer " + value}
        return response.json()


    # Management operations of NS descriptors and packages
    def get_ns_packages(name): # Query information about multiple NS packages

        endpoint = PUBLIC_IP_OSM + endpoint_ns_packages

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        bearer = HandlerOSM.generate_nbi_token()
        headers.update(bearer)
        response = requests.get(endpoint, headers=headers)
        # print(response.json())
        for item in response.json():
            if item['name'] == name:
                value_id = item['_id']
                return value_id
        else:
            print("NS package not found!")
            return False

    # Management operations of NS instances
    def get_ns_instances(self):
        endpoint = PUBLIC_IP_OSM + endpoint_ns_instances

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # print(endpoint_ns_instances)
        bearer = HandlerOSM.generate_nbi_token()
        headers.update(bearer)
        response = requests.get(endpoint, headers=headers)
        return response.json()

    def get_vim_accounts(self):
        endpoint = PUBLIC_IP_OSM + endpoint_vim_accounts

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        # to generate bearer value
        bearer = HandlerOSM.generate_nbi_token()
        # update headers with bearer authentication
        headers.update(bearer)
        # response - GET method
        response = requests.get(endpoint, headers=headers)

        if response.status_code != 200:
            return False

        if response.status_code == 200:
            value_id = response.json()[0]["_id"]
            return value_id

    def post_vnf_packages(self, vnfd_data):
        '''Post a new VNFd content in JSON to OSM'''
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages_content
        print(endpoint)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        bearer = HandlerOSM.generate_nbi_token()
        headers.update(bearer)

        response = requests.request("POST", endpoint, headers=headers,
                                    data=vnfd_data)

        if response.status_code != 201:
            print("The operation cannot be executed!")
            return False

        if response.status_code == 201:
            print("Successfuly VNFd onboarding on Open Source Mano")
            key_search = 'id'
            if key_search in response.json():
                id_value = response.json()[key_search]
                return id_value

    def post_ns_package(self, nsd_data):
        # campos importantes
        # vnfd-id: referencia a VNFD antes implantada
        # virtual-link-profile-id: nome da rede existente no OpenStack

        '''Post a new VNFd content in JSON to OSM'''
        endpoint = PUBLIC_IP_OSM + enpoint_ns_packages_content

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        bearer = HandlerOSM.generate_nbi_token()

        headers.update(bearer)

        response = requests.request("POST", endpoint, headers=headers, data=nsd_data)

        if response.status_code != 201:
            print("The operation cannot be executed!")
            return False

        if response.status_code == 201:
            print("Successfuly NSd onboarding on Open Source Mano")
            key_search = 'id'
            if key_search in response.json():
                id_value = response.json()[key_search]
                return id_value

    def post_create_ns_instances(self, nsd_id, ns_name, ns_description, vim_account_id):
        # campos importantes
        # vnfd-id: referencia a VNFD antes implantada
        # virtual-link-profile-id: nome da rede existente no OpenStack

        '''Post a new VNFd content in JSON to OSM'''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_create_instances
        print(endpoint)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        # nsd_id = HandlerOSM.get_ns_packages('hackfest_basic-ns')
        #
        # vim_account_id = HandlerOSM.get_vim_accounts()

        payload = {
            "nsdId": nsd_id,
            "nsName": ns_name,
            "nsDescription": ns_description,
            "vimAccountId": vim_account_id
        }

        payload = json.dumps(payload)

        bearer = HandlerOSM.generate_nbi_token()

        headers.update(bearer)

        response = requests.request("POST", endpoint, headers=headers, data=payload)

        print(response.text)

        if response.status_code != 201:
            print("The operation cannot be executed!")

        if response.status_code == 201:
            print("Successfuly Instantiation!")

        return response
