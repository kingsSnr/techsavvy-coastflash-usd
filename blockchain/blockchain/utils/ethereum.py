# blockchain/utils/ethereum.py

from web3 import Web3
import os

class EthereumClient:
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(os.getenv('WEB3_PROVIDER_URI')))
        self.contract_address = os.getenv('ETHEREUM_USDT_CONTRACT_ADDRESS')

    def send_transaction(self, sender_address, private_key, to_address, amount):
        # Create transaction
        nonce = self.web3.eth.getTransactionCount(sender_address)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei')
        }
        # Sign transaction
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        # Send transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)

# Example usage
# client = EthereumClient()
# tx_hash = client.send_transaction('sender_address', 'private_key', 'recipient_address', 1.5)
