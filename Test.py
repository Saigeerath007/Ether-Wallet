from tkinter import *
from BlockChain import Web3
from eth_account import Account

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


def printBalance():
    '''
    Function for fetching and printing Balance on screen.
    '''
    ac = getAccount(privateKey.get())
    bal = getBalance(ac)
    Label(root, text='Your balance is :' + str(bal), font=("Calibri", 13), fg='brown').place(x=220, y=200)


def makeTransaction():
    '''
    function to initiate transaction and print the details on screen.
    '''
    bal_bef = getBalance(getAccount(privateKey.get()))
    dict = SendEther(receiver.get(), privateKey.get(), amount.get())
    Label(root, text=' Transaction Sucessfull ', font=("Calibri", 13), fg='green').place(x=480, y=570)
    Label(root, text='Transaction hash is : ' + str(dict['txn_hash']), font=("Calibri", 13), fg='green').place(x=80,
                                                                                                               y=600)  # place(x = 80, y = 630)
    Label(root, text=' Sender  Address is : ' + str(dict['sender_address']), font=("Calibri", 13), fg='green').place(
        x=80, y=630)
    Label(root, text='Receiver Address is : ' + str(dict['receiver']), font=("Calibri", 13), fg='green').place(x=80,
                                                                                                               y=660)
    Label(root, text='Balance Before Transaction is : ' + str(bal_bef), font=("Calibri", 13), fg='green').place(x=80,
                                                                                                                y=690)
    Label(root, text='Balance  After Transaction is : ' + str(dict['bal']), font=("Calibri", 13), fg='green').place(
        x=80, y=720)
    Label(root, text='Amount of ETHER Transfered is : ' + str(amount.get()), font=("Calibri", 13), fg='green').place(
        x=80, y=750)  # place(x = 420, y = 690)


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


def main():
    '''
    GUI of the project.
    '''
    # Page headers, Size and Initiation of GUI
    global root
    root = Tk()
    root.title("Welcome")
    root.geometry("1050x800")

    # global Variables so that they are aceesible to all functions
    global privateKey
    global receiver
    global amount
    global account
    account = StringVar()
    privateKey = StringVar()
    receiver = StringVar()
    amount = StringVar()

    # Title bar
    Label(root, width="300", text="EtherTransaction With Ganache & Python", bg="orange", fg="white", height="2",
          font=("Calibri", 13)).pack()

    # Taking Input (Private Key)
    Label(root, text="PrivateKey * ", font=("Calibri", 13)).place(x=200, y=120)
    Entry(root, textvariable=privateKey, width=60, fg='grey').place(x=400, y=120, height=30)

    # Button for fetching balance
    Button(root, text="Get Balance", width=20, height=1, bg="orange", command=printBalance, pady=10).place(x=735, y=200)

    # Taking Input (Address of Benificiary)
    Label(root, text="ReceiverAddress * ", font=("Calibri", 13)).place(x=200, y=370)
    Entry(root, textvariable=receiver, width=60).place(x=400, y=370, height=30)

    # Taking Input (Amount of ether to transfer)
    Label(root, text="Amount * ", font=("Calibri", 13)).place(x=200, y=420)
    Entry(root, textvariable=amount, width=30).place(x=400, y=420, height=30)

    # Button for making transaction.
    Button(root, text="Pay", width=20, height=1, bg="orange", command=makeTransaction, pady=10).place(x=735, y=500)

    root.mainloop()


if __name__ == '__main__':
    # Http url of Ganache running on local network.s
    rpcUrl = 'HTTP://127.0.0.1:7545'
    w3 = Web3(Web3.HTTPProvider(rpcUrl))
    main()