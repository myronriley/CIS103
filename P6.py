print(' Calculating Calories ')
print ('-----')

answer='y'
while((answer=='y') or (answer=='Y')):
    c=(input('Enter run time'))
    q=5
    if (c.isspace()):
        print('Time must be longer than 5 minutes ')
    else:
        if(float(c)<5):
            print('Minutes:',q, 'burns' ,q*4.9, 'calories')
        else:
            while(q<=float(c)):
                print('Minutes:',q,'burns' ,q*4.9, 'calories')
                q=q+5
            print('-----')
    answer=input('Again, y/n?')
    print('-----')
print('Done')
    
