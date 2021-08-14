# Ether-Wallet
Simple python GUI application with tkinter.
User can log in, sign up,add their account , Check their account balance and make transactions of ether to other accounts.
User data is stored in json format.

### To begin
1) Clone the project.
2) Check the requirement from requirements.txt
3) Start the Ganache on your local machine
4) Run the Init.py file to start the execution of program.
5) U can create an account and one of the private key from Ganache to your Account.
6) Now you can see the balance and make a transaction. 



### Description of files
1) Init.py starts the authentication with log in or sign up option.
   1) After successful SignUp user is navigated to add their account.
   2) Init.py has 3 class for Login, SignUp and Adding or Changing account.
2) Transfer.py has the main screen after user suceesfully logged into account with his private key.
3) BlockChain.py has all required functions for
   1) making a transaction and fetching the hashes of transaction.
   2) Fetching balance
   3) It uses web3py library to implement functions.
4) Userinfo.json stores the data of all user in json format.
5) Test.py is just for testing the transaction without authentication with function implementation
6) Main screen.py is same as Test.py but implementation is done using classes and objects.

