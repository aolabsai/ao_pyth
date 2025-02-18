import ao_python.ao_python as ao
from config import api_key  #Get an api key
import numpy as np

Arch = ao.Arch(api_key)

message = Arch.kennel_create(kennel_name="recommender4", arch_i="[10, 4, 10]", arch_z="[10]", connector_function="full_conn")
print(message.text)


agent = ao.Agent(uid="recsys5", kennel_id="recommender4", api_key=api_key)  # Init agent

Input = []
for i in range(24):
    Input.append(1)

response = agent.next_state(INPUT=Input, LABEL=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # Next_state method
print(response)
agent_response = response["story"]  
state= response["state"]

print("response:", agent_response, "at state:",state)
