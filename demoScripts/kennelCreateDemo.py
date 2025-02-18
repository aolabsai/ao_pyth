import ao_python.ao_python as ao
from config import api_key

Arch = ao.Arch(api_key)

message = Arch.kennel_create(kennel_name="KennelCreateDemoWrapper4", arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn")
print(message.text)

agent = ao.Agent(kennel_id="KennelCreateDemoWrapper4", uid = "Agent1", api_key=api_key)

response = agent.next_state(INPUT=[0,0,0], LABEL=[0])
print(response)
print(response["story"])


