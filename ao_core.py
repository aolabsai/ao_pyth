import requests


ao_endpoint_url = "https://api.aolabs.ai/v0dev/kennel/agent"


class Agent():
    def __init__(self, uid, kennel_id, api_key):
        self.uid = uid
        self.kennel_id = kennel_id
        self.api_key = api_key

    def next_state(self, INPUT, LABEL=None):    #TODO add all of the flags 
        if LABEL:
            payload = {
                "kennel_id": self.kennel_id, 
                "agent_id": self.uid,  
                "INPUT": INPUT, 

                "LABEL": LABEL,

                "control": {
                    "US": True,
                    "states": 1,
                }
            }
        else:
            payload = {
                "kennel_id": self.kennel_id, 
                "agent_id": self.uid,  
                "INPUT": INPUT, 

                "control": {
                    "US": True,
                    "states": 1,
                }
            }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }

        agent_response = requests.post(ao_endpoint_url, json=payload, headers=headers).json()
        return agent_response
    
    def kennel_create(self, kennel_name, arch_url, description, permissions="free and open as the sea!"):
        payload = {
            "kennel_name": kennel_name,
            "arch_URL": arch_url,
            "description": description,
            "permissions": permissions
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        response = requests.post(ao_endpoint_url, json=payload, headers=headers)
        return response


    def agent_delete(self):
        payload = {
            "kennel_id": self.kennel_id,
            "agent_id": self.uid,
            "request": "delete_agent"
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        response = requests.post(ao_endpoint_url, json=payload, headers=headers)
        return response


