# get unspent outputrs from blockchain API

import json
import requests

# example address
ddres = '1Dorian4RoXcnBv9hnQ4Y2C1an6NJ4UrJX'

# The API URL is https://blockchain.info/unspent?active=<address>
# It returns a JSON object with a list "unspent_output", containing UTXO, like this:
#{      "unspent_outputs":[
#   {
#       "tx_hash":"ebadfaa92f1fd29e2fe29eda702c48bd11ffd52313e986e99ddad9084062167",
#       "tx`_index":51919767,
#       "tx`_output_n": 1,
#       "script":"76a91a48c7e252f8d64b0b6e313985915110fcfefcf4a2d88ac",
#       "value": 8000000,
#       "value_hex": "7a1200,"
#       "confirmations":28691 
#    },
# ...
# ]}
resp = requests.get('https://blockchain.info/unspent?active=%s' % address)
utxo_set = json.loads(resp.text)["unspent_outputs"]

for utxo in utxo_set:
    print "%s:%d - %ld Satoshis" % (utxo['tx_hash'], utxo['tx_output_n'], utxo['value'])