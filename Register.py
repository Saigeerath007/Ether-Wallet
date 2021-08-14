from tkinter import *
from PIL import Image, ImageTk
import json
import Transfer

root = Tk()


class Register:
    def __init__(self, tk):
        self.root = tk
        self.root.geometry('800x600+300+200')
        self.root.title('Register')
        self.root.resizable(0, 0)
        self.data = {}

        # Main frame
        self.f1 = Frame(self.root, width=500, height=500, bg='white').place(x=150, y=50)

        # First name input
        l1 = Label(self.root, text='First Name *', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=70)
        self.f_name = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.f_name.place(x=220, y=100, height=30)

        # Lastname input
        l2 = Label(self.root, text='Last Name *', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=150)
        self.l_name = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.l_name.place(x=220, y=180, height=30)

        # Username input
        l3 = Label(self.root, text='Username *', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=230)
        self.u_name = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.u_name.place(x=220, y=260, height=30)

        # Password input
        l4 = Label(self.root, text='Password*', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=310)
        self.passwd = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.passwd.place(x=220, y=340, height=30)

        # email name input
        l5 = Label(self.root, text='Email*', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=390)
        self.email = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.email.place(x=220, y=420, height=30)

        # Button
        btn = Button(self.root, text='Sign Up', width=20, padx=5, pady=10, font=('roboto', 13), bg='orange',
                     fg='white', command=lambda: self.register()).place(x=240, y=460)

        # Sign in toggling
        l5 = Label(root, text='Already a User? ', font=('roboto', 6), fg='black', bg='white').place(x=450, y=520)
        btn2 = Button(self.root, text='Sign In', padx=15, pady=5, font=('roboto', 6), bg='white', fg='black',
                      command=lambda: log(root)).place(x=520, y=510)

    def register(self):
        with open('userinfo.json', 'r') as userinfo:
            self.data = json.load(userinfo)
        print(self.passwd.get(), self.u_name.get())

        if self.data.__contains__(self.u_name.get()):
            print('Username already exists')

        else:
            self.data.update(
                {
                    self.u_name.get():
                        {
                            'f_name': self.f_name.get(),
                            'l_name': self.l_name.get(),
                            'u_name': self.u_name.get(),
                            'passwd': self.passwd.get(),
                            'pvkey': None,
                            'nuemonic': None,

                        }
                })
            print('Account Created Sucessfully!!!')
            with open('userinfo.json', 'w') as file:
                json.dump(self.data, file, indent=4)

            post_authenticated(self.root, self.data[self.u_name.get()])

#########################################################################################################

class SignIn:
    def __init__(self, tk):
        self.root = tk
        self.root.geometry('800x600+300+200')
        self.root.title('SignIn')
        self.root.resizable(0, 0)
        self.data = {}

        self.f1 = Frame(self.root, width=500, height=500, bg='white').place(x=150, y=50)

        l0 = Label(root, text='Enter Your Username & Password', fg='black', bg='white', font=('roboto', 13)).place(
            x=250, y=60)

        l1 = Label(root, text='Username *', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=150)
        self.u_name = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.u_name.place(x=220, y=190, height=30)

        l2 = Label(root, text='Password *', font=('roboto', 13), fg='brown', bg='white').place(x=220, y=250)
        self.passwd = Entry(self.root, width=30, fg='black', bg='white', font=(12))
        self.passwd.place(x=220, y=290, height=30)

        btn = Button(self.root, text='Sign In', width=20, padx=5, pady=10, font=('roboto', 13), bg='orange',
                     fg='white', command=lambda: self.login()).place(x=230, y=350)

        l5 = Label(root, text='New User? ', font=('roboto', 6), fg='black', bg='white').place(x=450, y=520)
        btn2 = Button(self.root, text='Sign Up', padx=15, pady=5, font=('roboto', 6), bg='white', fg='black',
                      command=lambda: reg(root)).place(x=520, y=510)

    def login(self):
        with open('userinfo.json', 'r') as userinfo:
            self.data = json.load(userinfo)
        #
        if self.data.__contains__(self.u_name.get()) and self.data[self.u_name.get()]['passwd'] == self.passwd.get():
            # user = data[self.u_name.get()]
            print('Logged in Successfully')
            print(self.passwd.get(), self.u_name.get(), self.data[self.u_name.get()])

            post_authenticated(self.root, self.data[self.u_name.get()])

        else:
            print('No existing user')
            # quit()
            print(self.passwd.get(), self.u_name.get(), self.data)

#########################################################################################################


class CheckAccountScreen:
    def __init__(self, tk, user):
        self.user = user
        self.root = tk
        self.root.geometry('800x600+300+200')
        self.root.title('More Info...')
        self.root.resizable(0, 0)
        self.data = {}

        self.f1 = Frame(self.root, width=500, height=500, bg='white').place(x=150, y=50)

        l1 = Label(self.root, text='Create New Account', font=('roboto', 15), fg='brown', bg='white').place(x=300,
                                                                                                            y=100)
        b1 = Button(self.root, text='Get an Account', width=20, padx=5, pady=10, font=('roboto', 8), bg='orange',
                    fg='white').place(x=300, y=170)
        l2 = Label(self.root, text='--------OR--------', font=('roboto', 10), fg='brown', bg='white').place(x=340,
                                                                                                            y=250)
        l3 = Label(self.root, text='Add Existing Account', font=('roboto', 15), fg='brown', bg='white').place(x=300,
                                                                                                              y=300)

        self.pvkey = Entry(self.root, width=45, fg='black', bg='white', font=("times new roman", 12))
        self.pvkey.place(x=220, y=350, height=30)

        b2 = Button(self.root, text='Add Account', width=20, padx=5, pady=10, font=('roboto', 8), bg='orange',
                    fg='white',command=lambda : self.move_next(),).place(x=320, y=400)

    def move_next(self):
        with open('userinfo.json', 'r') as userinfo:
            self.data = json.load(userinfo)
        print('1')
        self.data[self.user['u_name']]['pvkey'] = self.pvkey.get()
        print('2')
        with open('userinfo.json', 'w') as file:
            json.dump(self.data, file, indent=4)

        self.user['pvkey'] = self.pvkey.get()

        print(f'{self.pvkey.get()} added to {self.user["f_name"]}\n', self.user)

        self.root.quit()
        Transfer.main()


#########################################################################################################


def quit():
    root.quit()


def reg(tk):
    return Register(tk)


def log(tk):
    return SignIn(tk)


def post_authenticated(tk, user):
    if not user.__contains__('pvkey'):
        user['pvkey'] = None
    if user['pvkey'] is None or user['pvkey'] == '':
        return CheckAccountScreen(root, user)
    else:
        Transfer.main(tk, user)




log(root)

# c = CheckAccountScreen(root)
root.mainloop()
