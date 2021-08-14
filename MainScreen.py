from tkinter import *
from PIL import Image, ImageTk
import json
from BlockChain import Web3
from eth_account import Account

data = {}
root = Tk()


class Transaction:
    def __init__(self, tk):
        self.root = tk
        # self.user = user
        self.root.geometry('1050x800+300+200')
        self.root.title('Welcome')
        self.root.resizable(0, 0)

        self.rpcUrl = 'HTTP://127.0.0.1:7545'
        self.w3 = Web3(Web3.HTTPProvider(self.rpcUrl))


        # Label(root, width="300", text="EtherTransaction With Ganache & Python", bg="orange", fg="white", height="2",
        #       font=("Calibri", 13)).pack()

        # Taking Input (Private Key)
        Label(root, text="PrivateKey * ", font=("Calibri", 13)).place(x=200, y=120)
        self.privateKey = Entry(root, width=60, fg='grey')
        self.privateKey.place(x=400, y=120, height=30)

        # Button for fetching balance
        Button(root, text="Get Balance", width=20, height=1, bg="orange", command=lambda: self.printBalance(),
               pady=10).place(x=735,
                              y=200)

        # Taking Input (Address of Benificiary)
        Label(root, text="ReceiverAddress * ", font=("Calibri", 13)).place(x=200, y=370)
        self.receiver = Entry(root, width=60)
        self.receiver.place(x=400, y=370, height=30)

        # Taking Input (Amount of ether to transfer)
        Label(root, text="Amount * ", font=("Calibri", 13)).place(x=200, y=420)
        self.amount = Entry(root, width=30)
        self.amount.place(x=400, y=420, height=30)

        # Button for making transaction.
        Button(root, text="Pay", width=20, height=1, bg="orange", command=lambda: self.makeTransaction(),
               pady=10).place(x=735, y=500)

    def makeTransaction(self):
        '''
            function to initiate transaction and print the details on screen.
            '''
        bal_bef = self.getBalance()
        dict = self.sendEther()
        Label(self.root, text=' Transaction Sucessfull ', font=("Calibri", 13), fg='green').place(x=480, y=570)
        Label(self.root, text='Transaction hash is : ' + str(dict['txn_hash']), font=("Calibri", 13), fg='green').place(x=80,
                                                                                                                   y=600)  # place(x = 80, y = 630)
        Label(self.root, text=' Sender  Address is : ' + str(dict['sender_address']), font=("Calibri", 13),
              fg='green').place(
            x=80, y=630)
        Label(self.root, text='Receiver Address is : ' + str(dict['receiver']), font=("Calibri", 13), fg='green').place(x=80,
                                                                                                                   y=660)
        Label(self.root, text='Balance Before Transaction is : ' + str(bal_bef), font=("Calibri", 13), fg='green').place(
            x=80,
            y=690)
        Label(self.root, text='Balance  After Transaction is : ' + str(dict['bal']), font=("Calibri", 13), fg='green').place(
            x=80, y=720)
        Label(self.root, text='Amount of ETHER Transfered is : ' + str(self.amount.get()), font=("Calibri", 13),
              fg='green').place(
            x=80, y=750)  # place(x = 420, y = 690)

    def printBalance(self):
        pass

    def sendEther(self):
        '''
        function to send ether from account to account.
        '''
        # Getting Address from PrivateKey
        sender_address = Account.privateKeyToAccount(self.privateKey).address

        # Transaction Information
        txn = {
            'nonce': self.w3.eth.get_transaction_count(self.getAccount()),
            'to': self.receiver,
            'value': self.w3.toWei(self.amount, 'ether'),
            'gas': 100000,
            'gasPrice': Web3.toWei(50, 'gwei'),
        }

        # Signed Transaction
        signed_txn = self.w3.eth.account.sign_transaction(txn, self.privateKey)
        # Hash of the transaction.
        txn_hash = self.w3.toHex(self.w3.eth.send_raw_transaction(signed_txn.rawTransaction))

        # returning the txn_id, both accounts of transaction
        return {'txn_hash': txn_hash,
                'bal': self.getBalance(),
                'sender_address': sender_address,
                'receiver': self.receiver,
                }

    def getAccount(self):
        '''
        Fetching Account address from Private Key
        '''
        return Account.privateKeyToAccount(self.privateKey).address

    def getBalance(self):
        '''
        Function to get the balance from address fo Account.
        '''
        balanceInWei = self.w3.eth.getBalance(self.getAccount())
        balanceInEther = self.w3.fromWei(balanceInWei, 'ether')
        return balanceInEther

class MainScreen:
    def __init__(self, tk, user):
        self.root = tk
        self.user = user
        self.root.geometry('800x600+300+200')
        self.root.title('Welcome')
        self.root.resizable(0, 0)
        self.data = {}

        # Main frame
        self.f1 = Frame(self.root, width=800, height=600, bg='white').place(x=0, y=0)


# m = MainScreen(root, data)
s = Transaction(root)
root.mainloop()
