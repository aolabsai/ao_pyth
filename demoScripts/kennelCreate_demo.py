import ao_python as ao
from config import api_key


arch = ao.Arch(arch_i="[1, 1, 1]", arch_z="[1]", connector_function="full_conn",
                  api_key=api_key, kennel_id="kennelCreate_demo")
print(arch.api_status)

# If your Arch has been successfuly created in our API, you should see a confirmation message like this when printing Arch.api_status:
## '"{\\"kennel_id\\": \\"kennelCreate_demo\\", \\"developer_id\\": \\"v0dev\\", \\"description\\": \\"None\\", \\"arch_string\\": \\"arch_string upload SUCCESSFUL\\", \\"permissions\\": \\"free and open as the sea!\\", \\"agents\\": \\"newly created Kennel with no Agents yet! Get started with POST /kennel/agent\\"}"'