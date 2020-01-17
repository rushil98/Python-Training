INFO = [1201, "Neha", 15600.50]
#defining function
def cost_and_maintanance(size):
    if size >= 1000:
        rate = 2500
        mrate = 1.0
    else:
        rate = 2000
        mrate = 1.25
    cost = rate * size
    mcost = mrate * size
    print("cost is ", cost,"RS with monthly maintanance charges are :", mcost,"RS")

    #withdraw function
def withdraw(ls, amt):
    'to withdraw from account'
    if ls[2] >= amt:
        ls[2] -= amt
        print("current balance is",ls[2],"RS")
    else:
        print("insufficient balance")

#deposit function
def deposit(amt):
    INFO[2] += amt
    print("current balance is :",INFO[2],"RS")

#calling function
cost_and_maintanance( int(input("enter size of flat")))
withdraw(INFO, 5000)
print(INFO)
deposit(5000)
print(INFO)