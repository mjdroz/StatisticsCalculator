# Project Outline
## Calculator Object  
     1: Properties  
         1: Result  
     2: Methods  
         1: Addition -> Calls addition static method from addition.py  
         2: Subtraction -> Calls subtraction static method from subtraction.py  
         3: Multiplication -> Calls multiplication static method from multiplication.py  
         4: Division -> Calls division static method from division.py  
         5: Square -> Calls square static method from square.py  
         6: Square Root -> Calls square root static method from square_root.py  
     3: Calculator Static Class  
         1: Methods  
             1: Addition -> Calls addition class method of add  
             2: Subtraction -> Calls subtraction class method of subtract  
             3: Multiplication -> Calls multiplication class method of multiply  
             4: Division -> Calls division class method of divide  
             5: Square -> Calls square class method of square  
             6: Square Root -> Calls square root class method of squareRoot  
     4: Operations Classes  
         1: Addition  
             1: Methods  
                 Sum of 2 numbers  
         2: Subtraction  
             1: Methods  
                 Difference of 2 numbers  
         3: Multiplication  
             1: Methods  
                 Product of 2 numbers  
         4: Division  
             1: Methods  
                 Dividend of 2 numbers  
                 Implemented divide by 0 error  
         5: Square  
             1: Methods  
                 Squaring a number (Raising to the power of 2)  
         6: Square Root  
             1: Methods  
                 Getting the square root of a number  

## Random Generator Object  
	 1: Properties:  
		 1: Result  
	 2: Methods:  
		 1: Random Integer Generator -> Generate a random integer between two numbers without a seed  
		 2: Random Decimal Generator -> Generate a random decimal between two numbers without a seed  
		 3: Random Integer Generator (Seeded) -> Generate a random integer between two numbers with a seed  
		 4: Random Decimal Generator (Seeded) -> Generate a random decimal between two numbers with a seed  
		 5: Generate List of Integers (Seeded) -> Generate a random list of integers with a seed (same values everytime)  
		 6: Generate List of Decimals (Seeded) -> Generate a random list of decimals with a seed (same values everytime)  
		 7: Select a Random Item from a List -> Select a random item from a list that is passed in  
		 8: Select a Random Item from a List (Seeded) -> Select a random item from a list that is passed in with a seed (same value everytime)  
		 9: Select N Number of Items from a List -> Select a specified amount of values that is in a list  
		 10: Select N Number of Items from a List (Seeded) -> Select a specified amount of values that is in a list with a seed (same values everytime)  
     3: Random Generator Static Classes:  
         Methods  
             1: randomInt -> Calls randomInt class method of randomInt  
             2: randomDec -> Calls randomDec class method of randomDec  
             3: randomIntSeed -> Calls randomIntSeed class method of randomIntSeed  
             4: randomDecSeed -> Calls randomDecSeed class method of randomDecSeed  
             5: randomIntList -> Calls randomIntList class method of randomIntList with a seed  
             6: randomDecList -> Calls randomDecList class method of randomDecList with a seed  
             7: randomListSelection -> Calls randomListSelection class method of randomListSelection  
             8: randomListSelectionSeed -> Calls randomListSelectionSeed class method of randomListSelectionSeed  
             9: randomAmountSelection -> Calls randomAmountSelection class method of randomAmountSelection  
            10: randomAmountSelectionSeed -> Calls randomAmountSelectionSeed class method randomAmountSelectionSeed  
     4: Random Generator Operations Classes:  
         1: randomInt  
             1: Methods  
                 Generating random integers within two numbers  
         2: randomDec  
             1: Methods  
                 Generating random decimals within two numbers  
         3: randomIntSeed  
             1: Methods  
                 Generating random integers within two numbers using a seed  
         4: randomDecSeed  
             1: Methods  
                 Generating random decimals within two numbers using a seed  
         5: randomIntList  
             1: Methods  
                 Generating random list of integers between two numbers with specified length with a seed  
         6: randomDecList  
             1: Methods  
                 Generating random list of decimals between two numbers with specified length with a seed  
         7: randomListSelection  
             1: Methods  
                 Selecting a random number from a list that is passed in  
         8: randomListSelectionSeed  
             1: Methods  
                 Selecting a random number from a list that is passed in with a seed  
         9: randomAmountSelection  
             1: Methods  
                 Selecting N number of values from a list that is passed in  
         10: randomAmountSelectionSeed  
             1: Methods  
                 Selecting N number of values from a list that is passed in with a seed  
  
## Statistics Calculator Object  
     1: Properties:  
		 1: Result  
     2: Methods:  
	     1: Calculator Object Methods:  
             1: Addition -> Calls addition static method from addition.py  
             2: Subtraction -> Calls subtraction static method from subtraction.py  
             3: Multiplication -> Calls multiplication static method from multiplication.py  
             4: Division -> Calls division static method from division.py  
             5: Square -> Calls square static method from square.py  
             6: Square Root -> Calls square root static method from square_root.py  
         2: Statistics Calculator Methods:  
             1: Mean -> Calls mean static method from mean.py  
             2: Median -> Calls medium static method from median.py  
             3: Mode -> Calls mode static method from mode.py  
             4: Variance -> Calls variance static method from variance.py  
             5: Standard Deviation -> Calls standard deviation static method from standard_deviation.py  
             6: Z-Score -> Calls z-score static method from z-score.py  
         3: Population Sampling Methods:  
             1: Simple_random_sampling -> Calls population sampling static method from simple_random_sampling.py  
             2: ConfidenceIntervalBottom -> Calls confidence interval bottom static method from confidence_interval_Bottom.py  
             3: ConfidenceIntervalTop -> Calls confidence interval top static method from confidence_interval_Top.py  
             4: Margin_of_error -> Calls margin of error static method from margin_of_error.py  
             5: Cochran_sample_size -> Calls cochran sample size static method from cochran.py  
             6: Unknown_pop_stand_deviation -> Calls unknown population standard deviation static method from unknown_population_standard_deviation.py  
     3: Statistics Calculator Static Class:  
         1: Methods:  
             1: Addition -> Calls addition class method of add  
             2: Subtraction -> Calls subtraction class method of subtract  
             3: Multiplication -> Calls multiplication class method of multiply  
             4: Division -> Calls division class method of divide  
             5: Square -> Calls square class method of square  
             6: Square Root -> Calls square root class method of squareRoot  
             7: Mean -> Calls mean class method of mean  
             8: Median -> Calls medium class method of medium  
             9: Mode -> Calls mode class method of mode  
             10: Variance -> Calls variance class method of variance  
             11: Standard Deviation -> Calls standard deviation class method of standard_deviation  
             12: Z-Score - > Calls z score class method of z_score  
             13: Simple Random Sampling -> Calls simple random sampling class method of simple_random_sampling  
             14: Confidence Interval Bottom -> Calls confidence interval bottom class method of confidenceIntervalBottom  
             15: Confidence Interval Top -> Calls confidence interval top class method of confidenceIntervalTop  
             16: Margin of Error -> Calls margin of error class method of margin_of_error  
             17: Cochran Sample Size -> Calls cochran sample size class method of cochran_sample_size  
             18: Unknown Population Standard Deviation -> Calls unknown population standard deviation class method of unknown_pop_stand_deviation  
     4: Statistics Calculator Operations Classes  
         1: Methods:  
             1: Addition  
                 1: Methods  
                     Sum of 2 numbers  
             2: Subtraction  
                 1: Methods  
                     Difference of 2 numbers  
             3: Multiplication  
                 1: Methods  
                     Product of 2 numbers  
             4: Division  
                 1: Methods  
                     Dividend of 2 numbers  
                     Implemented divide by 0 error  
             5: Square  
                 1: Methods  
                     Squaring a number (Raising to the power of 2)  
             6: Square Root  
                 1: Methods  
                     Getting the square root of a number  
             7: Mean  
                 1: Methods  
                     Mean of a set of numbers  
             8: Median  
                 1: Methods  
                     Median of a set of numbers  
             9: Mode  
                 1: Methods  
                     Mode of a set of numbers  
             10: Variance  
                 1: Methods  
                     Variance of a set of numbers  
             11: Standard Deviation  
                 1: Methods  
                     Standard deviation of a set of numbers  
             12: Z-Score  
                 1: Methods  
                     Find the z score of a set of numbers  
             13: Simple Random Sampling  
                 1: Methods  
                     Random selection of a set of numbers  
             14: Confidence Interval Bottom  
                 1: Methods  
                     Find the confidence intervals for a set of numbers and returns the bottom interval  
             15: Confidence Interval Top  
                 1: Methods  
                     Find the confidence intervals for a set of numbers and returns the top interval  
             16: Margin of Error  
                 1: Methods  
                     Takes in the confidence level z score and returns the margin of error  
             17: Cochran Sample Size  
                1: Methods  
                     Takes in the confidence level z score, the confidence level, and the test variability and then returns the cochran sample size  
                     It determines the recommended sample size before calculating the cochran sample size  
             18: Unknown Population Standard Deviation  
                 1: Methods  
                     Takes in the confidence level z score, the margin of error, and the percent of the population that you are going to sample  
  
## Random Number Generator Object:  
     1: Properties:  
		 1: Result  
     2: Methods:  
	     1: Random Generator Object Methods:  
             1: Random Integer Generator -> Generate a random integer between two numbers without a seed  
             2: Random Decimal Generator -> Generate a random decimal between two numbers without a seed  
             3: Random Integer Generator (Seeded) -> Generate a random integer between two numbers with a seed  
             4: Random Decimal Generator (Seeded) -> Generate a random decimal between two numbers with a seed  
             5: Generate List of Integers (Seeded) -> Generate a random list of integers with a seed (same values everytime)  
             6: Generate List of Decimals (Seeded) -> Generate a random list of decimals with a seed (same values everytime)  
             7: Select a Random Item from a List -> Select a random item from a list that is passed in  
             8: Select a Random Item from a List (Seeded) -> Select a random item from a list that is passed in with a seed (same value everytime)  
             9: Select N Number of Items from a List -> Select a specified amount of values that is in a list  
             10: Select N Number of Items from a List (Seeded) -> Select a specified amount of values that is in a list with a seed (same values everytime)  
         2: Random Number Generator Object Methods:  
             1: Random Integer Generator -> Generate a random integer between two numbers without a seed  
             2: Random Decimal Generator -> Generate a random decimal between two numbers without a seed  
             3: Random Integer Generator (Seeded) -> Generate a random integer between two numbers with a seed  
             4: Random Decimal Generator (Seeded) -> Generate a random decimal between two numbers with a seed  
     3: Random Generator Static Classes:  
         1: Methods  
             1: Random Generator  
                 1: randomInt -> Calls randomInt class method of randomInt  
                 2: randomDec -> Calls randomDec class method of randomDec  
                 3: randomIntSeed -> Calls randomIntSeed class method of randomIntSeed  
                 4: randomDecSeed -> Calls randomDecSeed class method of randomDecSeed  
                 5: randomIntList -> Calls randomIntList class method of randomIntList with a seed  
                 6: randomDecList -> Calls randomDecList class method of randomDecList with a seed  
                 7: randomListSelection -> Calls randomListSelection class method of randomListSelection  
                 8: randomListSelectionSeed -> Calls randomListSelectionSeed class method of randomListSelectionSeed  
                 9: randomAmountSelection -> Calls randomAmountSelection class method of randomAmountSelection  
                 10: randomAmountSelectionSeed -> Calls randomAmountSelectionSeed class method randomAmountSelectionSeed  
             2: Random Number Generator  
                 1: randomNumGeneratorInt -> Calls random_num_generatorInt class method of random_num_generatorInt  
                 2: randomNumGeneratorDec -> Calls random_num_generatorDec class method of random_num_generatorDec  
                 3: randomNumGeneratorIntSeed -> Calls random_num_generatorIntSeed class method of random_num_generatorIntSeed  
                 4: randomNumGeneratorDecSeed -> Calls random_num_generatorDecSeed class method of random_num_generatorDecSeed  
     4: Random Generator Operations Classes:  
         1: randomInt  
             1: Methods  
                 Generating random integers within two numbers  
         2: randomDec  
             1: Methods  
                 Generating random decimals within two numbers  
         3: randomIntSeed  
             1: Methods  
                 Generating random integers within two numbers using a seed  
         4: randomDecSeed  
             1: Methods  
                 Generating random decimals within two numbers using a seed  
         5: randomIntList  
             1: Methods  
                 Generating random list of integers between two numbers with specified length with a seed  
         6: randomDecList  
             1: Methods  
                 Generating random list of decimals between two numbers with specified length with a seed  
         7: randomListSelection  
             1: Methods  
                 Selecting a random number from a list that is passed in  
         8: randomListSelectionSeed  
             1: Methods  
                 Selecting a random number from a list that is passed in with a seed  
         9: randomAmountSelection  
             1: Methods  
                 Selecting N number of values from a list that is passed in  
         10: randomAmountSelectionSeed  
             1: Methods  
                 Selecting N number of values from a list that is passed in with a seed  
         11: randomNumGeneratorInt  
             1: Methods  
                 Generating random integers within two numbers  
         12: randomNumGeneratorDec  
             1: Methods  
                 Generating random decimal within two numbers  
         13: randomNumGeneratorIntSeed  
             1: Methods  
                 Generating random integers within two numbers using a seed  
         14: randomNumGeneratorDecSeed  
             1: Methods  
                 Generating random decimal within two numbers using a seed  
                   
## File Checker Object:  
     1: Properties  
         1: Number as a string  
     2: Methods  
         1: Is_valid_number -> Checks to see if the string that is being passed in is numeric.  
     3: File Checker Static Class:  
         No static class for this module  
     4: File Checker Operations Class:  
         1: Methods  
             1: Is_valid_number  
                 1: Methods  
                     Checks to see if the string being passed in is numeric  
                     Checks to see if the string being passed in contains "-" (meaning it is a negative)  
                     Checks to see if the string being passed in only contains one decimal point to avoid errors in calculation  
   
## Developer Notes:  
     1: We have combined the population sampling functions with the statistics calculator and tested them on the test_statistics.py file.  
     2: With the TA's approval we have created a new random number generator that uses the code from the Random Generator Function.  
