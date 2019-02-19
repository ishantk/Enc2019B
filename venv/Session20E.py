class BaningException(Exception):
    pass

print(">> Banking Started")
accBalance = 10000
minBalance = 2000
attempts = 0

def withdraw(amount):
    global accBalance
    global minBalance
    global attempts

    accBalance = accBalance - amount
    if accBalance > minBalance:
        print("Withdrawl Finished!! New Balance is \u20b9{}".format(accBalance))
    else:
        accBalance = accBalance + amount
        print("Withdrawl Failed!! Balance is Low \u20b9{}".format(accBalance))
        attempts += 1

    # We are crashing the App ourselves !!
    if attempts == 3:
        # error = ZeroDivisionError("Illegal Attempts")
        error = BaningException("Illegal Attempts")
        raise error


for i in range(7):
    withdraw(3000)

print(">> Banking Finished")