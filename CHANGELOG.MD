### Features

---
All notable features to this project will be documented in this file.

---

#### `handler_osm.py:` handles the NBI OSM.
class HandlerOSM:
- [x] `verify_osm_status()` - verify OSM (Open Source Mano) status.
- [x] `generate_nbi_token()` - generate token for NBI OSM authentication
- [x] `get_ns_packages()`- get information about multiple NS packages
- [x] `get_ns_instances(name)` - get ID information about a specific NS instance.
- [x] `get_public_ip_osm()` - get value from IP_ADDRESS_OSM (OS environment variable) 
- [x] `get_vim_accounts()` - get information about VIM created in OSM.
- [x] `post_vnf_packages(vnfd_data):` post a new VNFd in JSON format to OSM.
- [x] `post_ns_package (nsd_data):` post a new NSd in JSON format to OSM.
- [x] `post_create_ns_instances (nsd_id, ns_name, ns_description, vim_account_id): `post a new NS instance. 
---

#### `intentgui.py:` basic GUI for intent expressing.
class IntentGUI:
- [X] `insert_intent()` - add intent into a database from GUI-template.
- [X] `show_table_intent()` - show created intents from database.
- [ ] `create_subscription_osm()` - create a new subscription to notifications related to NS lifecycle changes
- [ ] `receive_subscrition_changes()` - receive notifications of a subscription.
- [ ] `update_intent_status()` - update intent status (started, running, deployed, etc) accordingly to
received notifications.

--- 
####  `intent_engine.py`: converts intents into NILE
class IntentEngine:
- [X] `import nile` - import code from NILE (Network Intent LanguagE).
- [X] `get_intents_data()` - get intents data from database.


--- 
#### `intent_translator.py`: mapping NILE intents to VNFd and NSD.
TO DO

--- 
#### `tests.py`: to verify perfomance evaluation.

class Tests:
- [X] `onboarding()` - Onboarding  (VNFd and NSd)
- [X] `instantiaton()` - NSd instantiation.



