import ao_python as ao
from config import api_key


# Creating an Agent Architecture
arch = ao.Arch(arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn",
                  api_key=api_key, kennel_id="ao_python__full_demo_01", stage="dev")
# checking if the Arch has been successfully created
print(arch.api_status)


# Creating an Agent using that Arch
agent = ao.Agent(Arch=arch,
                 api_key=api_key, uid="full_demo_agent_01")
## If you don't have an `Arch` variable in your runtime, you can also create/invoke Agents by entering an `api_key` and `kennel_id`

# Invoking the Agent
input = [1,1,1] # inputs and labels can be lists or 1D numpy arrays of binary ints
# input = np.ones(3, dtype=int)
label = [1]
response = agent.next_state(INPUT=input, LABEL=label) # this is the output of the agent for use in your application
state  = agent.state
print("Agent's response: ", response, " - at state: ", state)


# Deleting the Agent so that others can try this script
agent.delete()