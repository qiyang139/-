from eth_account import Account

from web3 import Web3
def createNewETHWallet():

 account = Account.create()

 privateKey = account._key_obj

 publicKey = privateKey.public_key

 address = publicKey.to_checksum_address()



 print("privateKey:", privateKey)

 print("publicKey:", publicKey)

 print("address:", address)



 return privateKey, publicKey, address