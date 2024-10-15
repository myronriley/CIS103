
def distance():
    try:
        M=float(input('miles to convert-> '))
        K=M * 1.609344
        print(M, 'miles to kilometers-> ',K)
    except:
        print('data error')
def temperature():
    try:
        F=float(input('fahrenheit to convert-> '))
        C=(F-32)*5/9
        print(F, 'fahrenheit to celcius-> ',C)
    except:
        print('data error')
def weight():
    try:
        P=float(input('pounds to convert-> '))
        kg=pounds*0.45359237
        print(P, 'pounds to kilograms-> ',P)
    except:
        print('data error')
def main():
    ans='y'
    while (ans=='y') or (ans=='Y'):
        distance()
        temperature()
        weight()

        ans=input('Run again? type y or n')

main()
print('done')
