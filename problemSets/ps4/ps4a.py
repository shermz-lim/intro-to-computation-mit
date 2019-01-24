# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # base case 
    # if length of sequence is 1, just return the char 
    if len(sequence) == 1:
        return [sequence]

    # Defining new list of possible permutations 
    permutations = []

    # recursive cases 
    # for each character in sequence 
    for i in range(len(sequence)):
        char = sequence[i] 
        remaining_str = sequence[:i] + sequence[i + 1:]
        # for every possible permutations in remaining string excluding char 
        for permutation in get_permutations(remaining_str):
            # form a new permutation with the character 
            new_permutation = char + permutation
            permutations.append(new_permutation)

    # returns permutations 
    return permutations 



if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['123', '132', '213', '231', '312', '321'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'bust'
    print('Input:', example_input)
    print('Actual Output:', get_permutations(example_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)



