import requests
import json 
import pprint
#global id
def get_id():
	
	url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)

	id = (xData['data'][0]['asset_id'])
	return id



#asset_id = get_id()
asset_id = '1099738898474'
def get_name():
	#url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id'
	
	#print(id)
#	print(get_id.id)
	base_url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets/'
	#url = ("% s % s" %(base_url , id))
	url = base_url + asset_id
	print(url)
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	name = (xData['data']['data']['name'])
	return name
def get_multiplier():
	
	base_url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets/'
	url = base_url + asset_id
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	multiplier = (xData['data']['data']['type'])
	multiplier = multiplier.replace('X', '')
	return multiplier

def get_series():
	base_url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets/'
	url = base_url + asset_id
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	series = (xData['data']['data']['series'])
	return series

def get_img():
	base_url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets/'
	url = base_url + asset_id
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	img = (xData['data']['data']['img'])
	return img

def get_total_sales():
	
	base_url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets/'
	url = base_url + asset_id
	r = requests.get(url)
	jData = r.json()
	dump = json.dumps(jData)
	xData = json.loads(dump)
	totalSales = (int(xData['data']['prices'][0]['sales']))
	return totalSales
	
totalSales = get_total_sales()


	

	
def get_sales():
	base_url = 'https://wax.api.atomicassets.io/atomicmarket/v1/assets/'


	paramaters = '/sales?page=1&limit=100&order=desc'

	url = base_url + asset_id + paramaters

	r = requests.get(url)
	jData = r.json()
	dumps = json.dumps(jData)
	xData = json.loads(dumps)
	if totalSales <=1:
		
		sales = (xData['data'][0]['price'])
		length = len(sales)
		sales = (sales[:length - 8] + " Wax")
		return sales
	
	else:
		

		#prices = [each_price['data'] for each_price in xData['price']
		#for element in xData[key]:
			sales = [each_sale['price'] for each_sale in xData['data']]
			prices = sales
			new_prices = []
			for price in prices:
			 	v = len(str(price)) - 8
			 	new = str(price)[0:v]
			 	new_prices.append(new)
			 	
		#	print(new_prices) 

			
			 												 					#	sales = (xData['data']['price'])
				#length = len(sales)
			#for x in sales:
				
			#sales = (sales[:length - 8])
			return new_prices
			


id = get_id()
name = get_name()
multiplier = get_multiplier()
series = get_series()
total_sales = get_total_sales()
sales = get_sales()

pprint.pprint("assest id: " + id)
pprint.pprint("name: " + name)
pprint.pprint("multiplier: " + multiplier)
pprint.pprint("This beautiful NFT is from the " + series + " series!")
pprint.pprint("This NFT has been sold " + (str(total_sales)) + " time(s)")
pprint.pprint("last price bought: " + (str(sales)))

