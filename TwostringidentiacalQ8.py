x=input("Enter 1st string ")
y=input("Enter 2nd string ")
match (x,y):
    case (x,y) if x==y:
        print("Identical")
    case (x,y) if x>y:
        print(x,y)
    case (x,y) if x<y:
        print(y,x)