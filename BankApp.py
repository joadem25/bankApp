from random import randint


log_status = True
users_details = {}
users_details = {'User 1': (['Josh', 'Boss', 'joshboss@yahoo.com', 'M'], ('jboss', 'jboss')), 'User 2': (['Bisi', 'Adejumo', 'bisiadejumo@yahoo.com', 'F'], ('bisi', 'bisi'))}
account_details = {}
# account_details = {'User 1': (9551226738, 100), 'User 2': (8653233139, 100)}
while log_status == True:
    print("WELCOME TO JMB BANK".center(100))
    print("Please choose one of the following operations".center(100))
    print(f"{'1. Sign up'.center(60)}\n{'2. Sign in'.center(60)}\n{'3. Quit  '.center(60)}")

    operation = input("Type the number corresponding to your desired operation: ")
    while operation != "1" and operation != "2" and operation != "3" and operation != "jmb.developer001":
        print("Please input a valid number")
        operation = input("Type the number corresponding to your desired operation: ")
    if operation == "3":
        # break
        log_status = False
    elif operation == "jmb.developer001":
        print(users_details)
        print(account_details)
    else:
        # log_status = False

        while operation == "1":
            print(f"SIGN UP".center(100))
            print("Please input the following details")

            user_details = ["First Name", "Last Name", "Email", "Sex"]
            user_info = []
            for details in range(4):
                info = input(f"{user_details[details]}: ")
                user_info.append(info)
            print(f"Please choose Username and Password")
            user_security_details = ["Username", "Password"]
            user_security = []
            for details in range(2):
                security_details = input(f"{user_security_details[details]}: ")
                user_security.append(security_details)
            user_secured = tuple(user_security)

            check_user = []
            for n in users_details.keys():
                b = n.startswith("User")
                check_user.append(b)
            user_number = check_user.count(True)
            user_number += 1

            users_details[f"User {user_number}"] = user_info, user_secured

            account_number = randint(1000000000, 9999999999)
            account_balance = 100

            account_details[f"User {user_number}"] = account_number, account_balance
            print(f"{user_info[0]} {user_info[1]}, your Sign up is complete. Your account number is {account_number}.")
            operation = ""
            break
        while operation == "2":
            print("Please input your username and password or type 'quit' to go back to Login page")
            username = input("Username: ")
            if username == "quit":
                break
            password = input("Password: ")
            if password == "quit":
                break

            sign_in_attempt = (username, password)
            check_sign_in = []
            sign_in = True
            for x,y in users_details.values():
                if y == sign_in_attempt:
                    check_sign_in.append(True)
                else:
                    check_sign_in.append(False)
            while check_sign_in.count(True) == 0:
                print("Incorrect Username or password")
                break
            else:
                print("Log in successful")
                user_num = check_sign_in.index(True)
                user_num += 1
                user_detail_in_list = users_details.get(f"User {user_num}")
                user_account_detail = account_details.get(f"User {user_num}")
                print(f"Welcome {user_detail_in_list[0][0]} {user_detail_in_list[0][1]}")
                print(f"Account number: {user_account_detail[0]}")
                while sign_in == True:
                    print("Choose a transaction")
                    print("1. Withdraw\n2. Deposit\n3. Transfer\n4. Airtime\n5. Account Balance\n6. Log out")
                    transaction = input("Input the number corresponding to the transaction: ")
                    if transaction != "1" and transaction != "2" and transaction != "3" and transaction != "4" and transaction != "5" and transaction != "6":
                        print("Please input a valid number")
                    else:
                        if transaction == "1":
                            print("Input the amount you would like to withdraw")
                            amount_to_withdraw = float(input("Amount: "))
                            amount_to_withdraw_from = float(account_details.get(f'User {user_num}')[1])
                            balance = amount_to_withdraw_from - amount_to_withdraw
                            if balance < 0:
                                print("Insufficient funds")
                            else:
                                print("Transaction successful")
                                account_details[f"User {user_num}"] = user_account_detail[0], balance
                        elif transaction == "2":
                            print("Input the amount you would like to deposit")
                            amount = float(input("Amount: "))
                            balance = amount + float(account_details.get(f'User {user_num}')[1])
                            account_details[f"User {user_num}"] = user_account_detail[0], balance
                            print("Transaction successful")
                        elif transaction == "3":
                            print("Input account number and amount")
                            acc_num = input("Account number: ")
                            amount = float(input("Amount: "))
                            amount_to_withdraw_from = float(account_details.get(f'User {user_num}')[1])
                            balance = amount_to_withdraw_from - amount
                            if balance < 0:
                                print("Insufficient funds")
                            else:
                                print("Transaction successful")
                                account_details[f"User {user_num}"] = user_account_detail[0], balance
                        elif transaction == "4":
                            print("Input phone number and amount")
                            phone_number = input("Phone number: ")
                            amount = input("Amount: ")
                            amount_to_withdraw_from = float(account_details.get(f'User {user_num}')[1])
                            balance = amount_to_withdraw_from - amount
                            if balance < 0:
                                print("Insufficient funds")
                            else:
                                print("Transaction successful")
                                account_details[f"User {user_num}"] = user_account_detail[0], balance
                        elif transaction == "5":
                            print(f"Account balance: {account_details.get(f'User {user_num}')[1]}")  
                        elif transaction == "6":
                            sign_in = False
