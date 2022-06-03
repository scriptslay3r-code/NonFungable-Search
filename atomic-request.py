import requests
import json 

response = requests.get('https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id')

json_data = response.json()
#json_data = json.loads(response.text)

print(json_data)