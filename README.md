# Intent Layer

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=plastic&logo=Qt&logoColor=white)

- [Description](#getting-started)
- [Architecture](#architecture)
- [Intent layer components workflow](#intent-layer-components-workflow)
- [Prerequisites](#prerequisites)
- [Features](#)
- [How to install](#installing)
- [How to run](#running)

## Getting started

This project contains the code
for intent layer software and instructions to run in top of
an NFV environment.
<mark>**`Intent Layer`**</mark> has 3 (three) main modules:

**1)** **`intentgui.py`**- GUI-based for intent expressing;

**2)** **`intent_engine.py`**- Convert intents into NILE (**N**etwork **I**ntent **L**anguag**E**);

**3)** **`intent_translator.py`**- Convert NILE to suitable format e.g., VNFd (Virtual Network Function Descriptor) and NSd (Network Service Descriptor), and trigger network slice creation;

Obs 1: `nile` and `utils` folders are provided by [Jacobs et al.](https://github.com/lumichatbot/webhook)

Obs 2: This project is inspirated in [B. Martini, M. Gharbaoui and P. Castoldi](https://dl.acm.org/doi/abs/10.1016/j.future.2022.12.033)

##  Architecture

![](fig/experimental-setup.png)

## Intent layer components workflow

![](fig/POC-basic.png)

## Prerequisites

- VM/Bare metal with [OSM](https://osm.etsi.org/) and ONOS controller. View the details to create an SDN controller inside
OSM [here](https://github.com/mariotlemes/intent_layer/wiki/How-to-integrate-an-SDN-controller).
- VM/Bare metal with [OpenStack](https://docs.openstack.org/devstack/latest/).

## Features description
All features are described [here](CHANGELOG.MD).

## Installing

**1)** Install python3-venv, git and qttools:
```
sudo apt install python3-venv -y
sudo apt install git -y
sudo apt install qttools5-dev-tools -y
```

**2)** Clone the repository:

```
cd ~ && git clone https://github.com/mariotlemes/intent_layer.git
```

**3)** Export the os environment IP_ADDRESS_OSM, where **A.B.C.D** represents the IPv4 address for OSM (Open
Source Mano):
```
export IP_ADDRESS_OSM="A.B.C.D"
```

**4)** Install requirements.txt:
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
python3 ~/intent_layer/intentgui.py
```
