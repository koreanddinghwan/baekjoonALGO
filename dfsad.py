class store:
    def __init__(self, name,product1):
        self.product1 = []
        

    def addprod(self, value):
        self.product1.append(value)

    




samsung = store('samsung', [])


samsung.addprod('갤럭시')


print(samsung.product1)



         