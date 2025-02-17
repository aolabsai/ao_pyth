import ao_python.ao_python as ao
from config import api_key

arch_url = "https://gist.githubusercontent.com/Rafipilot/d354e1d4706096ac3db66c0d8e21e646/raw/7526c258ecd7c1a550b5cbcc70059e907da0aeb1/gistfile1.txt" #Simple demo arch

Arch = ao.Arch(api_key)

message = Arch.kennel_create(kennel_name="KennelCreateDemoWrapper3", arch_url=arch_url, description="Demo")
print(message.text)

agent = ao.Agent("1stWrapperTest3", "KennelCreateDemoWrapper3", api_key)

response = agent.next_state(INPUT=[0,0,0], LABEL=[0])

print(response["story"])


