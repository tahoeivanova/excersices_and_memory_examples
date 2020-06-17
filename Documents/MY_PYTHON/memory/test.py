a = 12

def test_func( c, d,b=3):

    global a
    a = 1
    return a + b + c + d

print(test_func(1,1))
print(a)