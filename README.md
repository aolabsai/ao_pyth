# The python package wrapper of the ao_core API.

This python repo wraps our api in a easy to use fast pip installable package. It is almost one to one with ao_core so most of the documentation will carry over here, we will add documentation below for futher instructions on how to use the library!

## Installation

Install with pip from command line with:
```bash
pip install git+https://github.com/aolabsai/pythonApiWrapper
```

## Documentation

To create a new kennel use:
```bash
ao.kennel_create(kennel_name, arch_url, description)
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


