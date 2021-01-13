from encoder import encode
from decoder import decode
from tree import generate_tree


phrase = "Hello, World!"

# Generates the huffman coding tree using a given string input
letter_tree = generate_tree(phrase)

# prints the string after going through encoding
print(encode(phrase, letter_tree))

# prints the decoded string based on a tree and an encoded string
print(decode(encode(phrase, letter_tree), letter_tree))
