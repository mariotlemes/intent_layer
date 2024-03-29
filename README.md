# Intent Layer

![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=plastic&logo=Qt&logoColor=white)

## Getting started

**`Intent Layer`** has four main modules:

**1)** **`intent_gui.py`**- GUI-based for intent expressing;

**2)** **`intent_engine.py`**- Convert intents into NILE (**N**etwork **I**ntent **L**anguag**E**);

**3)** **`intent_translator.py`**- Convert NILE to suitable format e.g., VNFd (Virtual Network Function Descriptor)/NSd (Network Service Descriptor), and trigger network slice creation;

**4)** **`handler_osm.py`**- Interact with OSM (Open Source Mano) via its REST API to onboard the descriptors and to deploy the Network Slice (NS) Instance.

> Obs 1: `nile` and `utils` folders are provided by [Jacobs et al.](https://github.com/lumichatbot/webhook)

> Obs 2: This project is inspirated in this [work](https://dl.acm.org/doi/abs/10.1016/j.future.2022.12.033).


## Documentation
You can find details about the documentation in [Wiki](https://github.com/mariotlemes/intent_layer/wiki).
