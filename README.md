# The python package wrapper of the ao_core API.

This python repo wraps our api in a easy to use fast pip installable package. It is almost one to one with ao_core so most of the documentation will carry over here; we will add documentation below for futher instructions on how to use the library!

## Installation & Use

Install with pip from command line with:
```bash
pip install ao_pyth # https://pypi.org/project/ao-pyth/
# or
pip install git+https://github.com/aolabsai/ao_pyth
```

This open source reference design repo will walk you through a simple application using this library: https://github.com/aolabsai/ao_loop1/


## Authentication & API keys
To get an API key, please message us on discord: https://discord.gg/mE3WBFaMQy


## Documentation

To create a new Arch use:
```python
arch = ao.Arch(arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn",
               api_key=api_key, email=<<insert_email>>, kennel_id=<<insert_unique_ID>>)
```

To initalise an Agent use:
```python
agent = ao.Agent(Arch=arch, 
                 api_key=api_key)
```

To invoke an Agent to get its output, use its next_state method:
```python
agent.next_state(INPUT="111"):

response = agent.next_state(INPUT=input, LABEL=label)
agent_output = response["story"] # this is the output of the agent for use in your application
agent_state  = response["state"]
print("Agent's response: ", agent_output, " - at state: ", agent_state)
```

To train an Agent, provide a label with next_state:
```python
agent.next_state(INPUT="000", LABEL="0"):
```

To delete an Agent from our hosted database use:
```python
agent.delete()
```
