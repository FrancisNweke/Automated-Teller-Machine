from getpass import getpass

print('\t\t\tWELCOME TO ASIX BANK')
restart = 'Y'
retry = 0
defaultPin = '1234'
acctBalance = 67800.90
amount = 0.00
returnCard = False

while retry <= 3 and returnCard is False:
    userPin = getpass('Please enter your pin: ')
    if len(userPin) == 4:
        if userPin == defaultPin:
            while restart not in ('N', 'NO', 'No', 'no', 'n'):
                print('\nPress 1 for Balance')
                print('Press 2 for Withdrawal')
                print('Press 3 for Transfer')
                print('Press 4 to Cancel')
                option = int(input('What transaction would you like to perform? '))

                if option == 1:  # Check Account Balance
                    print(f'Your Account Balance is {acctBalance}\n')
                    restart = input(
                        'Would you like to perform another transaction? (Yes/No): ')
                    if restart in ('N', 'No', 'n', 'no'):
                        print('Thank you. Please take your card.')
                        returnCard = True
                        break
                elif option == 2:  # Perform Withdrawal
                    validAmount = False

                    while not validAmount:
                        chooseAmount = int(input(
                            'Press 1 for 5,000\nPress 2 for 10,000\nPress 3 for 15,000\nPress 4 for 20,000\nPress 5 '
                            'to enter amount\n\n'))
                        if chooseAmount == 1:
                            amount = 5000.00
                            validAmount = True
                        elif chooseAmount == 2:
                            amount = 10000.00
                            validAmount = True
                        elif chooseAmount == 3:
                            amount = 15000.00
                            validAmount = True
                        elif chooseAmount == 4:
                            amount = 20000.00
                            validAmount = True
                        elif chooseAmount == 5:
                            amount = float(input('Enter Amount: '))
                            validAmount = True
                        else:
                            print('Invalid Input...')

                    if amount < acctBalance:
                        acctBalance = acctBalance - amount
                        print('\t\tThank you. Please take your cash.\n')
                        restart = input(
                            'Would you like to perform another transaction? (Yes/No): ')
                        if restart in ('N', 'No', 'n', 'no'):
                            print('\t\tThank you. Please take your card.')
                            returnCard = True
                            break
                    else:
                        print('Insufficient Balance.')
                        break
                elif option == 3:  # Perform Transfer
                    destinationAcctNo = input('Enter destination account number: ')
                    transferAmount = float(input('Enter amount: '))

                    if len(destinationAcctNo) != 9:
                        print('Invalid Account Number')
                    elif transferAmount < acctBalance:
                        print(
                            f'Transaction Completed Successfully. The sum of {transferAmount} was transferred to {destinationAcctNo}.\n 10.0 Naira VAT was subcharged for the transaction.')
                    else:
                        print('Insufficient Balance.')
                        break
                elif option == 4:
                    confirm = input('Return Card? (Yes/No) ')

                    if confirm in ('No', 'n', 'no', 'N'):
                        restart('Y')
                    elif confirm in ('Yes', 'y', 'yes', 'Y'):
                        returnCard = True
                        print('Thank you. Please take your card.')
                        break
                    else:
                        print('Invalid Input.')
                        break
        else:  # When Pin is incorrect
            print('Incorrect Pin')
            retry = retry + 1
            if retry == 3:
                print('No more available retries. Please take your card.')
                break
    else:
        print('Invalid Pin. Please confirm that pin is 4 digits.')
        retry = retry + 1
        if retry == 3:
            print('No more available retries. Please take your card.')
            break
