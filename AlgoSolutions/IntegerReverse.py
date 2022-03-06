import time
q = 1234757


def intRev(integer) :
    store = []
    result = 0
    
    while integer>1:
        rem = integer%10
        store.append(str(rem))
        New_int = (integer-rem)//10
        if New_int<10:
            store.append(str(New_int))
        integer = New_int

    return int("".join(store))

print(intRev(q))