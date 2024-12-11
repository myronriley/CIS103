def main():
# set up dictionary
    dt01={1:'I',7:'VII',13:'XIII',19:'XIX',
    2:'II',8:'VIII',14:'XIV',20:'XX',
    3:'III',9:'IX',15:'XV',21:'XXI',
    4:'IV',10:'X',16:'XVI',22:'XXII',
    5:'V',11:'XI',17:'XVII',23:'XXIII',
    6:'VI',12:'XII',18:'XVIII',24:'XXIV'}
    print('Roman Numerals')
    print(dt01)
    a=int(input('Enter Number: '))
    while a>0:
    
        
        if a in dt01:
            v01 = dt01[a]
            print(a,'-',v01)
         
        else:
            print(a,'Number is not in Dictionary')
            addtoDict = input('Add to Dictionay?: y/n: ')
            if addtoDict == 'y':
                addNum=input('Add Number and Roman Numeral to Dictionary (Roman number must be Alphabetic): ')
                dt01[a]=addNum
                print('-----')



        print(dt01)     
        a=int(input('Enter Number: '))
    print('Program Done')
main()
