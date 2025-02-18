import ao_python.ao_python as ao
from config import api_key  #Get an api key

agent = ao.Agent("Api_wrapperTest", "recommender3", api_key)  # Init agent

response = agent.next_state(INPUT=[1, 1, 1, 1, 1 , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])  # Next_state method
print(response)
agent_response = response["story"]  
state= response["state"]

print("response:", agent_response, "at state:",state)
