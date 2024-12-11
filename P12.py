def main():
 numb = [0] * 12
 for x in range(0,12,1):
     numb[x] = float(input('Enter number: '))
     print('number: ',numb[x], 'is at ',x)
 len1 = len(numb)
 print('\nnumber of elements ->',len1,'\n')
 print(numb)
 highest = max(numb)
 lowest = min(numb)
 total = sum(numb)
 print('highest -> ',max(numb))
 print('lowest -> ',min(numb))
 print('Total -> ', sum(numb))
 ave=sum(numb)/12
 print('average is ',ave)
 
main()
