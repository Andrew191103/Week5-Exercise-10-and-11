def testprime(k):
    y= True
    for i in range(2,k):
        if k % i ==0:
            y = False
            break
        if k == 1:
            y= False
        return y
print(testprime(9))
