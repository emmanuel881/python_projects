def mygenerator():
    print("first item")
    yield 10
    
    print("second item")
    yield 20

    print("last item")
    yield 30

def getSeq(x):
    for i in range(x):
        yield i
        
