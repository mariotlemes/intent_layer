# intent_layer

[![Build Passing](https://img.shields.io/badge/build-passing-brightgreen)](link_do_seu_build)

### Description

---

This repository contains the development code
for intent layer software. 
Intent Layer has 3 modules:

**i)** intent_gui.py - Intent Expressing;

**ii)** intent_engine - to convert intents into NILE;

**iii)** intent_translator - convert NILE to VNFd and trigger network slice creation.


### How to install

---
**1)** Export the os environment IP_ADDRESS_OSM, where A.B.C.D represents the IPv4 address for OSM (Open
Source Mano)
```
export IP_ADDRESS_OSM="A.B.C.D"
```
**2)** Clone the repository
```
git clone https://github.com/mariotlemes/intent_layer.git
```
**3)** Install requirements.txt:
```
cd intent_layer
python3 -m venv .venv
source .venv/bin/activate
install -r requirements.txt
```

