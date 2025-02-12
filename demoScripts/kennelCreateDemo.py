import ao_core.ao_core as ao
from config import api_key

arch_url = "https://gist.github.com/Rafipilot/d354e1d4706096ac3db66c0d8e21e646"

message = ao.kennel_create(kennel_name="KennelCreateDemoWrapper", arch_url=arch_url, api_key=api_key, description="Demo")
print(message.json())


agent = ao.Agent(uid="1stWrapperTest", kennel_id="KennelCreateDemoWrapper", api_key=api_key)

response = agent.next_state(INPUT=[0,0,0], LABEL=[0])

print(response["story"])


