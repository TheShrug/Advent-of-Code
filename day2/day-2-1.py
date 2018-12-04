def contains_count_of_any_letter(string, count):
    """ Returns bool of whether or not the provided
    string contains count number of any unique letter.
    This could be optimized further to prevent unnecessary
    processing.
    :param string:
    :param count:
    :return bool:
    """
    for char in string:
        if string.count(char) == count:
            return True
    return False


countContainsTwo = 0
countContainsThree = 0
file = open("input.txt")

for line in file:
    """
    These could be done in one function that returns a pair of booleans ¯\_(ツ)_/¯
    """
    if contains_count_of_any_letter(line, 2):
        countContainsTwo += 1
    if contains_count_of_any_letter(line, 3):
        countContainsThree += 1

print(countContainsTwo * countContainsThree)
