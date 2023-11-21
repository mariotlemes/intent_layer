import requests
import json
import connect_osm
from variables import GlobalVariables

def trigger_create_slice():
    url =  GlobalVariables.get_public_ip_osm() + '/nslcm/v1/ns_instances_content'
    print(url)

    '''TODO: Este request funciona. Verificar!'''
    payload = json.dumps({
        "nsdId": "4d2c0037-e568-42ce-9b8f-56f317000b07", # ns_slice_basic id
        "nsName": "New_Onboarding",
        "nsDescription": "default description",
        "vimAccountId": "424be87e-b91c-4dd9-97fa-f49adc355e6b" # openstack id
        # "netslice-vld": [{ "name": "slice_vld_mgmt", "vim-network-name": "public" }]
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # endpoint =  GlobalVariables.get_public_ip_osm() + '/nsilcm/v1/netslice_instances'

    # generate token for authentication
    bearer = connect_osm.generate_nbi_token()

    # update headers with bearer authentication token
    headers.update(bearer)

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    trigger_create_slice()

