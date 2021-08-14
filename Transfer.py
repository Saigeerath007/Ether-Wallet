from tkinter import *
from PIL import Image, ImageTk
import json

import BlockChain


class Transfer:
    def __init__(self, tk, user):
        self.txn = {}
        self.user = user
        self.root = tk
        self.root.geometry('1050x800+300+100')
        self.root.title('More Info...')
        self.root.resizable(0, 0)
        self.data = {}

        self.f1 = Frame(self.root, width=1050, height=800, bg='white').place(x=0, y=0)
        self.f2 = Frame(self.root, width=1050, height=50, bg='#3399ff').place(x=0, y=0)
        self.f3 = Frame(self.root, width=1030, height=200, bg='#d6f5f5').place(x=10, y=55)

        l1 = Label(self.root, text='Receiver Address', font=('roboto', 13), fg='black', bg='#d6f5f5').place(x=50, y=102)
        self.receiver = Entry(self.root, width=45, fg='black', bg='white', font=(12))
        self.receiver.place(x=230, y=100, height=30)

        l2 = Label(self.root, text='Amount', font=('roboto', 13), fg='black', bg='#d6f5f5').place(x=750, y=102)
        self.amount = Entry(self.root, width=10, fg='black', bg='white', font=(12))
        self.amount.place(x=840, y=100, height=30)

        b1 = Button(self.root, text="View Balance", width=20, height=1, bg="orange", command=lambda: self.getBalance(),
                    pady=10).place(x=120, y=160)

        b2 = Button(self.root, text="Pay", width=20, height=1, bg="orange", command=lambda: self.makeTransaction(),
                    pady=10).place(x=750, y=160)

    def getBalance(self):
        # print(self.user)
        bal = BlockChain.getBalance(BlockChain.getAccount(self.user['pvkey']))
        l3 = Label(self.root, text=f'Your balance is "{bal}" ether', font=('roboto', 13), fg='green', bg='#d6f5f5').place(
            x=320, y=165)

    def makeTransaction(self):
        if self.amount.get() == '' or self.receiver.get() == '' or len(self.receiver.get()) == 42 :
            print('Check Sender Address or Amount')
            f3 = Frame(self.root, width=350, height=40, bg='#d6f5f5').place(x=320, y=165)
            l3 = Label(self.root, text='Incorect Info', font=('roboto', 10), fg='green', bg='#d6f5f5').place(
                x=650, y=210)
        else:
            self.txn = BlockChain.SendEther(self.receiver.get(), self.user['pvkey'], self.amount.get())
            print(self.txn)
            f3 = Frame(self.root, width=350, height=40, bg='#d6f5f5').place(x=320, y=165)
            l3 = Label(self.root, text=f'{self.txn["txn_hash"]}', font=('roboto', 8), fg='green', bg='#d6f5f5').place(
                x=560, y=210)


def main(root, user):
    tsfr = r = Transfer(root, user)


if __name__ == '__main__':
    global root
    root = Tk()
    main(root, {'pvkey': '370aaaac1ebf3f8e929caac84d251c7e944627b2aeeb1cc346a8dc67907f3677'})
    root.mainloop()


