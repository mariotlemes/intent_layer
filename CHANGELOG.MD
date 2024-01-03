### Features

---
All `notable features` (is not an exhaustive list) are documented in this file.

---
#### `intent_gui.py:` template for intent expressing.
- [x] `insert_intent()` - This method adds an intent into a database from GUI-template.
- [x] `show_table_intent()` - This method shows created intents from database.
--- 
####  `intent_engine.py`: converts intents into NILE (Network Intent LanguagE)
- [x] `get_intent_from_database()` - This method gets intents data from database.
- [x] `filling_data (intent_from_database)` - This method returns an entity required for NILE builder. 
- [x] `transform_to_nile (entity)` - This method builds a NILE intent .
--- 
#### `intent_translator.py`: mapping NILE intents to suitable VNFd and NSd.
- [x] `extract_values_from_intent(nile_intent)` - This method extracts name and number of VNFs from a NILE intent.
- [x] `match_nsd_descriptor (name_intent, number_vfs)` - This method match NS descriptor accordingly with required number of VFs.
---
#### `handler_osm.py:` interacts with OSM (Open Source Mano) via REST API.
- [x] `verify_osm_status()` - This method checks OSM status (online/offline).
- [x] `generate_nbi_token()` - This method generates a bearer token for API Rest authorization.
- [x] `get_vim_accounts()` - This method gets an ID list of virtual infrastructure managers.
- [x] `get_vnf_package()` - This method gets a list (ID) of Virtual Network Function Descriptors.
- [x] `get_ns_instance` - This method gets a list (ID) of Network Service Instances.
- [x] `get_ns_instance_by_name(name)` - This method gets an ID of Network Service Instance using the name.
- [x] `get_ns_package()`- This method gets a list (ID) of Network Service Descriptors.
- [x] `get_ns_package_by_name(name)`- This method gets an ID of Network Service Descriptor using the name.
- [x] `get_ns_lcmp_op_occs(ns_instance_id)` - This method checks the status of network instance.
- [x] `post_vnf_package(data):` This method uploads a VNF descriptor package in OSM.
- [x] `post_ns_package (data):` This method uploads a NS descriptor package in OSM.
- [x] `post_ns_instance_create_and_instantiate(nsd_id, ns_name, ns_description)` - This method creates and instantiates a network service
- [x] `post_ns_instance_terminate (ns_instance_id):` - This method terminates a network service instance. 
- [x] `del_ns_instace(ns_instance_id)` - This method deletes a network service instance.
- [x] `del_vnf_package(vnf_package_id)` - This method deletes a virtual network function descriptor.
- [x] `del_ns_package(ns_package_id)` - This method deletes a network service descriptor.
- [x] `clean_environment(self)` - This method performs a clean environment in OSM, i.e., deletes all VNFd, NSDd, and network instances.
---
#### `tests.py`: performance evaluation.
- [x] `load_vnf_descriptors()` - This method calculates the time for onboarding the VNF descriptors in OSM.
- [X] `onboarding(number_descriptors)` - This method calculates the time for onboarding the specific NS descriptor accordingly to required number of descriptors.
- [X] `onboarding_and_instantiation (number_of_tests, name_ns_intance, number_descriptors)` - This method calculates the average time (based on number of tests) for onboarding VNFs and NSd to OSM. After,
    shows the average time for creation and instantiation the Network Service Instance.



