from RandomGenerator.randomInt import randomInt
from RandomGenerator.randomDec import randomDec

class random():

    def randomInt(self, a, b):
        self.result = randomInt(a,b)
        return self.result

    def randomDec(self, a, b):
        self.result = randomDec(a, b)
        return self.result