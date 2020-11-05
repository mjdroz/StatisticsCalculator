from RandomGenerator.randomInt import randomInt
from RandomGenerator.randomDec import randomDec
from RandomGenerator.randomIntSeed import randomIntSeed
from RandomGenerator.randomDecSeed import randomDecSeed
from RandomGenerator.randomIntList import randomIntList
from RandomGenerator.randomDecList import randomDecList
from RandomGenerator.randomListSelection import randomListSelection
from RandomGenerator.randomListSelectionSeed import randomListSelectionSeed
from RandomGenerator.randomAmountSelection import randomAmountSelection
from RandomGenerator.randomAmountSelectionSeed import randomAmountSelectionSeed

class random():

    result = 0

    def randomInt(self, start, end):
        self.result = randomInt(start, end)
        return self.result

    def randomDec(self, start, end):
        self.result = randomDec(start, end)
        return self.result

    def randomIntSeed(self, start, end, seed):
        self.result = randomIntSeed(start, end, seed)
        return self.result

    def randomDecSeed(self, start, end, seed):
        self.result = randomDecSeed(start, end, seed)
        return self.result

    def randomIntList(self, start, end, length, seed):
        self.result = randomIntList(start, end, length, seed)
        return self.result

    def randomDecList(self, start, end, length, seed):
        self.result = randomDecList(start, end, length, seed)
        return self.result

    def randomListSelection(self, list):
        self.result = randomListSelection(list)
        return self.result

    def randomListSelectionSeed(self, list, seed):
        self.result = randomListSelectionSeed(list, seed)
        return self.result

    def randomAmountSelection(self, list, num_values):
        self.result = randomAmountSelection(list, num_values)
        return self.result

    def randomAmountSelectionSeed(self, list, num_values, seed):
        self.result = randomAmountSelectionSeed(list, num_values, seed)
        return self.result