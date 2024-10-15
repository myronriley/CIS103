def distance():
    M=float(input('miles to convert-> '))
    K=M * 1.609344
    print(M, 'miles to kilometers-> ',K)

def temperature():
    F=float(input('fahrenheit to convert-> '))
    C=(F-32)*5/9
    print(F, 'fahrenheit to celcius-> ',C)

def weight():
    P=float(input('pounds to convert-> '))
    kg=P*0.45359237
    print(P, 'pounds to kilograms-> ',P)

def main():
    distance()
    temperature()
    weight()

main()
print('done')
