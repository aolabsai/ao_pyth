import requests
import numpy as np

ao_endpoint_kennel = "https://api.aolabs.ai/v0dev/kennel"
ao_endpoint_agent = "https://api.aolabs.ai/v0dev/kennel/agent"


def _set_endpoint(endpoint):
    if endpoint =="dev":
        endpoint = "https://api.aolabs.ai/v0dev/kennel"
    elif endpoint == "prod":
        endpoint = "https://api.aolabs.ai/kennel"
    else:
        raise ValueError(f"Not a valid endpoint: {endpoint}. Valid endpoints are dev or prod")
    return endpoint

class Arch:
    def __init__(self, arch_i=False, arch_z=False, arch_c=[], connector_function="full_conn", connector_parameters="[]", description="None",
                 api_key="", kennel_id=False, permissions="free and open as the sea!", arch_url=False, endpoint="dev"):
        

        """
            Initalize Arch

            Params:
        """

        self.endpoint = _set_endpoint(endpoint.lower())
        self.arch_i = arch_i
        self.arch_z = arch_z
        self.arch_c = []
        self.connector_function = connector_function
        self.connector_parameters = connector_parameters
        self.description = description

        # ao_api attributes
        self.api_key = api_key
        self.kennel_id = kennel_id
        self.permissions = permissions
        self.arch_url = arch_url



        if self.arch_url:
            payload = {
                "kennel_name": self.kennel_id,
                "arch_url": self.arch_url,
                "description": self.description,
                "permissions": self.permissions
            }
        elif arch_i and arch_z:
            payload = {
                "kennel_name": self.kennel_id,
                "arch": {
                    "arch_i": self.arch_i,
                    "arch_z": self.arch_z,
                    "connector_function": self.connector_function,
                    "connector_parameters": self.connector_parameters
                },
                "description": self.description,
                "permissions": self.permissions
            }
        else:
            return "Invalid; specify an arch_i and arch_z or arch_url"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-API-KEY": f"{self.api_key}"
        }

        response = requests.post(self.endpoint, json=payload, headers=headers)
        self.api_status = response.text


class Agent:
    def __init__(self, Arch=False, notes="",
                 api_key=False, kennel_id=False, uid=False, endpoint=False):
        
        # ao_api attributes
        self.uid = uid
        # self.error_message = False
        if Arch:
            self.api_key = Arch.api_key
            self.kennel_id = Arch.kennel_id
            self.endpoint = Arch.endpoint
        elif kennel_id:
            self.api_key = api_key
            self.kennel_id = kennel_id
            self.endpoint = _set_endpoint(endpoint.lower())
        else: 
            self.error_message = "You must either use a valid Arch variable or enter an api_key and kennel_id"
            return ValueError(f"{self.error_message}")

    def next_state(self, INPUT, LABEL=None, Instincts=False, Cneg=False, Cpos=False,
                   DD=True, Hamming=True, Default=True, unsequenced=False): 
    
        # handling numpy arrays as input
        if type(INPUT) is np.ndarray:
            INPUT = INPUT.tolist()
        if type(LABEL) is np.ndarray:
            LABEL = LABEL.tolist()

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
                    "US": unsequenced,
                    "neuron": {
                        "DD": DD,
                        "Hamming": Hamming,
                        "Default": Default
                    }
                }
            }
        else:
            payload = {
                "kennel_id": self.kennel_id, 
                "agent_id": self.uid,  
                "INPUT": INPUT, 
                "INSTINCTS": Instincts,
                "control": {
                    "CN": Cneg,
                    "CP": Cpos,
                    "US": unsequenced,
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

        agent_response = requests.post(ao_endpoint_agent, json=payload, headers=headers).json()
        print(agent_response)
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
        agent_response = requests.post(ao_endpoint_agent, json=payload, headers=headers).json()
        return agent_response


    def delete(self):
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
        response = requests.post(ao_endpoint_agent, json=payload, headers=headers)
        return response


