import stress_test
from sorting_algorithms.intertion_sort import insertion_sort
from runtime_estimate import runtime_approximation
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quicksort import quicksort
from sorting_algorithms.radix_sort import radix_sort

# SORTING ALGORITHM TESTING CODE
#
# This Python script tests sorting algorithms and attempts to guess their time complexity
#
# This is fairly CPU intensive, as it tests sorting algorithms with arrays of up to 1.024.000 numbers in size!
#
# There are 4 sorting algorithms included in this package, but you may use any algorithm as long as it takes an array as
# an input, and returns the sorted array when it is done (and the function can handle massive arrays)
#
# WARNING: Do not test insersion sort with this code unless you want to fry your CPU for a half an hour!
#
# TODO: Currently O(n log n) algorithms are sometimes (depending on random number generation) mistakenyly estimated to be O(n) and vice versa, this will be fixed.



def run():
    function_to_test = merge_sort # Replace merge_sort with the name of the function you would like to test
    arr = stress_test.stress_test(function_to_test)
    runtime_approximation(arr[0], arr[1])

run()
