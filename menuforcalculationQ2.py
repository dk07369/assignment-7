x=eval(input("Enter for menu 1.additin,2.subtaction,3.multiplication,4.division--"))
match x:
    case 1:
        a=int(input("Enter a number for a"))
        b=int(input("Enter a number for b"))
        x=a+b
        print("result",x)
    case 2:
        a=int(input("Enter a number for a"))
        b=int(input("Enter a number for b"))
        x=a-b
        print("result",x)
    case 3:
        a=int(input("Enter a number for a"))
        b=int(input("Enter a number for b"))
        x=a*b
        print("result",x)
    case 4:
        a=int(input("Enter a number for a"))
        b=int(input("Enter a number for b"))
        x=a/b
        print("result",x)
    case _:
        print("default")