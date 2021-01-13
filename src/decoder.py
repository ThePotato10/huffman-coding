from mapper import mapper
from typing import List


def decode(encoded: str, tree: List) -> str:
    letter_map = mapper(tree)
    decoded_str = ""
    encoded_list = list(encoded)

    current_key = ""
    index = 0

    while len(encoded_list) > 0:
        while current_key not in list(letter_map.keys()):
            current_key += encoded_list[index]
            index += 1

        decoded_str += letter_map[current_key]
        for i in range(index):
            encoded_list.pop(0)
        index = 0
        current_key = ""

    return decoded_str
