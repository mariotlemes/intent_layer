from variables import GlobalVariables
import requests, os, yaml, json, descriptors_constructor

# IPv4 address OSM NBI
PUBLIC_IP_OSM = GlobalVariables.get_public_ip_osm()

# endpoints for OSM NBI resources
enpoint_generate_token = '/admin/v1/tokens'
endpoint_vnf_packages = '/vnfpkgm/v1/vnf_packages'
endpoint_vim_accounts = '/admin/v1/vim_accounts'
endpoint_ns_packages = '/nsd/v1/ns_descriptors'
endpoint_ns_instances = '/nslcm/v1/ns_instances'
endpoint_del_ns_instances = '/nslcm/v1/ns_instances'
# endpoint_vnf_packages_content =

def verify_osm_status():
    """Verify  OSM (Open Source Mano) status. """

    print("Trying to connect OSM NorthBound Interface ... \n")
    is_online = True
    # headers necessary to return suitable response
    headers = {"Accept": "application/json", "Content_Type": "application/json"}
    # endpoint for bearer authentication generation
    endpoint = PUBLIC_IP_OSM + enpoint_generate_token
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
    endpoint = PUBLIC_IP_OSM + enpoint_generate_token


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
    bearer = generate_nbi_token()
    headers.update(bearer)
    response = requests.get(endpoint, headers=headers)

    return response.json()


# Management operations of NS descriptors and packages
def get_ns_packages(): # Query information about multiple NS instances

    endpoint = PUBLIC_IP_OSM + endpoint_ns_packages

    headers = {"Accept": "application/json", "Content_Type": "application/json"}
    bearer = generate_nbi_token()
    headers.update(bearer)
    response = requests.get(endpoint, headers=headers)

    return response.json()

# Management operations of NS instances
def get_ns_instances():
    endpoint = PUBLIC_IP_OSM + endpoint_ns_instances


    headers = {"Accept": "application/json", "Content_Type": "application/json"}
    # print(endpoint_ns_instances)
    bearer = generate_nbi_token()
    headers.update(bearer)
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_vim_accounts():
    endpoint = PUBLIC_IP_OSM + endpoint_vim_accounts

    headers = {"Accept": "application/json", "Content_Type": "application/json"}
    # to generate bearer value
    bearer = generate_nbi_token()
    # update headers with bearer authentication
    headers.update(bearer)
    # response - GET method
    response = requests.get(endpoint, headers=headers)
    return response.json()

def post_vnf_packages():
    endpoint = PUBLIC_IP_OSM + endpoint_vnf_packages
    print(endpoint)

    # print(endpoint)
    # ajustando para enviar dados de um arquivo YAML

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    bearer = generate_nbi_token()
    headers.update(bearer)
    payload = '''
    vnfd:
  description: VNFD with 2 CPs to be used on Slice Testing
  df:
  - id: default-df
    instantiation-level:
    - id: default-instantiation-level
      vdu-level:
      - number-of-instances: 1
        vdu-id: ubuntu_slice-VM
    vdu-profile:
    - id: ubuntu_slice-VM
      min-number-of-instances: 1
  ext-cpd:
  - id: eth0-ext
    int-cpd:
      cpd: eth0-int
      vdu-id: ubuntu_slice-VM
  - id: eth1-ext
    int-cpd:
      cpd: eth1-int
      vdu-id: ubuntu_slice-VM
  id: slice_basic_vnf
  mgmt-cp: eth0-ext
  product-name: slice_basic_vnf
  provider: OSM
  sw-image-desc:
  - id: ubuntu18.04
    image: ubuntu18.04
    name: ubuntu18.04
  - id: ubuntu18.04-aws
    image: ubuntu/images/hvm-ssd/ubuntu-artful-17.10-amd64-server-20180509
    name: ubuntu18.04-aws
    vim-type: aws
  - id: ubuntu18.04-azure
    image: Canonical:UbuntuServer:18.04-LTS:latest
    name: ubuntu18.04-azure
    vim-type: azure
  - id: ubuntu18.04-gcp
    image: ubuntu-os-cloud:image-family:ubuntu-1804-lts
    name: ubuntu18.04-gcp
    vim-type: gcp
  vdu:
  - alternative-sw-image-desc:
    - ubuntu18.04-aws
    - ubuntu18.04-azure
    - ubuntu18.04-gcp
    cloud-init-file: cloud-config.txt
    description: ubuntu_slice-VM
    id: ubuntu_slice-VM
    int-cpd:
    - id: eth0-int
      virtual-network-interface-requirement:
      - name: eth0
        virtual-interface:
          bandwidth: 0
          type: VIRTIO
          vpci: 0000:00:0a.0
    - id: eth1-int
      virtual-network-interface-requirement:
      - name: eth1
        virtual-interface:
          bandwidth: 0
          type: VIRTIO
          vpci: 0000:00:0a.0
    name: ubuntu_slice-VM
    sw-image-desc: ubuntu18.04
    virtual-compute-desc: ubuntu_slice-VM-compute
    virtual-storage-desc:
    - ubuntu_slice-VM-storage
  version: 1.0
  virtual-compute-desc:
  - id: ubuntu_slice-VM-compute
    virtual-cpu:
      num-virtual-cpu: 1
    virtual-memory:
      size: 1.0
  virtual-storage-desc:
  - id: ubuntu_slice-VM-storage
    size-of-storage: 10
    '''
    # payload = descriptors_constructor.create_template_vnfd("slice_basic_vnf", 2)
    print(payload)

    payload = json.dumps(payload)



    response = requests.request("POST", endpoint, headers=headers,
                                data=payload)
    print(response.status_code)
    # # to restory id value
    # key_search = 'id'
    # if key_search in response.json():
    #     id_value = response.json()[key_search]
    #
    #  return id_value



