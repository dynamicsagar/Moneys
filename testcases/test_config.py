from silasdk import EthWallet
from silasdk.client import App
from utilities.util import Util


# Calling utility class
utility = Util()
name = utility.getUniqueName(8)

# #time
# stt = time.strftime("%Y%m%d-%H")

app_handle = 'sdap'
app_private_key = 'c2bef64adfcba8004195cdf39fceccafcb169101c3d5d7dc89140c9855c9e0e9'
user_handle = "test" + name + ".silamoney.eth"
check_handle_status_401 = "saty.silamoney.eth"
business_uuid = "9f280665-629f-45bf-a694-133c86bffd5e"

# import os
app = App("SANDBOX", app_private_key, app_handle)

#
eth = EthWallet.create()
eth_address = eth["eth_address"]
eth_private_key = eth["eth_private_key"]

#
eth_2 = EthWallet.create()
eth_address_2 = eth_2["eth_address"]
eth_private_key_2 = eth_2["eth_private_key"]

#
wallet = EthWallet.create()
wallet_address = wallet["eth_address"]
wallet_private_key = wallet["eth_private_key"]
verification_signature = EthWallet.signMessage(wallet_address, wallet_private_key)
wallet_address_signed_verified = EthWallet.verifySignature(wallet_address, verification_signature)















