from RandomGenerator.randomInt import randomInt
from RandomGenerator.randomDec import randomDec
from RandomGenerator.randomIntSeed import randomIntSeed
from RandomGenerator.randomDecSeed import randomDecSeed
from RandomGenerator.randomIntList import randomIntList
from RandomGenerator.randomDecList import randomDecList
from RandomGenerator.randomListSelection import randomListSelection
from RandomGenerator.randomListSelectionSeed import randomListSelectionSeed
from RandomGenerator.randomAmountSelection import randomAmountSelection

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

    def randomIntList(self, a, b, l):
        self.result = randomIntList(a, b, l)
        return self.result

    def randomDecList(self, a, b, l):
        self.result = randomDecList(a, b, l)
        return self.result

    def randomListSelection(self, list):
        self.result = randomListSelection(list)
        return self.result

    def randomListSelectionSeed(self, list):
        self.result = randomListSelectionSeed(list)
        return self.result

    def randomAmountSelection(self, list, num_values):
        self.result = randomAmountSelection(list, num_values)
        return self.result