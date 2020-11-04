from RandomGenerator.randomInt import randomInt
from RandomGenerator.randomDec import randomDec
from RandomGenerator.randomIntSeed import randomIntSeed

class random():

    result = 0
    s = 0

    def randomInt(self, a, b):
        self.result = randomInt(a,b)
        return self.result

    def randomDec(self, a, b):
        self.result = randomDec(a, b)
        return self.result

    '''def randomIntSeed(self, a, b, s):
        self.result = randomIntSeed(a , b, s)
        return self.result'''