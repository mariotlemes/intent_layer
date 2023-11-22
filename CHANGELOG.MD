## Change Log

### 11-23-2023:
#### Global Features
- [x] `get_public_ip_osm()` - get value from IP_ADDRESS_OSM (OS environment variable)  
- [x] `verify_osm_status()` - verify OSM (Open Source Mano) status.
- [x] `generate_nbi_token()` - generate token for NBI OSM authentication

####  1) intent_gui.py
- [x] `GUI template` - create a basic GUI for intent expressing.
- [X] `insert_intent()` - add intent into a database from GUI-template.
- [X] `show_table_intent()` - show created intents from database.
- [ ] `create_subscription_osm()` - create a new subscription to notifications related to NS lifecycle changes
- [ ] `receive_subscrition_changes()` - receive notifications of a subscription.
- [ ] `update_intent_status()` - update intent status (started, running, deployed, etc) accordingly to
received notifications.

####  2) intent_engine.py
- [X] `import nile` - import code from NILE (Network Intent LanguagE).
- [X] `get_intents_data()` - get intents data from database.

####  3) intent_translator.py
- [X] `trigger_creation_slice()` - trigger the creation of slice interacting 
with OSM NBI REST API.

