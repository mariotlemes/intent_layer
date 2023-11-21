# intent_layer

[![Build Passing](https://img.shields.io/badge/build-passing-brightgreen)](link_do_seu_build)

### Description

---

This repository contains the development code
for intent layer software. 
Intent Layer has 3 modules:

**1)** ***intent_gui.py*** - GUI-based for intent expressing;

**2)** ***intent_engine*** - Convert intents into NILE;

**3)** ***intent_translator*** - convert NILE to suitable format (e.g., VNFd and NSd) and trigger network slice creation.

###  Architecture

---

![](fig/experimental-setup.png)

### Intent layer components workflow

---

![](fig/POC-basic.png)


### Requirements
Software and resources already available:

--- 
* python3.
* pip3.
* VM/Bare metal with [OSM](https://osm.etsi.org/).
* VM/Bare metal with [OpenStack](https://docs.openstack.org/devstack/latest/).

### How to install

---
**1)** Clone the repository:

```
cd ~
```
```
git clone https://github.com/mariotlemes/intent_layer.git
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

### How to RUN
intent-GUI:

```
python3 ~/intent_layer/intent_gui.py
```


