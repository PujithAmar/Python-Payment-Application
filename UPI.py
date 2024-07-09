# modules
import time

n = time.strftime("%d/ %m/ %y")
time.time()
a = time.ctime(time.time())


# App unlocking
try:
    apikey = int(input("Enter the 4 Digit API Key to Unlock the App: "))
    print()
    if apikey == 2024:
        print("Authentication Successful 👍\n")
        f = open("balance.txt", "r")
        balance = f.read()
        bal = int(balance)

        # Mode of Banking
        while True:
            mode = input("Enter (B) for Banking or (T) for Transaction Related or (Q) to Quit:").upper()
            print()
            if mode == "B":
                try:
                    while True:
                        numb = int(input("Enter 10 Digit Mobile Number of Recipient :"))
                        print()
                        lent = len(str(numb))
                        if lent == 10:
                            print(f"Recipients UPI Id is {numb}.ybl\n")
                            cnf = input("Enter (C) to Confirm or (N) to Re-Enter : ").upper()
                            print()
                            if cnf == "C":
                                amount = input("Enter the Amount To be Transferred : ₹")
                                print()
                                if amount.isdigit():
                                    upi = int(input("Enter the Six digit UPI Pin :"))
                                    print()
                                    try:
                                        if upi == 180710:
                                            if int(amount) < bal:
                                                print(f"The Amount ₹{amount} was transferred Successfully ")
                                                print("Transaction Successful 🤩\n")
                                                # List of transactions
                                                with open("transactions.txt", 'a') as f:
                                                    f.write(f"Amount ₹{amount} was Transferred to UPI Id {numb}.ybl on {n} at {a} \n")


                                                # New Balance
                                                new_balance = bal - int(amount)
                                                with open("balance.txt", 'w+') as f:
                                                    f.write(str(new_balance))

                                                # View new balance
                                                exe = input("Would you like to view Balance (B) or (Q) to Quit:").lower()
                                                if exe == 'b':
                                                    print(f"Your Available Balance is ₹{new_balance}\n")
                                                    quit()

                                                elif exe =='Q':
                                                    quit()

                                                else:
                                                    print("Enter a proper input !")
                                            else:
                                                print("Insufficient Funds!\n")
                                                quit()

                                        else:
                                            print("Wrong UPI Pin \n")
                                            print("Transaction UnSuccessful 🧐")

                                    except ValueError:
                                            print("Enter the Six digit UPI Pin !")

                                else:
                                    print("Please Enter the Amount in Digits !")



                        else:
                            print("Please Enter '10 Digit' Mobile Number !")


                except ValueError:
                    print("Please Enter 10 Digit Mobile Number !")

            elif mode == "T":
                while True:
                    opt2 = input("Enter (B) to view Balance or (H) to view Past Transactions or (Q) to Quit : ").upper()
                    print()
                    if opt2 == "B":
                        print(f"The Balance in your Account is {balance}\n")
                        break

                    elif opt2 == "H":
                        f = open("transactions.txt", "r")
                        transaction = f.read()
                        print(transaction)
                        quit()


                    elif opt2 == "Q":
                        quit()

                    else:
                        print("Please Enter the Proper input !")

            elif mode == "Q":
                print("Exiting Application")
                quit()


            else:
                print("Please Enter the Proper Mode of Application !")


    else:
        print("Authentication UnSuccessful 👎")
        print("Please Try Again !")


except ValueError:
    print("Please Enter the 4 digit API Key!")