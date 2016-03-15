import matplotlib.pyplot as plt
import math
import numpy as np


class PrimeNumberAnalyzer():
    """
    Analyzes prime numbers
    """

    def __init__(self, lower, higher):
        self.run_analysis(lower, higher)

    def is_prime(self, number):
        """
        Determines whether the number "number" is in fact prime, if so, it
        returns true. Otherwise, it returns false.
        """
        if number % 2 == 0 and number > 2:
            return False

        return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

    def analyze_distribution(self, starting_number, ending_number):
        """
        Analyzes the prime numbers and returns 4 arrays:
        1) All prime numbers that end in 1
        2) All prime numbers that end in 3
        3) All prime numbers that end in 5
        4) All prime numbers that end in 7
        """
        # Creating prime number arrays
        end_in_1 = []
        end_in_3 = []
        end_in_5 = []
        end_in_7 = []

        # Identifying all prime numbers from "starting_number" and
        #   "ending_number"
        for number in range(starting_number, ending_number):
            print("Determining if " + str(number) + " is a prime number")
            if self.is_prime(number):
                remainder = number % 10

                if remainder == 1:
                    end_in_1.append(number)
                elif remainder == 3:
                    end_in_3.append(number)
                elif remainder == 5:
                    end_in_5.append(number)
                elif remainder == 7:
                    end_in_7.append(number)

        # Returning final prime number arrays
        return [end_in_1, end_in_3, end_in_5, end_in_7]

    def display_prime_number_analysis(self, prime_number_arrays, starting_number, ending_number):
        """
        Displays (using matplotlib) the distribution of prime numbers
        """
        # Creating temporary arrays
        prime_number_1 = []
        prime_number_3 = []
        prime_number_5 = []
        prime_number_7 = []

        # Array totals
        total_1 = 0
        total_3 = 0
        total_5 = 0
        total_7 = 0

        overall_total = 1.0
        for number_index in range(starting_number, ending_number):
            print("Totaling number: " + str(number_index))
            if self.is_prime(number_index):
                if number_index in prime_number_arrays[0]:
                    total_1 += 1
                elif number_index in prime_number_arrays[1]:
                    total_3 += 1
                elif number_index in prime_number_arrays[2]:
                    total_5 += 1
                elif number_index in prime_number_arrays[3]:
                    total_7 += 1

                overall_total = total_1 + total_3 + total_5 + total_7
                overall_total /= 100.0
                if overall_total == 0.0:
                    overall_total = 1.0

            prime_number_1.append(total_1)
            prime_number_3.append(total_3)
            prime_number_5.append(total_5)
            prime_number_7.append(total_7)

            prime_number_1[-1] /= overall_total
            prime_number_3[-1] /= overall_total
            prime_number_5[-1] /= overall_total
            prime_number_7[-1] /= overall_total

        print("Plotting graph")

        line_1, = plt.plot(np.asarray(prime_number_1), 'r', label='Ending in 1')
        line_3, = plt.plot(np.asarray(prime_number_3), 'g', label='Ending in 3')
        line_5, = plt.plot(np.asarray(prime_number_5), 'b', label='Ending in 5')
        line_7, = plt.plot(np.asarray(prime_number_7), 'y', label='Ending in 7')

        plt.ylabel('percentage')
        plt.xlabel('number')

        print("Total prime numbers: " + str(overall_total * 100))

        plt.legend()
        plt.show()

    def run_analysis(self, starting_number, ending_number):
        """
        Run the analysis
        """
        prime_arrays = self.analyze_distribution(starting_number, ending_number)

        self.display_prime_number_analysis(prime_arrays, starting_number, ending_number)

PrimeNumberAnalyzer(0, 100000)
