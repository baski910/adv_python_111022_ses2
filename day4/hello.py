def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b

if __name__ == '__main__':
    print("calling from module:",__name__) # for current script __name__ is equal to __main__
    print("calling from module:",addnum(35,7))
    print("calling from module:",divnum(35,7))