import requests

ao_endpoint_url = "https://api.aolabs.ai/v0dev/kennel/agent"
ao_endpoint_create = "https://api.aolabs.ai/v0dev/kennel"



def Arch(kennel_id, arch_i=False, arch_z=False, connector_function="full_conn", connector_parameters="[]", description="None", permissions="free and open as the sea!", arch_url=False, api_key=""):
    if arch_url:
        payload = {
            "kennel_name": kennel_id,
            "arch_url": arch_url,
            "description": description,
            "permissions": permissions
        }
    elif arch_i and arch_z:
        payload = {
            "kennel_name": kennel_id,
            "arch": {
                "arch_i": arch_i,
                "arch_z": arch_z,
                "connector_function": connector_function,
                "connector_parameters": connector_parameters
            },
            "description": description,
            "permissions": permissions
        }
    else:
        return "Invalid, not specified arch i and arch z or arch_url"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.post(ao_endpoint_create, json=payload, headers=headers)
    return response


class Agent():
    def __init__(self, uid, kennel_id, api_key):
        self.uid = uid
        self.kennel_id = kennel_id
        self.api_key = api_key

    def next_state(self, INPUT, LABEL=None, Instincts=False, Cneg=False, Cpos=False, Unsequenced=False, DD=True, Hamming=True, Default=True):    #TODO add all of the flags 
        if LABEL:
            payload = {
                "kennel_id": self.kennel_id, 
                "agent_id": self.uid,  
                "INPUT": INPUT, 
                "LABEL": LABEL,
                "INSTINCTS": Instincts,
                "control": {
                    "CN": Cneg,
                    "CP": Cpos,
                    "US": Unsequenced,
                    "neuron": {
                        "DD": DD,
                        "Hamming": Hamming,
                        "Default": Default
                    }
                }
            }
        else:
            print("no label")
            payload = {
                "kennel_id": self.kennel_id, 
                "agent_id": self.uid,  
                "INPUT": INPUT, 
                "INSTINCTS": Instincts,
                "control": {
                    "CN": Cneg,
                    "CP": Cpos,
                    "US": Unsequenced,
                    "neuron": {
                        "DD": DD,
                        "Hamming": Hamming,
                        "Default": Default
                    }
                }
            }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }

        agent_response = requests.post(ao_endpoint_url, json=payload, headers=headers).json()
        return agent_response
    
    def reset_state(self):
        payload = {
                "kennel_id": self.kennel_id, 
                "agent_id": self.uid,  

                "control": {
                    "US": True,
                }
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }
        agent_response = requests.post(ao_endpoint_url, json=payload, headers=headers).json()
        return agent_response


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


