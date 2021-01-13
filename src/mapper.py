from typing import List


def flatten(_list: List) -> List:
    new_list = []
    for i in range(len(_list)):
        if type(_list[i]) is list:
            for j in range(len(_list[i])):
                new_list.append(_list[i][j])
        else:
            new_list.append(_list[i])

    return new_list


def get_tree_max_depth(tree: List) -> int:
    # gets the maximum depth of the tree by counting the number of times the list is 'flattened'
    # Flattening is the process of taking the list and for each list element,
    # taking all the elements in the list element and inserting them into the list
    # Additionally, it removes the original list element
    # Counts the number of times this process repeats to get max depth

    def no_lists(list_element: List) -> bool:
        lists_in_list = False

        for i in range(len(list_element)):
            if type(list_element[i]) is list:
                lists_in_list = True

        return lists_in_list

    depth = 1
    flattened_list = tree

    while no_lists(flattened_list):
        flattened_list = flatten(flattened_list)
        depth += 1

    return depth


def mapper(tree: List) -> dict:
    map_dict = {}

    def try_tree_path(path: str, tree_param: List) -> None:
        try:
            tree_value = tree_param
            path_list = list(path)
            for number in range(len(path_list)):
                tree_value = tree_value[int(path_list[number])]

            if type(tree_value) is not list and tree_value not in map_dict.values():
                map_dict[path] = tree_value
        except Exception:
            pass

    def get_all_tree_paths(length: int) -> List:
        def next_path(path: str) -> str:
            binary = int(path, 2)
            binary += 1
            return "{0:b}".format(binary)

        if length == 1:
            # Since 1^1 = 1, we hardcode a return value for a length of one
            return ["0", "1"]

        else:
            traverse_string = ""
            tree_paths = []
            for j in range(length):
                traverse_string += "0"

            tree_paths.append(traverse_string)
            while len(tree_paths) < (length ** 2):
                traverse_string = next_path(traverse_string)
                if len(traverse_string) < length:
                    # Converting to and from the binary in the next_path() function strips 'unnecessary' zeros,
                    # so this adds them back
                    for _ in range(len(traverse_string), length):
                        traverse_string = "0" + traverse_string
                tree_paths.append(traverse_string)

            return tree_paths

    max_depth = get_tree_max_depth(tree)
    all_tree_paths = []

    for i in range(1, max_depth + 1):
        all_tree_paths.append(get_all_tree_paths(i))

    all_tree_paths = flatten(all_tree_paths)

    for i in range(len(all_tree_paths)):
        try_tree_path(all_tree_paths[i], tree)

    return map_dict
