# blockchain/utils/tron.py

from tronpy import Tron
from tronpy.keys import PrivateKey
import os

class TronClient:
    def __init__(self):
        self.client = Tron(network='nile')
        self.contract_address = os.getenv('TRON_USDT_CONTRACT_ADDRESS')

    def send_transaction(self, sender_address, private_key, to_address, amount):
        # Get account details
        priv_key = PrivateKey(bytes.fromhex(private_key))
        txn = (
            self.client.trx.transfer(sender_address, to_address, int(amount * 1e6))
            .memo('Transaction Memo')
            .build()
            .sign(priv_key)
        )
        # Broadcast transaction
        result = txn.broadcast()
        return result['txid']

# Example usage
# client = TronClient()
# tx_id = client.send_transaction('sender_address', 'private_key', 'recipient_address', 1.5)
