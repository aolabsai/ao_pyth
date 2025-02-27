import ao_python.ao_python as ao
from config import api_key


message = ao.Arch(kennel_id="KennelDelete", arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn", api_key=api_key)
print(message.text)

agent = ao.Agent(kennel_id="KennelCreateDemoWrapper5", uid = "Agent1", api_key=api_key)

response = agent.next_state(INPUT=[0,0,0])

print(response)


message2 = agent.delete()
print(message2.text)