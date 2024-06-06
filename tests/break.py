a = [1,2,3,4]
Break = False
while True:
    if Break:
        break
    for i in a:
        if i == 3:
            Break = True

def test():
    a = 5
    if a == 5:
        print("pierwszy if")
    elif a > 0:
        print("drugi if")

test()