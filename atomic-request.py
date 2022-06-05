import requests
import json 
import pprint

url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'


r = requests.get(url)
jData = r.json()
dump = json.dumps(jData)
xData = json.loads(dump)
id = (xData['data'][0]['asset_id'])
pprint.pprint(id)

