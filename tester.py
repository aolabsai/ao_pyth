import ao_core as ao
from config import api_key

agent = ao.Agent("RafiApi_wrapperTest", "recommender3", api_key)

response = agent.next_state([1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1,0,0,0,0,0,0,0,0,0,0])

print(response)