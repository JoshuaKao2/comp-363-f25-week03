from Node import Node


def filter_uppercase_and_spaces(input_string: str) -> str:
    """
    Filters the input string to retain only uppercase letters and spaces.
    """
    return "".join(
        char for char in input_string.upper() if char.isalpha() or char == " "
    )


def count_frequencies(input_string: str) -> list[int]:
    """
    Counts the frequency of each uppercase letter in the input string.
    Returns a list of 26 integers, where index 0-25 correspond to 'A'-'Z'.
    You can assume the input string contains only uppercase letters and spaces.
    And that spaces are the most frequent character, so really we dont need
    to count them.
    """
    # creates a list and makes each letter start at 0
    frequencies = [0] * 26

    #for each letter in the string
    for letter in input_string:
        #if the char is a letter and not a space
        if letter != ' ':
            # Converts A-Z to 0-25
            ascii = ord(letter) - ord('A')  
            frequencies[ascii] += 1

    return frequencies
      
    
def initialize_forest(frequencies: list[int]) -> list[Node]:
    """
    Initializes a forest (list) of Node objects for each character with a non-zero frequency.
    """
    #creates empty forest
    forest = []
    #goes through each letter
    for i in range(len(frequencies)):
        if frequencies[i] > 0:
            #creates the node, with the letter and its frequency
            ascii = ord('A') + i
            new_node = Node(frequencies[i], chr(ascii))
            forest.append(new_node)
    return forest


def build_huffman_tree(frequencies: list[int]) -> Node:
    """
    Builds the Huffman tree from the list of frequencies and returns the root Node.
    """
    forest = initialize_forest(frequencies)
    # Your code here
    while len(forest) > 1:
        s1 = get_smallest(forest)
        s2 = get_smallest(forest)
        new_node = Node(s1.get_frequency() + s2.get_frequency())
        new_node.set_left(s1)
        new_node.set_right(s2)
        forest.append(new_node)
    return forest[0]


def get_smallest(forest):
    smallest_index = 0
    for i in range(1, len(forest)):
        if forest[i] < forest[smallest_index]:
            smallest_index = i
    return forest.pop(smallest_index)



def build_encoding_table(huffman_tree_root: Node) -> list[str]:
    """
    Builds the encoding table from the Huffman tree.
    Returns a list of 27 strings, where index 0-25 correspond to 'A'-'Z'
    and index 26 corresponds to space.
    Each string is the binary encoding for that character.
    """
    pass


def encode(input_string: str, encoding_table: list[str]) -> str:
    """
    Encodes the input string using the provided encoding table. Remember
    that the encoding table has 27 entries, one for each letter A-Z and
    one for space. Space is at the last index (26).
    """
    pass


def decode(encoded_string: str, huffman_root: Node) -> str:
    """
    Decodes the encoded string using the Huffman table as a key.
    """
    pass


