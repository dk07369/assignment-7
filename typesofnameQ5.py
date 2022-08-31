x=int(input("Enter a number"))
match x:
    case x if x%2==0:
        print("saurabh shukla")
    case x if x<0 and x%2:
        print("prateek jain")
    case x if x>0 and x%2:
        print("Aditya choudhary")
