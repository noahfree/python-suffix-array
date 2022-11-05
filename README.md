# Suffix Array U.S. Constitution Pattern Finder

This program is a Python script that can be run using the command "python 3 SuffixArray.py". Since math is the only import, a virtual environment is not necessary but of course can be used.

Initially, I had decided to work with a suffix tree and that I wanted to implement Ukkonen’s Algorithm for building a suffix tree for a piece of text in linear time. Unfortunately, even after multiple hours of trying I was not able to figure out the correct implementation for this and truly wrap my head around the complex algorithm that Ukkonen’s Algorithm is. Eventually, I switched to creating a suffix array instead of a suffix tree.

This program first creates a suffix array from the entire U.S. Constitution. Essentially, a suffix array is an array of indexes for a string that can then be used to search the string for patterns at a greater efficiency. This program creates the suffix array by first creating a list containing every suffix contained in the string, which is equivalent to the string's length.

Then, a dictionary is used to store the indices of each suffix. Originally I was using a class called Suffix (which is still defined at the top of the file) but I decided to switch to dictionary to see if it made things any simpler, and I ended up sticking with that method. Once we have a list of suffixes and a way of accessing the index for each suffix, we can sort the list of suffix alphabetically, ideally using an efficient sorting algorithm like QuickSort or MergeSort. Once this is done, we can iterate through the list of suffixes and add each suffix's index to the suffix array, called suffix_array in the program.

Once the suffix array is created, searching for a string can be done more efficiently. I created two different search algorithms to perform the task of finding the number of occurences of the inputted pattern in the Constitution. The first one is a fairly naive approach which iterates through the suffix array, comparing the first letter at each index in the array to the first letter of the pattern, and for any that match it is compared to the entire string.

Unfortunately, I was having some troubles with the the 2nd method which would significantly reduce the runtime of the search. This method is a binary search technique which is essentially able to cut the search pool in half on every comparison. The issues I was facing seemed very strange, something to do with comparing strings and geting unexpected values, so I was not able to finish this approach.

The primary resource I used for this assignment is the following:
https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
