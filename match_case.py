x = 4
match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 4 if x % 2 == 0:
        print("x%2==0 and case is 4")
    case _:
        print("this is the default case")
