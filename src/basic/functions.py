
def hello():
    print("Hello world ")

def calc(a,b):
    print("add ", a, " + ", b)
    return a + b

def mytuple(a,b):
    print("add ", a, " + ", b)
    return a, b, a + b

if __name__ == '__main__':
    hello()
    print("calc...")
    r = calc ( 2, 3)
    print(r)
    r = calc (a=20, b=2)
    print(r)
    r = calc (b=10, a=2)
    print(r)
    print("calc with tuple as a result ...")
    r = mytuple (2, 4)
    print("Tuple returned : ")
    for v in r :
        print(v)
    print(r)
    a, b, c = mytuple (2, 4)
    print(a, b, c)
    # x,y = calc(15,3) # error "int object is not iterable"
    # x,y = mytuple (2, 4) # error "too many values to unpack
    # x,y,z,w = mytuple (2, 4) #error "need more than 3 values to unpack
