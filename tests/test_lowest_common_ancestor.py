from challenges.lowest_common_ancestor import (
    lowest_common_ancestor,
)

from data_structures.tree import Tree


def create_reference_tree():
    tree = Tree()

    for value in [
        20,
        10,
        30,
        5,
        15,
        25,
        35,
    ]:
        tree.insert_with_recursion(value)

    return tree


def test_nodes_on_left_subtree():
    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            5,
            15,
        )
        == 10
    )


def test_nodes_on_right_subtree():
    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            25,
            35,
        )
        == 30
    )


def test_nodes_on_opposite_sides():

    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            5,
            35,
        )
        == 20
    )


def test_left_ancestor():
    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            10,
            15,
        )
        == 10
    )


def test_right_ancestor():

    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            30,
            35,
        )
        == 30
    )


def test_same_node():
    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            15,
            15,
        )
        == 15
    )


def test_reverse_order_arguments():
    tree = create_reference_tree()

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            35,
            5,
        )
        == 20
    )


def test_single_node_tree():
    tree = Tree()

    tree.insert_with_recursion(10)

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            10,
            10,
        )
        == 10
    )


def test_degenerate_tree():
    tree = Tree()

    for value in [
        1,
        2,
        3,
        4,
        5,
    ]:
        tree.insert_with_recursion(value)

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            3,
            5,
        )
        == 3
    )


def test_deeper_tree():
    tree = Tree()

    for value in [
        50,
        30,
        70,
        20,
        40,
        60,
        80,
        10,
        25,
        35,
        45,
    ]:
        tree.insert_with_recursion(value)

    assert (
        lowest_common_ancestor(
            tree.get_root(),
            10,
            45,
        )
        == 30
    )
