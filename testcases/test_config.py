from silasdk import EthWallet
from silasdk.client import App
from utilities.util import Util


# Calling utility class
utility = Util()
"""
Using getUniqueName function to generate unique user_handle name.
Parameters:
        user_handle: name
            
"""
name = utility.getUniqueName(8)
user_handle = "test" + name + ".silamoney.eth"


#  Use app_handle and app_private key which we get at the time of creating the app from https://console.silamoney.com/
app_handle = 'sdap'
app_private_key = 'c2bef64adfcba8004195cdf39fceccafcb169101c3d5d7dc89140c9855c9e0e9'

app = App("SANDBOX", app_private_key, app_handle)


# check_handle_status_401 : taking hardcoded value to verify that the status 401.
check_handle_status_401 = "saty.silamoney.eth"

# It will be used at the time of silatransfer api.
business_uuid = "9f280665-629f-45bf-a694-133c86bffd5e"


# Generate etherium key and eth private address
eth = EthWallet.create()
eth_address = eth["eth_address"]
eth_private_key = eth["eth_private_key"]

# Generate wallet_address_signed_verified.
wallet = EthWallet.create()
wallet_address = wallet["eth_address"]
wallet_private_key = wallet["eth_private_key"]
verification_signature = EthWallet.signMessage(wallet_address, wallet_private_key)
wallet_address_signed_verified = EthWallet.verifySignature(wallet_address, verification_signature)
