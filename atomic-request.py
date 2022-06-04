import requests
import json 


def get_assets():

	response = requests.get('https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id')
	json = response.json()
	resp = requests.get('https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id')
	data = resp.json()
	asset_id = data['data']['asset_id']
	return asset_id

get_assets()
#for key in json:
#	print(key, json[key])
#json_data = json.loads(response.text)

#print(json['data']['name'])
#return assest_id

