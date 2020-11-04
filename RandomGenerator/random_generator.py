from RandomGenerator.randomInt import randomInt
from RandomGenerator.randomDec import randomDec
from RandomGenerator.randomIntSeed import randomIntSeed
from RandomGenerator.randomDecSeed import randomDecSeed

class random():

    result = 0

    def randomInt(self, a, b):
        self.result = randomInt(a,b)
        return self.result

    def randomDec(self, a, b):
        self.result = randomDec(a, b)
        return self.result

    def randomIntSeed(self, a, b):
        self.result = randomIntSeed(a , b)
        return self.result

    def randomDecSeed(self, a, b):
        self.result = randomDecSeed(a , b)
        return self.result