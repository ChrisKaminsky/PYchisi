from random import randint
def test():
    decNum = randint(1, 10)
    decision = decNum <= 7
    return decision

for i in range(100):
    print(test())