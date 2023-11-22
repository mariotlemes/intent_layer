import yaml, tarfile, gzip, os, json
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
def create_template_ns():
    '''TODO: Criar um dicionario de TEMPLATE para os descriptores de serviços da rede (NSd)'''
    pass

def create_template_vnfd(name_of_intent, number_vfs):
    '''Receive intent name and number of VFs and generate a JSON file
    of VNFD'''

    # vnfd (caracteristicas das funções)
    # DF deployment flavour profile - requisitos de capacidade e performance
    # VDU (Virtual Deployment Unit)) - representa uma VM individual dentro de uma VNF
    # ext-cpd (external-connection point descriptor) - especifica caracteristicas de
    # um ou mais pontos de conexão externos expostos pela função de rede

    # 1o - conteúdo padrão da VNFD em YAML
    yaml_content = \
'''vnfd:
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
    name: ubuntu18.04-aws
    image: ubuntu/images/hvm-ssd/ubuntu-artful-17.10-amd64-server-20180509
    vim-type: aws
  - id: ubuntu18.04-azure
    name: ubuntu18.04-azure
    image: Canonical:UbuntuServer:18.04-LTS:latest
    vim-type: azure
  - id: ubuntu18.04-gcp
    name: ubuntu18.04-gcp
    image: ubuntu-os-cloud:image-family:ubuntu-1804-lts
    vim-type: gcp
  vdu:
  - cloud-init-file: cloud-config.txt
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
    alternative-sw-image-desc:
    - ubuntu18.04-aws
    - ubuntu18.04-azure
    - ubuntu18.04-gcp
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
    size-of-storage: 10'''
    # 2o - carregar o conteúdo em YAML para um dicionário PYTHON
    vnfd_dict = yaml.safe_load(yaml_content)

    if 'vnfd' in vnfd_dict and 'df' in vnfd_dict['vnfd']:
        vnfd_dict['vnfd']['id'] = name_of_intent
        vnfd_dict['vnfd']['product-name'] = name_of_intent
        vnfd_dict['vnfd']['df'][0]['instantiation-level'][0]['vdu-level'][0]['number-of-instances'] = 5

    # 3º converter dicionario em yaml
    yaml_str = yaml.dump(vnfd_dict, default_flow_style=False,
                         width=float("inf"))

    # remove the last line white line if exists
    if yaml_str.endswith('\n'):
        yaml_str = yaml_str[:-1]

    data = yaml.safe_load(yaml_str)

    data_json = json.dumps(data, indent=2)

    # print(data_json)
    return data_json

if __name__ == '__main__':

    create_template_vnfd('slice_basic_vnf', 4)

    # print(conteudo)





