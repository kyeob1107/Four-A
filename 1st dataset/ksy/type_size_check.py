def type_size(x):
    if x < 2**8 :
        print("---8")
    elif x < 2**16:
        print("---16")
    elif x < 2**32:
        print("---32")
    elif x < 2**64:
        print("---64")
    else:
        print("그외")