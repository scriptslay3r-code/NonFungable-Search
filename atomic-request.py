import requests

response = requests.get("https://wax.api.atomicassets.io/atomicassets/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=100&order=desc&sort=asset_id")

print(response)