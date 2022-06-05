import requests
import json 
import pprint

def get_id():
	url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	id = (xData['data'][0]['asset_id'])
	return id
	
def get_name():
	url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	name = (xData['data'][0]['name'])
	return name
	
def get_multiplier():
	url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	multiplier = (xData['data'][0]['data']['type'])
	multiplier = multiplier.replace('X', '')
	return multiplier

def get_series():
	url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	series = (xData['data'][0]['data']['series'])
	return series


id = get_id()
name = get_name()
multiplier = get_multiplier()
series = get_series()
pprint.pprint("assest id: " + id)
pprint.pprint("name: " + name)
pprint.pprint("multiplier: " + multiplier)
pprint.pprint("This beautiful NFT is from the " + series + " series!")

