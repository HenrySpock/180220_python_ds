# 01
def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    return a * b

# 02
def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days.get(day_of_week, None)

# 03
def last_element(lst):
    """Return last item in list (None if list is empty).
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if lst:
        return lst[-1]
    else:
        return None
    
# 04
def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        return 'First is greater'
    elif b > a:
        return 'Second is greater'
    else:
        return 'Numbers are equal'
    
# 05
def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    return phrase[::-1]

# 06
def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    return word.lower().count(letter.lower())

# 07
def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_count = {}
    for letter in phrase:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# 08
def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst
        else:
            return None
    elif command == "remove":
        if location == "beginning":
            return lst.pop(0)
        elif location == "end":
            return lst.pop()
        else:
            return None
    else:
        return None

# 09
def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # Remove spaces and convert to lowercase
    phrase = phrase.replace(" ", "").lower()

    # Check if the phrase is the same when reversed
    return phrase == phrase[::-1]

# 10
def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    return lst.count(search_term)

# 11
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    return result

# 12
def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    result = 1
    for num in nums:
        if num % 2 == 0:
            result *= num
    return result if result != 1 else 1

# 13
def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    return phrase.capitalize()

# 14
def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """    
    return [elem for elem in lst if elem]

# 15
def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    return [x for x in l1 if x in l2]

# 16
def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    a = []
    b = []
    for item in lst:
        if fn(item):
            a.append(item)
        else:
            b.append(item)
    return [a, b]

# 17
def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # create a dictionary to store the count of each number
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # find the number with the highest count
    max_count = 0
    max_num = None
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_num = num
    
    return max_num

# 18
def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    else:
        return None

    if make_int:
        result = int(result)

    return f"{message} {result}"

# 19
def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])
    return bool(hobbies_a & hobbies_b)

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess', 'magic'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess', 'magic'])
    
# 20
def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    return [num * 3 for num in nums if num % 4 == 0]

# 21
def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    return [f"{person['first']} {person['last']}" for person in people]

# 22
def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """
    total = 0
    for num in nums:
        if isinstance(num, float):
            total += num
    return total

# 23
def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    return all(isinstance(item, list) for item in lst)

# 24
def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    return lst[::2]

# 25
def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    seen_nums = set()
    for num in nums:
        target = goal - num
        if target in seen_nums:
            return (target, num)
        seen_nums.add(num)
    return ()

# 26
def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    frequency = {}
    for char in phrase.lower():
        if char in vowels:
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

# 27
def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return " ".join(word.capitalize() for word in phrase.split())

# 28
def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors

# 29
def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
   # If the collection is a dictionary, check if the sought value is in the values of the dictionary
    if type(collection) == dict:
        return sought in collection.values()
    
    # If the collection is a set, simply check if the sought value is in the set
    elif type(collection) == set:
        return sought in collection
    
    # If the collection is a string, list, or tuple, use the start parameter to determine where to start searching
    elif type(collection) in (str, list, tuple):
        if start is not None:
            collection = collection[start:]
        return sought in collection
    
    # If the collection is not one of the above types, return False
    else:
        return False
    
# 30
def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """ 
    # Check if num is a valid integer
    if not isinstance(num, int) or num < 0:
        return None
    else:
        # Return repeated phrase
        return phrase * num
    
# 31
def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    # Check if n is at least 3
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    # Check if phrase is longer than n
    elif len(phrase) >= n:
        return phrase[:n-3] + '...'
    # If phrase is shorter than or equal to n, return the phrase
    else:
        return phrase

# 32
def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """ 
    # Create a dictionary with keys and None values
    result_dict = dict.fromkeys(keys, None)
    
    # Update dictionary with corresponding values from the values list
    for i in range(len(values)):
        if i < len(keys):
            result_dict[keys[i]] = values[i]
    
    return result_dict

# 33
def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    # If end is not provided or is greater than the length of nums, set end to the length of nums
    if end is None or end > len(nums):
        end = len(nums)
    
    # Return the sum of the sublist from start to end
    return sum(nums[start:end + 1])

# 34
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # Convert numbers to strings to iterate over digits
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # If the lengths of the strings are different, return False
    if len(str_num1) != len(str_num2):
        return False
    
    # Create dictionaries to store the frequencies of digits in each number
    freq1 = {}
    freq2 = {}
    
    # Iterate over the digits in each number and update the corresponding dictionary
    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1
        
    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1
        
    # Compare the two dictionaries to see if they have the same frequencies
    return freq1 == freq2

# 35
def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    # Sort the list in descending order
    sorted_ages = sorted(ages, reverse=True)
    
    # Find the oldest age
    oldest_age = sorted_ages[0]
    
    # Iterate over the sorted list to find the second-oldest age
    for age in sorted_ages:
        if age < oldest_age:
            return (age, oldest_age)
    
    # If there is only one age in the list, return it twice
    return (oldest_age, oldest_age)

# 36
def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    # Create an empty set to store seen numbers
    seen = set()
    
    # Iterate over the list and check if each number has been seen before
    for num in nums:
        if num in seen:
            return num
        else:
            seen.add(num)
    
    # If no duplicates are found, return None
    return None

# 37
def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # Get the dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Initialize variables to store the sums of the diagonals
    tl_to_br_sum = 0
    bl_to_tr_sum = 0
    
    # Iterate over the rows and columns of the matrix
    for i in range(num_rows):
        for j in range(num_cols):
            # If the current element is on the TL-to-BR diagonal, add it to the sum
            if i == j:
                tl_to_br_sum += matrix[i][j]
            
            # If the current element is on the BL-to-TR diagonal, add it to the sum
            if i + j == num_rows - 1:
                bl_to_tr_sum += matrix[i][j]
    
    # Return the sum of the two diagonals
    return tl_to_br_sum + bl_to_tr_sum

# 38
def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # Get the keys of the dictionary as a list
    keys = list(d.keys())
    
    # Find the minimum and maximum keys
    min_key = min(keys)
    max_key = max(keys)
    
    # Return a tuple of the minimum and maximum keys
    return (min_key, max_key)
    
# 39
def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    # Initialize a variable to keep track of the count of greater numbers
    count = 0
    
    # Iterate over the numbers in the list
    for i in range(len(nums)):
        # Iterate over the numbers that come after the current number
        for j in range(i+1, len(nums)):
            # If the current number is less than the next number, increment the count
            if nums[i] < nums[j]:
                count += 1
    
    # Return the count of greater numbers
    return count

# fs1
def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # Hint: you may find the ord() function useful here
    # Initialize a variable to keep track of the sum of character positions
    char_sum = 0
    
    # Iterate over the characters in the word
    for char in word:
        # Find the character position by subtracting the ASCII value of 'a' or 'A' (depending on whether the character is uppercase or lowercase) from the ASCII value of the character and adding 1
        char_pos = ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 1
        # Add the character position to the sum
        char_sum += char_pos
    
    # Return True if the sum of character positions is odd, False otherwise
    return char_sum % 2 == 1

# fs2
def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # Initialize a variable to keep track of the number of open parentheses
    open_count = 0
    
    # Iterate over the characters in the string
    for char in parens:
        # If the character is an open parenthesis, increment the open count
        if char == '(':
            open_count += 1
        # If the character is a closing parenthesis, decrement the open count
        elif char == ')':
            open_count -= 1
            # If the open count is negative, there are more closing parentheses than opening parentheses, so the parentheses are not balanced
            if open_count < 0:
                return False
    
    # If the open count is not zero, there are more opening parentheses than closing parentheses, so the parentheses are not balanced
    return open_count == 0    

# fs3
def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    for i in range(len(nums) - 2):
        if (nums[i] + nums[i+1] + nums[i+2]) % 2 == 1:
            return True
    return False

# fs4
def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    s = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] in vowels:
            j -= 1
        else:
            i += 1

    return "".join(s)

# fs5
def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!
    try:
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found")