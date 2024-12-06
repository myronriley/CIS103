#name
name=input('enter name')
lenstr=len(name)
if(lenstr ==0):
    print('name may not be blank')
else:
    if name.isspace():
        print('name may not have spaces')
        else:
            if lenstr<3:
                print('must be at least 3 characters long')
                else:
                    if name.isalpha():
                        print('Valid')
                    else:
                        print('must be alphabetic')
#account number
accountnumber=input('enter account number')
lenacc=len(accountnumber)
if (lenacc ==0)
    print('account number may not be blank')
else:
    if accontnumber,isspace():
        print('account may not have spaces')
    else:
        if lenacc!=9:
            print('account number must be 9 digits ')
        else:
            if accountmumber.isnumeric():
                print('valid')
            else:
                print('account must be numeric')
#payment amount
paymentamount=input('enter payment amount')
lenamt=len(amount)
if lenamt ==0
    print('payment may not be blank')
else:
    if paymentamount.isspace():
        print('account may not have spaces')
        else:
            amt=float(paymentamount)
            if amt==0
                print('account may not be zero')
            else:
                if amt<0:
                    print('account may not be negative')
                else:
                    print('valid')
