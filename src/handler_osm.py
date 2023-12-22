from variables import GlobalVariables
import requests
import json, yaml

# IPv4 address for OSM NBI
PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()

# Endpoints for OSM NBI resources
endpoint_generate_token = '/admin/v1/tokens'
endpoint_vnf_packages = '/vnfpkgm/v1/vnf_packages'
endpoint_vim_accounts = '/admin/v1/vim_accounts'
endpoint_ns_packages = '/nsd/v1/ns_descriptors'
endpoint_ns_instances = '/nslcm/v1/ns_instances'
endpoint_del_ns_instances = '/nslcm/v1/ns_instances'
endpoint_vnf_packages_content = '/vnfpkgm/v1/vnf_packages_content'
endpoint_ns_packages_content = '/nsd/v1/ns_descriptors_content'
endpoint_ns_create_instances = '/nslcm/v1/ns_instances_content'
endpoint_create_new_subscription = '/nslcm/v1/subscriptions'

class HandlerOSM:
    """This class provides methods to interact with the OSM REST interface"""
    def get_vim_accounts(self):
        endpoint = PUBLIC_IP_OSM + endpoint_vim_accounts
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)

            if response.status_code != 200:
                return False

            if response.status_code == 200:
                value_id = response.json()[0]["_id"]
                return value_id
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def verify_osm_status(self):
        """Verify  OSM (Open Source Mano) status. """
        print(f"Trying to connect OSM NBI - {PUBLIC_IP_OSM} -")
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        endpoint = PUBLIC_IP_OSM + endpoint_generate_token

        try:
            # send a POST request to generate token
            requests.post(endpoint, headers=headers,
                          json={"username": "admin",
                                "password": "admin"})
            print("Connected!")
            return True
        except requests.Timeout:
            print("Timeout! OSM is probably down...")
            return False
        except requests.RequestException as error:
            print("Error:", error)
            return False

    def get_vnf_packages(self):
        """Query information about multiple VNF package resources"""
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)
            key_search = '_id'
            if key_search in response.json():
                value = response.json()[key_search]
                headers = {"Authorization": "Bearer " + value}
            return response.json()
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def get_ns_instances(self, name):
        endpoint = PUBLIC_IP_OSM + endpoint_ns_instances
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)
            for item in response.json():
                if item['name'] == name:
                    value_id = item['_id']
                    return value_id
            else:
                print("NS instance not found!")
                return False
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def generate_nbi_token(self):
        """Generate token for NBI authentication"""
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        endpoint = PUBLIC_IP_OSM + endpoint_generate_token

        try:
            response = requests.post(endpoint, headers=headers,
                                     json={"username": "admin", "password": "admin"})

            # to restore the bearer authentication
            key_search = 'id'
            if key_search in response.json():
                value = response.json()[key_search]
                headers = {"Authorization": "Bearer " + value}
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)
        return headers

    def get_ns_packages(self, name):
        """Query information about multiple NS packages"""

        endpoint = PUBLIC_IP_OSM + endpoint_ns_packages
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)
            for item in response.json():
                if item['name'] == name:
                    value_id = item['_id']
                    return value_id
            else:
                print("NS package not found!")
                return False
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_ns_instance(self, nsd_id, ns_name, ns_description):
        '''Post a new descriptors content (JSON object) to OSM'''

        # vnfd-id: references a VNFD
        endpoint = PUBLIC_IP_OSM + endpoint_ns_create_instances
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        nsd_id = HandlerOSM()
        vim_account_id = HandlerOSM()

        payload = json.dumps({
            "nsdId": nsd_id.get_ns_packages('nsd'),
            "nsName": ns_name,
            "nsDescription": ns_description,
            "vimAccountId": vim_account_id.get_vim_accounts()
        })

        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        try:
            response = requests.request("POST", endpoint, headers=headers, data=payload)
            if response.status_code != 201:
                response = response.json()
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}")
                return False
            else:
                response = response.json()
                print(f"Code: 201 (SUCCESS)")
                print(f"ID: {response['id']}")

        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_vnf_packages(self, vnfd_data):
        """Post a new descriptors content in YAML to OSM"""
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages_content

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        # transform vnfd_data to JSON
        data = json.dumps(vnfd_data)

        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        response = requests.request("POST", endpoint, headers=headers,
                                    data=data)
        try:
            if response.status_code != 201:
                response = response.json()
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}")
                return False
            else:
                response = response.json()
                print(f"Code: 201 (SUCCESS)")
                print(f"ID: {response['id']}")
                key_search = 'id'
                if key_search in response:
                    id_value = response[key_search]
                    return id_value
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_ns_package(self, nsd_data):
        """Post a new descriptors content in JSON to OSM"""
        endpoint = PUBLIC_IP_OSM + endpoint_ns_packages_content

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        data = json.dumps(nsd_data)

        bearer = HandlerOSM()
        headers.update(bearer.generate_nbi_token())

        try:
            response = requests.request("POST", endpoint, headers=headers, data=data)
            print(response.status_code)

            if response.status_code != 201:
                response = response.json()
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}")
                return False
            else:
                response = response.json()
                print(f"Code: 201 (SUCCESS)")
                print(f"ID: {response['id']}")
                key_search = 'id'
                if key_search in response:
                    id_value = response[key_search]
                    return id_value
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)
    def post_create_new_subscription(self, name):
        '''Create a new subscription to receive notifications about a NSd.
        The input is the name of resource and the output is the subscription ID'''
        endpoint = PUBLIC_IP_OSM + endpoint_create_new_subscription

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        bearer = HandlerOSM()
        nsd_instance = HandlerOSM()

        headers.update(bearer.generate_nbi_token())

        payload = json.dumps({
                "filter": {
                    "nsInstanceSubscriptionFilter": {
                        "nsdIds": [
                            nsd_instance.get_ns_instances(name)
                        ]
                    },
                    "notificationTypes": [
                        "NsLcmOperationOccurrenceNotification"
                    ],
                    "operationTypes": [
                        "INSTANTIATE",
                        "TERMINATE"
                    ],
                    "operationStates": [
                        "PROCESSING",
                        "COMPLETED",
                        "FAILED"
                    ]
                },
                "CallbackUri": "http://189.63.44.102:5400/notifications"
            })

        try:
            response = requests.request("POST", endpoint, headers=headers, data=payload)
            if response.status_code != 201:
                print("The operation cannot be executed!")
                print(response.status_code)
            else:
                print("Subscription is successfully!")
                # print(response.json())
                key_search = 'id'
                if key_search in response.json():
                    id_value = response.json()[key_search]
                    return id_value
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)