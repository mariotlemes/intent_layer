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
    def create_template_ns():
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
                "vnfd-id": "slice_basic_vnf"
              }
            ]
          }
        ],
        "id": "hackfest_basic-ns",
        "name": "hackfest_basic-ns",
        "version": 1,
        "virtual-link-desc": [
          {
            "id": "mgmtnet",
            "mgmt-network": true
          }
        ],
        "vnfd-id": [
          "slice_basic_vnf"
        ]
      }
    ]
  }
}"""
        return nsd_data

    def create_template_vnfd(name_of_intent, number_vfs):
        '''Receive intent name and number of VFs and generate a JSON file
        of VNFD'''

        vnfd_data = """
                {
              "vnfd": {
                "description": "A basic VNF descriptor w/ one VDU",
                "df": [
                  {
                    "id": "default-df",
                    "instantiation-level": [
                      {
                        "id": "default-instantiation-level",
                        "vdu-level": [
                          {
                            "number-of-instances": 1,
                            "vdu-id": "hackfest_basic-VM"
                          }
                        ]
                      }
                    ],
                    "vdu-profile": [
                      {
                        "id": "hackfest_basic-VM",
                        "min-number-of-instances": 1
                      }
                    ]
                  }
                ],
                "ext-cpd": [
                  {
                    "id": "vnf-cp0-ext",
                    "int-cpd": {
                      "cpd": "vdu-eth0-int",
                      "vdu-id": "hackfest_basic-VM"
                    }
                  }
                ],
                "id": "teste2",
                "mgmt-cp": "vnf-cp0-ext",
                "product-name": "MARIO-TESTE-S",
                "sw-image-desc": [
                  {
                    "id": "ubuntu20.04",
                    "image": "ubuntu20.04",
                    "name": "ubuntu20.04"
                  },
                  {
                    "id": "ubuntu20.04-aws",
                    "name": "ubuntu20.04-aws",
                    "image": "ubuntu/images/hvm-ssd/ubuntu-artful-17.10-amd64-server-20180509",
                    "vim-type": "aws"
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
                ],
                "vdu": [
                  {
                    "id": "hackfest_basic-VM",
                    "name": "hackfest_basic-VM",
                    "sw-image-desc": "ubuntu20.04",
                    "alternative-sw-image-desc": [
                      "ubuntu20.04-aws",
                      "ubuntu20.04-azure",
                      "ubuntu20.04-gcp"
                    ],
                    "virtual-compute-desc": "hackfest_basic-VM-compute",
                    "virtual-storage-desc": [
                      "hackfest_basic-VM-storage"
                    ],
                    "int-cpd": [
                      {
                        "id": "vdu-eth0-int",
                        "virtual-network-interface-requirement": [
                          {
                            "name": "vdu-eth0",
                            "virtual-interface": {
                              "type": "PARAVIRT"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ],
                "version": 1,
                "virtual-compute-desc": [
                  {
                    "id": "hackfest_basic-VM-compute",
                    "virtual-cpu": {
                      "num-virtual-cpu": 1
                    },
                    "virtual-memory": {
                      "size": 1
                    }
                  }
                ],
                "virtual-storage-desc": [
                  {
                    "id": "hackfest_basic-VM-storage",
                    "size-of-storage": 10
                  }
                ]
              }
            }"""

        # 2o - carregar o conteúdo em YAML para um dicionário PYTHON
        vnfd_dict = json.loads(vnfd_data)

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

        # print(json_pos_operation)

        return json_pos_operation





# vnfd (caracteristicas das funções)
# DF deployment flavour profile - requisitos de capacidade e performance
# VDU (Virtual Deployment Unit)) - representa uma VM individual dentro de uma VNF
# ext-cpd (external-connection point descriptor) - especifica caracteristicas de
# um ou mais pontos de conexão externos expostos pela função de rede

# 1o - conteúdo padrão da VNFD em YAML


