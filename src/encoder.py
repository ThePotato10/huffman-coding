from mapper import mapper
from typing import List


def encode(unencoded_str: str, tree: List) -> str:
    letter_map = mapper(tree)
    encoded_str = ""
    unencoded_str_list = list(unencoded_str)

    for i in range(len(unencoded_str_list)):
        encoded_value = list(letter_map.keys())[list(letter_map.values()).index(unencoded_str_list[i])]
        encoded_str += encoded_value

    return encoded_str
