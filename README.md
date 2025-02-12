# The python package wrapper of the ao_core API.

This python repo wraps our api in a easy to use fast pip installable package. It is almost one to one with ao_core so most of the documentation will carry over here, we will add documentation below for futher instructions on how to use the library!

## Installation

Install with pip from command line with:
```bash
pip install githttps://github.com/aolabsai/ao_python
```

## Documentation

To initalise Arch class:
```bash
Arch = ao.Arch(api_key)
```
To create a new kennel use:
```bash
Arch.kennel_create(kennel_name, arch_url, description)
```

To initalise our agents use
```bash
agent = ao.Agent(unique_id, kennel_id, api_key)
```

To use next_state():

```bash
agent.next_state(self, INPUT, LABEL=None, Instincts=False, Cneg=False, Cpos=False, Unsequenced=False, DD=True, Hamming=True, Default=True):
```

To delete and agent use:
```bash
agent.agent_delete()
```

## Demo script

```bash
import ao_core as ao
from config import api_key  #Get an api key


agent = ao.Agent("Api_wrapperTest", "recommender3", api_key)  # Init agent

response = agent.next_state(INPUT=[1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], LABEL=[0,0,0,0,0,0,0,0,0,0])  # Next_state method

agent_response = response["story"]  
state= response["state"]

print("response:", agent_response, "at state:",state)
```


