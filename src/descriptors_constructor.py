import yaml, tarfile, gzip, os, json, io
import handler_osm
'''
NFs, throghput, topology

https://codilime.com/blog/how-to-configure-vnfs-using-a-virtual-network-function-descriptor/
Folder structure to VNFD template (https://osm-download.etsi.org/ftp/osm-doc/etsi-nfv-vnfd.html#):
cloud_init_example_VNF/
    vnfd.yaml #options to deploy an instance in OpenStack
    cloud_init/
        cloud_init.cfg
Reference: https://osm-download.etsi.org/ftp/osm-doc/etsi-nfv-vnfd.html#
'''
class DescriptorConstrutor:
    '''Create a template for network service'''
    def create_template_ns(self):
        nsd_data = """
        {
  "nsd": {
    "nsd": [
      {
        "description": "Simple NS with a single VNF and a single VL",
        "df": [
          {
            "id": "default-df",
            "vnf-profile": [
              {
                "id": "vnf",
                "virtual-link-connectivity": [
                  {
                    "constituent-cpd-id": [
                      {
                        "constituent-base-element-id": "vnf",
                        "constituent-cpd-id": "vnf-cp0-ext"
                      }
                    ],
                    "virtual-link-profile-id": "mgmtnet"
                  }
                ],
                "vnfd-id": "simple_3vm-vnf"
              }
            ]
          }
        ],
        "id": "simple_3vm-ns",
        "name": "simple_3vm-ns",
        "version": 1,
        "virtual-link-desc": [
          {
            "id": "mgmtnet",
            "mgmt-network": true
          }
        ],
        "vnfd-id": [
          "simple_3vm-vnf"
        ]
      }
    ]
  }
}"""
        return nsd_data

    def create_template_vnfd(self, name_of_intent, number_vfs):
        '''Receive intent name and number of VFs and generate a JSON file
        of VNFD'''

        vnfd_data = """{
  "vnfd": {
    "description": "A VNFD consisting of 3 VDUs (VMs) connected to an internal VL (with bitrate-requirement - 10MB) and a cloud-init configuration",
    "id": "simple_3vm-vnf",
    "product-name": "simple_3vm-vnf",
    "vdu": [
      {
        "id": "VM1",
        "name": "VM1",
        "int-cpd": [
          {
            "id": "VM1-eth0-int",
            "virtual-network-interface-requirement": [
              {
                "name": "VM1-eth0",
                "position": 1,
                "virtual-interface": {
                  "type": "PARAVIRT"
                }
              }
            ]
          },
          {
            "id": "VM1-eth1-int",
            "int-virtual-link-desc": "internal",
            "virtual-network-interface-requirement": [
              {
                "name": "VM1-eth1",
                "position": 2,
                "virtual-interface": {
                  "type": "PARAVIRT"
                }
              }
            ],
            "bitrate-requirement": 5000
          }
        ],
        "sw-image-desc": "ubuntu20.04",
        "alternative-sw-image-desc": [
          "ubuntu20.04-azure",
          "ubuntu20.04-gcp"
        ],
        "virtual-compute-desc": "VM1-compute",
        "virtual-storage-desc": [
          "VM1-storage"
        ]
      },
      {
        "id": "VM2",
        "name": "VM2",
        "int-cpd": [
          {
            "id": "VM2-eth0-int",
            "int-virtual-link-desc": "internal",
            "virtual-network-interface-requirement": [
              {
                "name": "VM2-eth0",
                "position": 1,
                "virtual-interface": {
                  "type": "PARAVIRT"
                }
              }
            ],
            "bitrate-requirement": 5000
          }
        ],
        "sw-image-desc": "ubuntu20.04",
        "alternative-sw-image-desc": [
          "ubuntu20.04-azure",
          "ubuntu20.04-gcp"
        ],
        "virtual-compute-desc": "VM2-compute",
        "virtual-storage-desc": [
          "VM2-storage"
        ]
      },
      {
        "id": "VM3",
        "name": "VM3",
        "int-cpd": [
          {
            "id": "VM3-eth0-int",
            "int-virtual-link-desc": "internal",
            "virtual-network-interface-requirement": [
              {
                "name": "VM3-eth0",
                "position": 1,
                "virtual-interface": {
                  "type": "PARAVIRT"
                }
              }
            ],
            "bitrate-requirement": 5000
          }
        ],
        "sw-image-desc": "ubuntu20.04",
        "alternative-sw-image-desc": [
          "ubuntu20.04-azure",
          "ubuntu20.04-gcp"
        ],
        "virtual-compute-desc": "VM3-compute",
        "virtual-storage-desc": [
          "VM3-storage"
        ]
      }
    ],
    "version": 1,
    "virtual-compute-desc": [
      {
        "id": "VM1-compute",
        "virtual-memory": {
          "size": 2572
        },
        "virtual-cpu": {
          "num-virtual-cpu": 2
        }
      },
      {
        "id": "VM2-compute",
        "virtual-memory": {
          "size": 512
        },
        "virtual-cpu": {
          "num-virtual-cpu": 1
        }
      },
      {
        "id": "VM3-compute",
        "virtual-memory": {
          "size": 512
        },
        "virtual-cpu": {
          "num-virtual-cpu": 1
        }
      }
    ],
    "virtual-storage-desc": [
      {
        "id": "VM1-storage",
        "size-of-storage": 20
      },
      {
        "id": "VM2-storage",
        "size-of-storage": 10
      },
      {
        "id": "VM3-storage",
        "size-of-storage": 10
      }
    ],
    "df": [
      {
        "id": "default-df",
        "instantiation-level": [
          {
            "id": "default-instantiation-level",
            "vdu-level": [
              {
                "number-of-instances": 1,
                "vdu-id": "VM1"
              },
              {
                "number-of-instances": 1,
                "vdu-id": "VM2"
              },
              {
                "number-of-instances": 1,
                "vdu-id": "VM3"
              }
            ]
          }
        ],
        "vdu-profile": [
          {
            "id": "VM1",
            "min-number-of-instances": 1
          },
          {
            "id": "VM2",
            "min-number-of-instances": 1
          },
          {
            "id": "VM3",
            "min-number-of-instances": 1
          }
        ]
      }
    ],
    "ext-cpd": [
      {
        "id": "vnf-mgmt-ext",
        "int-cpd": {
          "cpd": "VM1-eth0-int",
          "vdu-id": "VM1"
        }
      }
    ],
    "int-virtual-link-desc": [
      {
        "id": "internal"
      }
    ],
    "mgmt-cp": "vnf-mgmt-ext",
    "sw-image-desc": [
      {
        "id": "ubuntu20.04",
        "image": "ubuntu20.04",
        "name": "ubuntu20.04"
      },
      {
        "id": "ubuntu20.04-azure",
        "name": "ubuntu20.04-azure",
        "image": "Canonical:0001-com-ubuntu-server-focal:20_04-lts:latest",
        "vim-type": "azure"
      },
      {
        "id": "ubuntu20.04-gcp",
        "name": "ubuntu20.04-gcp",
        "image": "ubuntu-os-cloud:image-family:ubuntu-2004-lts",
        "vim-type": "gcp"
      }
    ]
  }
}"""

        # 2o - carregar o conteúdo em YAML para um dicionário PYTHON
        vnfd_dict = json.loads(vnfd_data)

        # vnf = yaml.safe_load(vnfd_data)

        print(vnfd_dict)

        value_id = vnfd_dict['vnfd']['id']
        print(value_id)

        try:
            if 'vnfd' in vnfd_dict and 'df' in vnfd_dict['vnfd']:
                vnfd_dict['vnfd']['id'] = name_of_intent
                vnfd_dict['vnfd']['product-name'] = name_of_intent
                vnfd_dict['vnfd']['df'][0]['instantiation-level'][0]['vdu-level'][0]['number-of-instances'] = number_vfs
        except KeyError:
            print("The key not exists!.")
        except Exception as e:
            print("Error:", e)

        #return to json
        json_pos_operation = json.dumps(vnfd_dict, indent=2)

        print(json_pos_operation)

        return json_pos_operation


# vnfd (caracteristicas das funções)
# DF deployment flavour profile - requisitos de capacidade e performance
# VDU (Virtual Deployment Unit)) - representa uma VM individual dentro de uma VNF
# ext-cpd (external-connection point descriptor) - especifica caracteristicas de
# um ou mais pontos de conexão externos expostos pela função de rede

# 1o - conteúdo padrão da VNFD em YAML

if __name__ == '__main__':
    vnfd = DescriptorConstrutor()
    vnfd.create_template_vnfd("teste", 2)

