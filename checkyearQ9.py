year=eval(input("Enter a year:--"))
match year:
    case year if year%100!=0 and year%4==0:
        print("Non century leap year")
    case year if year%4==0 and year%100!=0 or year%400==0:
        print("century leap year")
    case year if year%100!=0 or year%4!=0:
        print("non century non leap year")
    case year if year%100==0 or year%4!=0:
        print("Century non leap year")
