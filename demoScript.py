import ao_core.ao_core as ao
from config import api_key

agent = ao.Agent("RafiApi_wrapperTest", "recommender3", api_key)

response = agent.next_state(INPUT=[1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], LABEL=[0,0,0,0,0,0,0,0,0,0])

agent_response = response["story"]
state= response["state"]

print("response:", agent_response, "at state:",state)
