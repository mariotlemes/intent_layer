from variables import GlobalVariables
import requests
import json
import yaml
import time

# IPv4 address for OSM NBI
PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()

# Endpoints for OSM NBI resources
endpoint_generate_token = '/admin/v1/tokens'
endpoint_vnf_package = '/vnfpkgm/v1/vnf_packages'
endpoint_vim_account = '/admin/v1/vim_accounts'
endpoint_ns_package = '/nsd/v1/ns_descriptors'
endpoint_ns_instance = '/nslcm/v1/ns_instances'
endpoint_vnf_package_content = '/vnfpkgm/v1/vnf_packages_content'
endpoint_ns_package_content = '/nsd/v1/ns_descriptors_content'
endpoint_ns_create_instance = '/nslcm/v1/ns_instances'
endpoint_create_subscription = '/nslcm/v1/subscriptions'
endpoint_occurrences = '/nslcm/v1/ns_lcm_op_occs/'

class HandlerOSM:
    """This class provides methods to interact with the OSM REST interface"""
    def get_ns_lcmp_op_occs(self, ns_instance_id):
        '''
        This method verify the status of network instance. It is used to safed delete.
        :param ns_instance_id: network instance id
        :return: true or false
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_occurrences + ns_instance_id
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            status = False
            while (status == False):
                response = requests.get(endpoint, headers=headers)
                # ns - blank
                if (response.status_code == 404):
                    status = True
                    return status

                response = response.json()

                if ((response['operationState'] == "COMPLETED"
                        and response['_id'] == ns_instance_id) or
                        (response['nsInstanceId'] == ns_instance_id)):
                    status = True
                    return status
                else:
                    status = False
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    """Verify OSM (Open Source Mano) status. """
    def verify_osm_status(self):
        '''
        This method checks OMS status (online/offline)
        :return: true (ON) or false (OFF)
        '''
        print("------------------------------------------------------------------------------")
        print(f"              Connecting to OSM NBI ({PUBLIC_IP_OSM})                        ")
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        endpoint = PUBLIC_IP_OSM + endpoint_generate_token

        try:
            # send a POST request to generate token
            requests.post(endpoint, headers=headers,
                          json={"username": "admin",
                                "password": "admin"})
            print("\nRESULT: Connected to OSM NBI.")
            return True
        except requests.Timeout:
            print("\nRESULT: Timeout! OSM is probably down...")
            return False
        except requests.RequestException as error:
            print("Error:", error)
            return False

    def generate_nbi_token(self):
        '''
        This method generates a NBI bearer token for API Rest authorization
        :return: bearer token ID
        '''
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

    def get_vim_account(self):
        '''
        This method gets a ID list of virtual infrastructure managers
        :return: list (ID)
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_vim_account
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

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

    def get_vnf_package(self):
        '''
        This method gets a list (ID) of Virtual Network Function Descriptors
        :return: list (ID)
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_package
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            value_id = []
            response = requests.get(endpoint, headers=headers)
            for item in response.json():
                if "_id" in item:
                    value_id.append(item['_id'])
            return value_id
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def get_ns_instance(self):
        '''
        This method gets a list (ID) of Network Service Instances
        :return: list (ID)
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_instance
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            value_id = []
            response = requests.get(endpoint, headers=headers)
            # print(response.json())
            for item in response.json():
                if "_id" in item:
                    value_id.append(item['_id'])
            return value_id
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def get_ns_instance_by_name(self, name):
        '''
        This method gets ID of Network Service Instance using the name
        :param name: name of instance
        :return: ID of instance
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_instance
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)
            for item in response.json():
                if item['name'] == name:
                    value_id = item['_id']
                    return value_id
            else:
                print(f"NS instance (name: {name}) not exist!")
                return False
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def get_ns_package(self):
        '''
        This method gets a list (ID) of Network Service Descriptors
        :return: list (ID) of nsd
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_package
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)
            value_id = []
            for item in response.json():
                if "_id" in item:
                    value_id.append(item['_id'])
            return value_id
                # else:
                #     print("NS package not found!")
                #     return False
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def get_ns_package_by_name(self, name):
        '''
        This method gets ID of Network Service Descriptor using the name
        :param name: name of nsd
        :return: ID of nsd
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_package
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            response = requests.get(endpoint, headers=headers)
            for item in response.json():
                if item['name'] == name:
                    value_id = item['_id']
                    # print(value_id)
                    return value_id
            else:
                print("NS package not found!")
                return False
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_ns_instance_create_and_instantiate(self, nsd_id, ns_name, ns_description):
        '''
        This method creates and instantiates a network service
        :param nsd_id: id of network service descriptor
        :param ns_name: network service nane
        :param ns_description: network service description
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_create_instance
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        nsd_id = self.get_ns_package_by_name(nsd_id)

        vim_account_id = HandlerOSM()

        payload = json.dumps({
            "nsdId": nsd_id,
            "nsName": ns_name,
            "nsDescription": ns_description,
            "vimAccountId": vim_account_id.get_vim_account(),
            "lcmOperationType": "NsLcmOperationOccurrenceNotification"
        })

        try:
            response = requests.request("POST", endpoint, headers=headers, data=payload)
            if response.status_code != 201:
                response = response.json()
                print(f"NS ID: {ns_name}")
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}\n")
            else:
                response = response.json()
                print(f"NS ID: {ns_name}")
                print(f"Code: 201 (SUCCESS)")
                print(f"ID: {response['id']}\n")
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

        # id = HandlerOSM()
        endpoint_instantiate = (PUBLIC_IP_OSM + endpoint_ns_instance +
                    "/" + self.get_ns_instance_by_name('nsd_instance') + "/instantiate")

        print(f"Instantiating: {self.get_ns_instance_by_name('nsd_instance')}")

        try:
            response = requests.request("POST", endpoint_instantiate, headers=headers, data=payload)
            if response.status_code != 202:
                response = response.json()
                # return response['id']
            else:
                response = response.json()
                # print(response)
                return response['id']
                # print(response)
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_vnf_package(self, data):
        '''
        This method creates a VNF descriptor package in OSM
        :param data: YAML descriptor
        :return: ID of created VNF or False if not created
        '''
        '''Post a new VNFd content in JSON to OSM'''
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_package_content
        # print(endpoint)
        # print(endpoint)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        headers.update(self.generate_nbi_token())

        vnfd_data = json.dumps(data)

        vnfd_name = data['vnfd']['id']


        try:
            response = requests.request("POST", endpoint, headers=headers,
                                        data=vnfd_data)
            if response.status_code != 201:
                response = response.json()
                print(f"VNFd ID: {vnfd_name}")
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}\n")
                return False
            else:
                response = response.json()
                # print(f"VNFd ID: {vnfd_name}")
                print(f"Code: 201 (SUCCESS)")
                print(f"ID: {response['id']}\n")
                key_search = 'id'
                if key_search in response:
                    id_value = response[key_search]
                    return id_value
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_create_vnf_package(self):
        """Post a new descriptors content in YAML to OSM"""
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_package
        print(endpoint)
        headers = {"Accept": "application/json", "Content_Type": "application/json"}

        headers.update(self.generate_nbi_token())

        response = requests.request("POST", endpoint, headers=headers)

        response = response.json()

        vnfd_id = response['id']

        # print(teste)

        return vnfd_id

    # def put_vnf_package(self, vnfpkg_id, vnfpkg_data):
    def put_vnf_package(self, vnfd_id):
        with open('descriptors/test1/basic_VNF1d.yaml', 'r') as file:
            data = yaml.safe_load(file)
            # print(data)

        payload = json.dumps(
            data, indent=2
        )

        print(payload)
        #
        # print(dados_json)

        endpoint = PUBLIC_IP_OSM + endpoint_vnf_package + '/' + vnfd_id + '/package_content/'
        print(endpoint)

        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        response = requests.request("PUT", endpoint, headers=headers, data=payload)

        print(response.text)

        print(response.status_code)

    def post_ns_package(self, data):
        '''
        This method creates a network service descriptor package in OSM
        :param data: nsd in YAML
        :return: the ID of NS package or False if not created
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_package_content

        # print(endpoint)

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        headers.update(self.generate_nbi_token())

        nsd_data = json.dumps(data)

        nsd_name = data['nsd']['nsd'][0]['id']

        try:
            response = requests.request("POST", endpoint, headers=headers, data=nsd_data)

            if response.status_code != 201:
                response = response.json()
                print(f"NSd ID: {nsd_name}")
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}")
                return False
            else:
                response = response.json()
                print(f"NSd ID: {nsd_name}")
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

    def post_ns_subscription(self, id):
        '''
        This method creates a new subscription to receive notifications about a network service
        :param id: resource ID
        :return: subscription ID
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_create_subscription
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        payload = json.dumps({
                "filter": {
                    "NsInstanceSubscriptionFilter": {
                        "nsInstanceIds": [
                            id
                        ]
                    },
                    "notificationTypes": [
                        "NsChangeNotification"
                    ],

                    "nsComponentTypes" : [

                    ],
                },
                "CallbackUri": "http://35.199.94.95:5400/notifications"
            })

        try:
            response = requests.request("POST", endpoint, headers=headers, data=payload)
            if response.status_code != 201:
                response = response.json()
                print(f"Code: {response['status']} ({response['code']})")
                print(f"Detail: {response['detail']}")
            else:
                response = response.json()
                print(f"Code: 201 (SUCCESS)")
                print(f"ID of subscription: {response['id']}")
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def post_ns_instance_terminate(self, ns_instance_id):
        '''
        This method terminates a network service instance
        :param ns_instance_id: network instance ID
        :return: True if success
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_create_instance + '/' + ns_instance_id + '/' + 'terminate'
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            status = False
            print("Terminating proccess (wait): ", end="")
            while (status == False):
                response = requests.request("POST", endpoint, headers=headers)
                # print(response.status_code)
                if(response.status_code) != 409:
                    response = response.json()
                    id = response['id']
                    if (self.get_ns_lcmp_op_occs(id)):
                        status = True
                        return status
                    else:
                        return status
                else:
                    status = True
                    return status
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def del_ns_instace(self, ns_instance_id):
        '''
        This method deletes a network service instance
        :param ns_instance_id: network service instance ID
        '''
        endpoint_delete = PUBLIC_IP_OSM + endpoint_ns_create_instance + "/" + ns_instance_id + "/"
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        response = requests.request("DELETE", endpoint_delete, headers=headers)
        try:
            if response.status_code != 204:
                print("Not deleting..")
            else:
                print("Delete successfull!")
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def del_vnf_package(self, vnf_package_id):
        '''
        This method deletes a virtual network function descriptor
        :param vnf_package_id: virtual network function ID
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_package + "/" + vnf_package_id + "/"
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        response = requests.request("DELETE", endpoint, headers=headers)
        try:
            if response.status_code != 204:
                print("Not deleting..")
            else:
                print("Delete successfull!")
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def del_ns_package(self, ns_package_id):
        '''
        This method deletes a network service descriptor
        :param ns_package_id: network service descriptor ID
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_ns_package + "/" + ns_package_id + "/"
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        response = requests.request("DELETE", endpoint, headers=headers)
        try:
            if response.status_code != 204:
                print("Not deleting..")
            else:
                print("Delete successfull!")
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def del_vnf_packages(self, vnfPkgId):
        '''
        This method deletes a virtual network function descriptor
        :param vnfPkgId: virtual network function descriptor ID
        '''
        endpoint = PUBLIC_IP_OSM + endpoint_vnf_package + '/' + vnfPkgId
        headers = {"Accept": "application/json", "Content_Type": "application/json"}
        headers.update(self.generate_nbi_token())

        try:
            response = requests.request("DELETE", endpoint, headers=headers)
            if response.status_code != 204:
                print("Not deleting..")
            else:
                print("Delete successfull!")
                response = response.json()
        except requests.Timeout as timeout:
            print("Timeout:", timeout)
        except requests.RequestException as error:
            print("Error:", error)

    def clean_environment(self):
        '''
        This function perfom a clean environment in OSM, i.e., deletes all VNFd, NSD, and network instances
        '''
        qtnsi = len(self.get_ns_instance())
        qtnsd = len(self.get_ns_package())
        qtvnfd = len(self.get_vnf_package())

        if (not self.get_ns_instance() and
                not self.get_vnf_package()
                and not self.get_ns_package()):
            print("Nothing to clean!!")

        # to clean all network service instances
        if (len(self.get_ns_instance()) > 0):
            for pos, ns_instance_id in enumerate(self.get_ns_instance(), start=1):
                    print(f"Cleanning network instances ({pos}/{qtnsi}): ", end="")
                    if self.get_ns_lcmp_op_occs(ns_instance_id):
                        id_terminate = self.post_ns_instance_terminate(ns_instance_id)
                        if id_terminate:
                            self.del_ns_instace(ns_instance_id)

        # to clean all nsd - descriptors
        if (len(self.get_ns_package()) > 0):
            for pos, nsd_descriptor in enumerate(self.get_ns_package(), start=1):
                    print(f"Cleanning NS descriptors ({pos}/{qtnsd}): ", end="")
                    self.del_ns_package(nsd_descriptor)

        # to clean all vnfd - descriptors
        if (len(self.get_vnf_package()) > 0):
            for pos, vnfd_descritor in enumerate(self.get_vnf_package(), start=1):
                    print(f"Cleanning VNF descriptors ({pos}/{qtvnfd}): ", end="")
                    self.del_vnf_package(vnfd_descritor)