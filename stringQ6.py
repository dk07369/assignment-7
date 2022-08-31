x=(input("Enter a string name"))
x.strip()
match x:
    case x if ' ' in x:
        print("multi word string")
    case x if ' ' not in x:
        print("single word string")
