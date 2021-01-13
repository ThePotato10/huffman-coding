from encoder import encode
from decoder import decode
from tree import generate_tree


phrase = "Hello, World!"

letter_tree = generate_tree(phrase)
print(encode(phrase, letter_tree))
print(decode(encode(phrase, letter_tree), letter_tree))
