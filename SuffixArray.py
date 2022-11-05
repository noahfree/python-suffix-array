import math

# below is where you can input the name of the search file
FILENAME = "constitution.txt" #"1000-most-common-words.txt"

# class Suffix is used to create the suffix array
class Suffix:
    def __init__(self, index, suffix):
        self.index = index
        self.suffix = suffix

# function BuildSuffixArray() creates the suffix array from a given piece of text (a pattern)
def BuildSuffixArray(text):

    # first, initialize a list and a dictionary
    suffixes = []
    dictionary = {}

    # initialize an empty string
    string = ""
    # our iterator, i, is initialized to the last index in the array
    i = len(text) - 1
    # while i is greater than or equal to 0
    while i >= 0:
        # add the next letter to the string
        string = text[i] + string
        # add the suffix to the suffixes array
        suffixes.append(string)
        # add the suffix's index to the dictionary
        dictionary[string] = i
        # decrement the iterator
        i -= 1

    # sort the suffixes array alphabetically
    suffixes = sorted(suffixes)

    # initialize out suffix_array
    suffix_array = []
    # for every element in suffixes, add that suffix's index to the suffix_array
    for j in range(len(suffixes)):
        suffix_array.append(dictionary[suffixes[j]])

    # return the suffix_array
    return suffix_array

# function PrintSuffixArray() can be used to print a given suffix array created
# in the above function, not recommended on large suffix arrays
def PrintSuffixArray(suffix_array, string):
    for i in range(len(suffix_array)):
        text = ""
        for j in range(suffix_array[i], len(string)):
            text += string[j] + " "
        print(str(i) + ": " + str(suffix_array[i]) + " => " + text)

# SearchSuffixArray() is used to find how many occurences of the given pattern there are
# in the suffix array
def SearchSuffixArray(string, suffix_array, key, count):
    for i in range(len(suffix_array)):
        if string[suffix_array[i]] == key[0]:
            try:
                if key == string[suffix_array[i]:suffix_array[i]+len(key)]:
                    count += 1
                    del suffix_array[i]
                    return SearchSuffixArray(string, suffix_array, key, count)
            except:
                continue
    return count

# This is a faster version of the above function which unfortunately does not yet work
def FasterSuffixArraySearch(pattern, string, suffix_array):
    left_index = 0
    right_index = len(string)-1
    while left_index <= right_index:

        middle = 1 + math.floor((right_index - left_index)/2)
        print(pattern)
        print(string[suffix_array[middle]:])
        if pattern is string[suffix_array[middle]:]:
            return True

        elif pattern < string[suffix_array[middle]:]:
            if pattern == string[suffix_array[middle]:suffix_array[middle]+len(pattern)]:
                return True
            right_index = middle - 1
        elif pattern > string[suffix_array[middle]:]:
            left_index = middle + 1
    return False

# CompareStrings is a function created to basically simulate ==, <, and > for strings
def CompareStrings(str1, str2):
    i = 0
    while i < len(str1) and i < len(str2):
        if str1[i] != str2[i]:
            if str1[i] > str2[i]:
                return 1
            else:
                return -1
    if (len(str2) > len(str1)):
        return -1
    if (len(str1) > len(str2)):
        return 1
    return 0

# GetFileText is used to merely read a file
def GetFileText(file_name):
    file = open(file_name, "r")
    string = file.read()
    return string

# Function GetInput() gets user input for the string that the user wants to use
def GetInput():
    string = input("\nPlease enter a pattern to search for:\n")
    # the string is returned
    return string

def Main():
    count = 0
    string = GetFileText(FILENAME)
    print("\nWelcome to the suffix array program!\n")
    print("\nCreating suffix array...")
    suffix_array = BuildSuffixArray(string)
    #PrintSuffixArray(suffix_array, string)
    pattern = GetInput()
    #print(FasterSuffixArraySearch(pattern, string, suffix_array))
    result = SearchSuffixArray(string, suffix_array, pattern, count)
    #result = FasterSuffixArraySearch(pattern, string, suffix_array)
    print("\nInput \"" + pattern + "\" found " + str(result) + " times in the U.S. Constitution")

    # toggle is used to run the program again if the user chooses
    toggle = input("\nWould you like to run the program again? (y/n)\n")
    while toggle != 'y' and toggle != 'Y' and toggle != 'n' and toggle != 'N':
        toggle = input("\n\nWould you like to run the program again? (y/n)\n")

    # if the user inputes 'y' or 'Y', the Main() runs again
    if toggle == 'y' or toggle == 'Y':
        Main()

Main()
