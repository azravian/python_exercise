
print("this is outside \"__main__\"")
def MyDivider(n1, n2):
    return n1 / n2

def MyPow(n1,n2):
    return n1**n2

def MyProduct(n1,n2):
    return n1*n2

if __name__=="__main__":
    print("this is inside \"__main__\"")

    def test_all_func():
        print(MyDivider(10,5.0))
        print(MyPow(2, 4))
        print(MyProduct(2, 5))
    
    test_all_func()
