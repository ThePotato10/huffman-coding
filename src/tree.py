from typing import List

tree = []

def sort_letter_list (letter_list: List) -> List:
    # Uses Pythons builtin sorted function to sort the list
    # Uses lambda to extract value from dicts, as you can see in key param
    # Reverses the sort so that highest values are first
    return sorted(letter_list, key=lambda k: k["value"], reverse=True)

def generate_letter_list (string: str) -> List:
    # Generates the initial letter list based off the string input
    letter_list = []
    used_letters = []
    string_list = list(string)

    for i in range(len(string_list)):
        if string_list[i] in used_letters:
            # Do some shit to find the dict in the letter_list, and add 1 to it's value field
            for j in range(len(letter_list)):
                if (letter_list[j]["letters"] == string_list[i]):
                    letter_list[j]["value"] += 1
        else:
            letter_list.append({
                "value": 1,
                "letters": string_list[i]
            })
            used_letters.append(string_list[i])

    return letter_list

def add_to_tree (sorted_letter_list: List):
    elements = [sorted_letter_list[-1], sorted_letter_list[-2]]
    sorted_letter_list.pop(-1)
    sorted_letter_list.pop(-1)

    # Remove duplicates from the tree
    if elements[0]["letters"] in tree:
        tree.remove(elements[0]["letters"])
    if elements[1]["letters"] in tree:
        tree.remove(elements[1]["letters"])

    tree.append([elements[0]["letters"], elements[1]["letters"]])
    sorted_letter_list.append({
        "value": elements[0]["value"] + elements[1]["value"],
        "letters": [elements[0]["letters"], elements[1]["letters"]]
    })

    return sort_letter_list(sorted_letter_list)

def generate_tree (string: str) -> List:
    huffman_list = sort_letter_list(generate_letter_list(string))

    while (len(huffman_list) > 1):
        huffman_list = add_to_tree(huffman_list)

    # Hacky workaround to deal with the fact that the current algorithm creates a unnecessary wrapper array
    return tree[0]