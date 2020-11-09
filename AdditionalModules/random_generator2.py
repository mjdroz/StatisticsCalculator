from AdditionalModules.GeneratorFiles.randomInt2 import random_num_generatorInt
from AdditionalModules.GeneratorFiles.randomIntSeed2 import random_num_generatorIntSeed
from AdditionalModules.GeneratorFiles.randomDec2 import random_num_generatorDec
from AdditionalModules.GeneratorFiles.randomDecSeed2 import random_num_generatorDecSeed
from RandomGenerator.random_generator import random

class randomNumberGenerator(random):

    result = 0

    def randomNumGeneratorInt(self, start, end):
        self.result = random_num_generatorInt(start, end)
        return self.result

    def randomNumGeneratorDec(self, start, end):
        self.result = random_num_generatorDec(start, end)
        return self.result

    def randomNumGeneratorIntSeed(self, start, end, seed):
        self.result = random_num_generatorIntSeed(start, end, seed)
        return self.result

    def randomNumGeneratorDecSeed(self, start, end, seed):
        self.result = random_num_generatorDecSeed(start, end, seed)
        return self.result