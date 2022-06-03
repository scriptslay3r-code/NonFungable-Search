# <p align="center">NonFungable-Search</p>
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


## Let me explain myself

I really like the idea of this project. The entire value is based on an honor based system. 
For example, I caught this project early, joined the Discord and earned an NFT from NFSE that allowed me to recieve future air drops. Now let's say that I recieve an air dropped 100x2 card. I am supposed to sell that card for 100 WAX and it has a resale multiplier of 2. Which means, after it is bought, it is to be re listed for 2 times the price paid originally. And in this case it would be listed for sell for 200 Wax. 
It has a value because of the hope to resale it for a even higher amount. 
They are technically worthless, however it's all community trust based. 
I'm having to trust that the next guy will buy it for the price + the multiplier. 

### There's a twist though 

This project added an incentive to buy and resale. And they call it 'live staking'. While you have a correctly listed NFT for sale, you are eligible for future air drops. Which is a pretty interesting idea to me. 

### The "issue" was people were listing the NFTs for "wrong" prices. 
And I put air quotes around this because that's the beauty of NFTs, you own them. So you can do with it whatever the hell you want :) and I support owning your digital assets. 
However, if you want to participate in their live staking experience, you're doing it the wrong way if you list incorrectly.  

Anyway, being faced with this *issue*, you could not simply purchase any NFSE NFT and relist it for the multiplier amount. You should check the sale logs of the NFT. 

And maybe I'm doing this for all for nothing. But I didn't find a way that was super simple to check the logs. 

So I aim to make a program that sorts through the listings, and based off the name of the NFT, (100X2) check for proper live staking. 

 .