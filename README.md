# NonFungable-Search
## Searches Atomic Marketplace for nfsocialexgg assets that have been listed correctly. 

#### Join the discord and learn about the community [here](https://discord.gg/cfgcFCTt)

#### Follow the project on [Twitter](https://twitter.com/NFSE_Experiment?s=20&t=NBit4Gx_a9jDA_V8s3O3rQ)

#### Their website is [here](nfsocialex.com)

I am not affiliated with this project, they take all credit. I am just an interested investor. 

Example output of API request:

https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=100&order=desc&sort=asset_id

## Example Request
```
curl -X 'GET' \
  'https://wax.api.atomicassets.io/atomicmarket/v1/assets?collection_name=nfsocialexgg&schema_name=nfse&page=1&limit=1&order=desc&sort=asset_id' \
  -H 'accept: application/json'
 ```
 
 
 ## Example Response
 ```
{
  "success": true,
  "data": [
    {
      "contract": "atomicassets",
      "asset_id": "1099773646288",
      "owner": "skiebeast111",
      "is_transferable": true,
      "is_burnable": true,
      "collection": {
        "collection_name": "nfsocialexgg",
        "name": "NFsocialEX",
        "img": "QmS7VzViGpNAZ82XEE3UVrRrmcTdgP6g2Vh351fjnAxPcR",
        "author": "nohn4.c.wam",
        "allow_notify": true,
        "authorized_accounts": [
          "nohn4.c.wam",
          "neftyblocksd"
        ],
        "notify_accounts": [],
        "market_fee": 0.09,
        "created_at_block": "179694164",
        "created_at_time": "1651305057500"
      },
      "schema": {
        "schema_name": "nfse",
        "format": [
          {
            "name": "name",
            "type": "string"
          },
          {
            "name": "img",
            "type": "image"
          },
          {
            "name": "type",
            "type": "string"
          },
          {
            "name": "series",
            "type": "string"
          },
          {
            "name": "website",
            "type": "string"
          },
          {
            "name": "mint Date",
            "type": "string"
          }
        ],
        "created_at_block": "179695699",
        "created_at_time": "1651305826000"
      },
      "template": {
        "template_id": "515376",
        "max_supply": "0",
        "is_transferable": true,
        "is_burnable": true,
        "issued_supply": "1",
        "immutable_data": {
          "img": "QmPXRNf1xyJ29PhysJSCzQZQdPzUt2CSitZud4ysUK6i7L",
          "name": "#100X3",
          "type": "X3",
          "series": "WATER",
          "website": "\tWWW.NFSOCIALEX.IO",
          "mint Date": "21ST MAY 2022"
        },
        "created_at_time": "1653120340500",
        "created_at_block": "183323968"
      },
      "mutable_data": {},
      "immutable_data": {},
      "template_mint": "1",
      "backed_tokens": [],
      "burned_by_account": null,
      "burned_at_block": null,
      "burned_at_time": null,
      "updated_at_block": "183530034",
      "updated_at_time": "1653223377000",
      "transferred_at_block": "183530034",
      "transferred_at_time": "1653223377000",
      "minted_at_block": "183326924",
      "minted_at_time": "1653121818500",
      "sales": [
        {
          "market_contract": "atomicmarket",
          "sale_id": "75020264"
        }
      ],
      "auctions": [],
      "prices": [
        {
          "market_contract": "atomicmarket",
          "token": {
            "token_symbol": "WAX",
            "token_precision": 8,
            "token_contract": "eosio.token"
          },
          "median": "10000000000",
          "average": "20000000000",
          "suggested_median": "10000000000",
          "suggested_average": "20000000000",
          "min": "10000000000",
          "max": "30000000000",
          "sales": "2"
        }
      ],
      "data": {
        "img": "QmPXRNf1xyJ29PhysJSCzQZQdPzUt2CSitZud4ysUK6i7L",
        "name": "#100X3",
        "type": "X3",
        "series": "WATER",
        "website": "\tWWW.NFSOCIALEX.IO",
        "mint Date": "21ST MAY 2022"
      },
      "name": "#100X3"
    }
```
    
#### Also thanks to [HackersAndSlackers](https://hackersandslackers.com/extract-data-from-complex-json-python/) 