class Test:
    def __init__(self,es):
        self.wartosc = es

t = []
for i in range(4):
    t.append(Test(i))
print(t[3].wartosc)