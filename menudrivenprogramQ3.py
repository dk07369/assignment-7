x=eval(input("1=isosceles triangle or not--, 2= right angled triangle or not--, 3=equilateral triangle or not--, 4=Exit---"))
match x:
    case 1:
        p=int(input("p: "))
        q=int(input("q: "))
        r=int(input("r: "))
        if p==q or q==r or r==p:
             print("isosceles tringle--")
        else:
            print("not isoseles tingle--")
        
    case 2:
        p=int(input("p: "))
        q=int(input("q: "))
        r=int(input("r: "))
        if p*p+q*q==r*r or p*p+r*r==q*q or q*q+r*r==p*p:
            print("it is a right angled tringle--")
        else:
            print("it is not a right angled tringle--")

    case 3:
        p=int(input("p: "))
        q=int(input("q: "))
        r=int(input("r: "))
        if p==q==r:
            print("equiletral triangle--")
        else:
             print(" not equiletral triangle--")
    case _4:
        print("Exit")

print()





        
