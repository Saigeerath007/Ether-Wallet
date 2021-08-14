from web3 import Web3
from eth_account import Account

# Http url of Ganache running on local network.s
rpcUrl = 'HTTP://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(rpcUrl))


def getBalance(address):
    '''
    Function to get the balance from address fo Account.
    '''
    balanceInWei = w3.eth.getBalance(address)
    balanceInEther = w3.fromWei(balanceInWei, 'ether')
    return balanceInEther


def getAccount(privateKey):
    '''
    Fetching Account address from Private Key
    '''
    return Account.privateKeyToAccount(privateKey).address


def SendEther(receiver, sender_private_key, value):
    '''
    function to send ether from account to account.
    '''
    # Getting Address from PrivateKey
    sender_address = Account.privateKeyToAccount(sender_private_key).address

    # Transaction Information
    txn = {
        'nonce': w3.eth.get_transaction_count(sender_address),
        'to': receiver,
        'value': w3.toWei(value, 'ether'),
        'gas': 100000,
        'gasPrice': Web3.toWei(50, 'gwei'),
    }

    # Signed Transaction
    signed_txn = w3.eth.account.sign_transaction(txn, sender_private_key)
    # Hash of the transaction.
    txn_hash = w3.toHex(w3.eth.send_raw_transaction(signed_txn.rawTransaction))

    # returning the txn_id, both accounts of transaction
    return {'txn_hash': txn_hash,
            'bal': getBalance(sender_address),
            'sender_address': sender_address,
            'receiver': receiver,
            }
