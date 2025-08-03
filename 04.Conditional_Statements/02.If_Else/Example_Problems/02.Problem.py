# Check year is leaf or not

year=1885

if(year%4==0 and year%100!=0) or (year % 400==0):
    print("Leap Year")
else:
    print("Not a leap Year")