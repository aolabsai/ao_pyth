import ao_python as ao
from config import api_key


arch = ao.Arch(arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn",
                  api_key=api_key, kennel_id="kennel_delete_demo")

# Creating an Agent from that Arch
agent = ao.Agent(arch, uid = "Agent_1", api_key=api_key)

# Let's use the Agent a few times
agent.next_state(INPUT=[0,0,0])

# Now let's delete the Agent from the API database
response = agent.delete()
print(response.text)