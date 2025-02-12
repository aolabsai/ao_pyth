import requests


ao_endpoint_url = "https://api.aolabs.ai/v0dev/kennel/agent"


class Agent():
    def __init__(self, uid, kennel_id, api_key):
        self.uid = uid
        self.kennel_id = kennel_id
        self.api_key = api_key

    def next_state(self, INPUT, LABEL=None):
        payload = {
            "kennel_id": self.kennel_id, 
            "agent_id": self.uid,  
            "INPUT": INPUT, 

            "Label": LABEL,

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
        return agent_response.get("story")
    def reset_state(self):
        pass

    def kennel_create(self, arch_url):
        pass

    def agent_delete(self):
        pass


