from data_structures.tree import Tree
from functools import lru_cache
from random import choice, randint, shuffle
from typing import Dict, List, Tuple


import big_o

Schedule = Tuple[int, int]


def generate_schedules(
    quantity: int,
) -> Tuple[List[Schedule], int]:
    schedule = [
        (x, x + randint(0, 3))
        for x in big_o.datagen.integers(quantity, 1, 5)
    ]

    chosen_time_x = randint(1, 8)

    return schedule, chosen_time_x + randint(0, 3)


def generate_anagrams(size: int) -> Tuple[str, str]:
    first_string = big_o.datagen.strings(size)

    chars = list(first_string)

    shuffle(chars)

    second_string = "".join(chars)

    return first_string, second_string


def generate_group_anagrams(quantity: int):
    words = []

    WORD_SIZE = 20

    for _ in range(quantity):

        first, second = generate_anagrams(WORD_SIZE)

        words.append(first)
        words.append(second)

    return words


@lru_cache
def generate_integers(quantity: int) -> List[int]:
    if quantity <= 1:
        quantity = 2

    result = []

    while len(result) < quantity - 1:

        num = randint(1, quantity * 10)

        if num not in result:
            result.append(num)

    result.append(choice(result))

    return result


def generate_graph_without_cycle(
    quantity: int,
) -> Dict[int, List[int]]:
    graph = {}

    for node in range(quantity):

        neighbors = []

        if node + 1 < quantity:
            neighbors.append(node + 1)

        if node + 2 < quantity:
            neighbors.append(node + 2)

        graph[node] = neighbors

    return graph


def generate_graph_with_cycle(quantity):

    graph = {}

    for node in range(quantity):

        neighbors = []

        if node + 1 < quantity:
            neighbors.append(node + 1)

        graph[node] = neighbors

    if quantity > 1:
        graph[quantity - 1].append(0)

    return graph


def generate_tree_values(
    quantity: int,
) -> List[int]:
    values = list(range(quantity))

    shuffle(values)

    return values


def generate_tree(quantity: int):
    tree = Tree()

    for value in range(quantity):
        tree.insert_with_recursion(value)

    return tree.get_root()


def generate_balanced_bst(quantity: int):
    values = list(range(quantity))

    tree = Tree()

    def insert_middle(values):

        if not values:
            return

        middle = len(values) // 2

        tree.insert_with_recursion(
            values[middle]
        )

        insert_middle(
            values[:middle]
        )

        insert_middle(
            values[middle + 1:]
        )

    insert_middle(values)

    return (
        tree.get_root(),
        0,
        quantity - 1,
    )
