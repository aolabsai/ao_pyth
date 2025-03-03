import numpy as np

import ao_python as ao
from config import api_key


# Creating an Agent Architecture
arch = ao.Arch(arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn",
                  api_key=api_key, kennel_id="full_demo")
# checking if the Arch has been successfully created
print(arch.api_status)


# Creating an Agent using that Arch
agent = ao.Agent(Arch=arch,
                 api_key=api_key, uid="full_demo_agent")
## If you don't have an `Arch` variable in your runtime, you can slso create/invoke Agents by entering an `api_key` and `kennel_id`


# Invoking the Agent
input = np.ones(3)
label = [1]
response = agent.next_state(INPUT=input, LABEL=label)

agent_output = response["story"] # this is the output of the agent for use in your application
agent_state  = response["state"]
print("Agent's response: ", agent_output, " - at state: ", agent_state)


# Deleting the Agent so that others can try this script
agent.delete()