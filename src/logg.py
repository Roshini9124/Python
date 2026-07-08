import logging as l
'''
logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s %(funcName)s"
)

def withdraw(balance, amount):
    logging.info(f"Withdrawal requested: {amount}")

    if amount > balance:
        logging.error("Insufficient balance")
        return

    balance -= amount

    logging.info(f"Remaining Balance: {balance}")

withdraw(1000, 500)
withdraw(500, 700)'''


l.basicConfig(
    filename="bank.log",
    filemode='a',
    level=l.DEBUG,
    format="%(asctime)s %(lineno)d %(levelname)s %(message)s"
)
'''
a=5
l.info("Started")
l.debug("Value of a:%d",a)
l.warning("Zero cannot be a denominator")
l.error("Zero division error")
l.critical("calculator stopped")'''


'''def add(a,b):
    l.info("Function started")
    return a+b

print(add(5,5))'''

'''a=int(input("Enter numerator:"))
b=int(input("Enter denominator:"))
try:
    print("Result:",(a//b))
    l.info("Divided successfully")
except Exception as e:
    print("Zero division error")
    l.exception("Division by zero exception")

'''

def atm():
    print("ATM started")
    l.info("ATM started")
    try:
        n=int(input("Enter the amount:"))
        if n>10000:
            print("Large withdrawl")
            l.warning("Large withdrawl")
    except Exception as e:
            print(e)
            l.exception(e)
    else:
         print("Transaction successful")
         l.info("Transaction successful")
    
atm()