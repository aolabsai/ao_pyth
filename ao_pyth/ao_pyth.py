import requests
import numpy as np


BASE_URL = "https://api.aolabs.ai/"

ENDPOINTS = {
    "dev": {
        "kennel": f"{BASE_URL}v0dev/kennel",
        "agent": f"{BASE_URL}v0dev/kennel/agent"
    },
    "prod": {
        "kennel": f"{BASE_URL}prod/kennel",
        "agent": f"{BASE_URL}prod/kennel/agent"
    }
}

def _set_endpoint(stage, type):
    stage_key = "dev" if "dev" in stage.lower() else "prod" if "prod" in stage.lower() else None
    if not stage_key or type not in ENDPOINTS[stage_key]:
        raise ValueError(f"Invalid stage or type: stage={stage}, type={type}")
    return ENDPOINTS[stage_key][type]

class Arch:
    def __init__(self, arch_i=False, arch_z=False, arch_c="[]", connector_function="full_conn", connector_parameters="[]", description="None",
                 api_key="", kennel_id=False, permissions="free and open as the sea!", arch_url=False, stage="prod"):
        
        if not api_key:
            raise ValueError(f"You must enter an api_key")

        if not ((arch_i and arch_z) or arch_url):
            raise ValueError("You must enter both arch_i and arch_z or provide an arch_url")
        
        if type(arch_i) is not str:
            arch_i = str(arch_i)

        if type(arch_z) is not str:
            arch_z = str(arch_z)

        if not kennel_id:
            raise ValueError(f"You must enter a kennel_id")

        self.endpoint = _set_endpoint(stage, "kennel")
        self.stage = stage

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
    def __init__(self, Arch=False, notes="", save_meta=False, _steps=1000000,
                 api_key=False, kennel_id=False, uid=False, endpoint=False, stage="prod"):
        
        # ao_api attributes
        self.uid = uid

        if not uid:
            raise ValueError(f"You must enter a uid")
        self.state = 1
        self.save_meta = False           

        if Arch:
            self.api_key = Arch.api_key
            self.kennel_id = Arch.kennel_id
            self.endpoint = _set_endpoint(Arch.stage, "agent")   # get agent endpoint
        elif kennel_id:
            if not api_key:
                raise ValueError(f"You must enter an api_key")
            self.api_key = api_key
            self.kennel_id = kennel_id
            self.endpoint = _set_endpoint(stage, "agent")   # get agent endpoint
        else: 
            raise ValueError(f"You must either use a valid Arch variable or enter an api_key and kennel_id")

    def next_state(self, INPUT, LABEL=None, Instincts=False, Cneg=False, Cpos=False,
                   DD=True, Hamming=True, Default=True, unsequenced=True): 
    
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

        agent_response = requests.post(self.endpoint, json=payload, headers=headers).json()
        self.state = agent_response["state"]
        output = np.asarray(list(agent_response["story"]), dtype="int8")

        return output
    
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
        agent_response = requests.post(self.endpoint, json=payload, headers=headers).json()
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
        response = requests.post(self.endpoint, json=payload, headers=headers)
        return response


