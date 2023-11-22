# Intent Layer

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=plastic&logo=Qt&logoColor=white)

- [Description](#getting-started)
- [Architecture](#architecture)
- [Intent layer components workflow](#intent-layer-components-workflow)
- [Prerequisites](#prerequisites)
- [How to install](#installing)
- [How to run](#running)

## Getting started

This project contains the code
for intent layer software (src directory) and instructions to run in top of
an NFV environment.
<mark>**`Intent Layer`**</mark> has 3 (three) main modules:


**1)** **`intent_gui.py`**- GUI-based for intent expressing;

**2)** **`intent_engine.py`**- Convert intents into NILE (**N**etwork **I**ntent **L**anguag**E**);

**3)** **`intent_translator.py`**- Convert NILE to suitable format e.g., VNFd (Virtual Network Function Descriptor) and NSd (Network Service Descriptor), and trigger network slice creation;

Obs: `nile` and `utils` folders are provided by [Jacobs et al.](https://github.com/lumichatbot/webhook)

##  Architecture

![](fig/experimental-setup.png)

## Intent layer components workflow

![](fig/POC-basic.png)

## Prerequisites

- python3. 
- pip3. 
- VM/Bare metal with [OSM](https://osm.etsi.org/). 
- VM/Bare metal with [OpenStack](https://docs.openstack.org/devstack/latest/).

## Installing

**1)** Clone the repository:

```
cd ~ && git clone https://github.com/mariotlemes/intent_layer.git
```

**2)** Export the os environment IP_ADDRESS_OSM, where **A.B.C.D** represents the IPv4 address for OSM (Open
Source Mano):
```
export IP_ADDRESS_OSM="A.B.C.D"
```

**3)** Install requirements.txt:
```
cd ~/intent_layer
```

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install --upgrade pip
```

```
pip3 install -r requirements.txt
```

## Running

**1)** intent-GUI:

```
python3 ~/intent_layer/intent_gui.py
```
